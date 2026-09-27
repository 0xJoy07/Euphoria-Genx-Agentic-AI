# Euphoria GenX 2026 — Agentic AI Industrial Training

Industrial training program referred by **Narula Institute of Technology** to **Euphoria GenX**, focused on Agentic AI concepts and hands-on Python development.

|||
|-----|--------|
| **Institute** | Narula Institute of Technology |
| **Training Partner** | Euphoria GenX |
| **Domain** | Agentic AI |
| **Year** | 2026 |

## Days

| Day | Topics |
|-----|--------|
| Day 1 | Python basics — conditionals, loops, functions |
| Day 2 | Data structures — Lists, Tuples, Dictionaries |
| Day 3 | Data structures continued |
| Day 4 | LangChain + Google Gemini — working with LLMs |
| Day 5 | RAG — Document loading, text chunking |
| Day 6 | RAG Part 2 — Embeddings and Vector Databases (ChromaDB) |
| Day 7 | RAG Part 3 — Vector DB loading, MMR Retrieval & Context-based Q&A |
| Day 8 | Agentic AI — Tool calling & Agent creation with LangChain & Groq |
| Day 9 | Agentic AI Part 2 — Stateful Agents (LangGraph Memory `InMemorySaver`) & Multimodal Report Analysis Agent |

## Tech Stack & Tools

- **Core**: Python 3.10+, Jupyter Notebook
- **Frameworks & Orchestration**: LangChain, LangGraph
- **LLM & Vision Providers**: Google Gemini (`langchain-google-genai`), Groq (`langchain-groq`)
- **Vector Database**: ChromaDB (`langchain-chroma`)
- **Document Processing**: PyPDF, LangChain Text Splitters

## Setup & Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/0xJoy07/Euphoria-Genx-Agentic-AI.git
   cd Euphoria-Genx-Agentic-AI
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the relevant day's folder or root:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

