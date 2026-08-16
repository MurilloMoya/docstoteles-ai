# 📚 Docstóteles AI

**IA inteligente sobre qualquer documentação da web**

Transforme qualquer documentação técnica em um assistente de IA capaz de responder perguntas sobre ela, usando scraping inteligente e RAG (Retrieval-Augmented Generation), com ferramentas 100% gratuitas.

---

## ✨ O que é o Docstóteles?

O Docstóteles junta **Web Scraping inteligente** (Firecrawl) com **RAG** (LangChain + Groq) para criar um assistente de IA que "aprende" qualquer documentação disponível na web.

Você cola o link de uma documentação (Django, React, Vue, etc.), o app baixa o conteúdo, indexa em um vector store e cria um chat para perguntas e respostas atualizadas, sem depender do conhecimento estático de um LLM treinado no passado.

## 🚀 Tecnologias

| Camada | Ferramenta |
|---|---|
| Interface | Streamlit |
| Web Scraping | Firecrawl |
| RAG / Orquestração | LangChain |
| LLM | Groq API (llama3-8b) |
| Embeddings | Hugging Face (`all-MiniLM-L6-v2`) |
| Vector Store | FAISS |

## 🛠️ Instalação

**1. Clone o repositório:**
```bash
git clone https://github.com/MurilloMoya/docstoteles-ai.git
cd docstoteles-ai
```

**2. Crie e ative um ambiente virtual:**
```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Configure as variáveis de ambiente:**

Copie o arquivo de exemplo e preencha com suas próprias chaves:
```bash
cp .env.example .env
```

```env
GROQ_API_KEY=sua_chave_groq
FIRECRAWL_API_KEY=sua_chave_firecrawl
FIRECRAWL_API_URL=sua_url_firecrawl
```

> Groq e Firecrawl oferecem planos gratuitos (Groq não pede cartão de crédito).

**5. Crie as pastas necessárias:**
```bash
mkdir -p data/collections
```

## 🏃 Como rodar

```bash
streamlit run docstoteles/app.py
```

Acesse pelo link exibido no terminal (geralmente `http://localhost:8501`).

## 📝 Como usar

**1. Scraping**
- Selecione o modo **Scraping** na barra lateral
- Cole a URL da documentação (ex: `https://docs.streamlit.io`)
- Dê um nome para a coleção
- Clique em **Iniciar Scraping** e aguarde o download

**2. Chat**
- Selecione o modo **Chat**
- Escolha a coleção criada
- Pergunte qualquer coisa sobre a documentação indexada

## 🌐 Sugestões de documentações para testar

- https://docs.streamlit.io
- https://python.langchain.com/docs
- https://docs.python.org/3/tutorial

## 📦 Estrutura do projeto

```
docstoteles-ai/
├── docstoteles/
│   ├── app.py
│   ├── presentation/
│   │   ├── scraping.py
│   │   └── chat.py
│   └── services/
│       ├── scraping.py
│       └── rag.py
├── data/
│   └── collections/        
├── requirements.txt
├── .env.example
└── README.md
```

## 💡 Notas

- O scraping baixa até 10 páginas por padrão (ajustável em `services/scraping.py`)
- Projeto pensado como base extensível: dá pra plugar outros LLMs, adicionar upload de arquivos locais, suporte a mais formatos, etc.
- Ferramentas usadas priorizam camada gratuita (Groq, Firecrawl free tier, Hugging Face, FAISS)

## 🧑‍💻 Autor

Desenvolvido por Murillo Moya Martins

Projeto de estudo em Engenharia de IA, com foco em RAG e pipelines de dados não-estruturados da web.

## 🙏 Créditos

Projeto desenvolvido a partir do material de aula da [Asimov Academy](https://github.com/asimov-academy), como parte da trilha de Engenharia de IA. A base do projeto (estrutura, stack e conceito original) veio do curso; a implementação, ajustes e evolução deste repositório são de autoria própria.

