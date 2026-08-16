import os
from firecrawl import FirecrawlApp



class ScrapingService:
    def __init__(self):
        self.api_key=os.getenv("FIRECRAWL_API_KEY")
        self.api_url=os.getenv("FIRECRAWL_API_URL")

        self.app=FirecrawlApp(api_key=self.api_key,api_url=self.api_url)

    def scrape_website(self,url,collection_name):
        try:
            map_result=self.app.map_url(url)
            if hasattr(map_result,"links"):
                links=map_result.links
            elif hasattr(map_result,"data") and hasattr(map_result.data,"links"):
                links=map_result.data.links
            else:
                links=getattr(map_result,"links",[])

            if not links:
                raise Exception("Nenhum link encontrado")

            links=[l.url if hasattr(l,"url") else l["url"] if isinstance(l,dict) else l for l in links]

            print(f"Encontrados{len(links)} links")

            scrap_result=self.app.batch_scrape_urls(links)

            if hasattr(scrap_result,"data"):
                scrap_data=scrap_result.data
            else:
                scrap_data = scrap_result.get("data",[]) if hasattr(scrap_result,"get") else []
            collection_path=f"data/collections/{collection_name}"
            os.makedirs(collection_path,exist_ok=True)


            saved_cont=0
            for i, page in enumerate(scrap_data,1):
                if hasattr(page,"markdown")and page.markdown:
                    mardown_content=page.markdown
                elif hasattr(page,"data")and hasattr(page.data,"markdown"):
                    mardown_content=page.data.markdown
                elif isinstance(page,dict)and page.get("markdown"):
                    mardown_content=page["markdown"]
                else:
                    continue

                with open(f"{collection_path}/{i}.md","w",encoding="utf-8")   as f:
                    f.write(mardown_content)
                saved_cont+=1
            return{"success":True,"files":saved_cont}
        except Exception as e:
            print(f"ERRO NO SCRAPING!!! {str(e)}")
            return {"success": False, "error": str(e)}


