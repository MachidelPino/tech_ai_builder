import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader
from transformers import AutoTokenizer
from langchain_text_splitters import CharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

pdfs = DirectoryLoader('documentos',glob='*.pdf').load()
tokenizer = AutoTokenizer.from_pretrained('BAAI/bge-m3')
splitter = CharacterTextSplitter.from_huggingface_tokenizer(
            tokenizer=tokenizer,chunk_size=1250, chunk_overlap=150
)

fragmentos =  splitter.split_documents(pdfs)

embeddings = OllamaEmbeddings(model='bge-m3')

vector_store = FAISS.from_documents(documents=fragmentos,embedding=embeddings)

prompt = ChatPromptTemplate(
    [("system" , "Responde usando exclusivamente el contenido que se incluye a continuación. Genera una respuesta concisa. \n\nContexto:\n{contexto}"),
    ("human", "{query}")]
)

retriever = vector_store.as_retriever()
modelo = OllamaLLM(model = "gemma3:4b") 
cadena = prompt | modelo | StrOutputParser()

pregunta = 'Cómo solicitar el seguro de viaje?'

# modelo.invoke(pregunta)

trechos = retriever.invoke(pregunta)
contexto = "\n\n".join(trecho.page_content for trecho in trechos)
# cadena.invoke({"query": pregunta, "contexto":contexto})

rag_chain = (
    {"contexto": RunnablePassthrough() | retriever,
     "query":RunnablePassthrough()}
     | prompt | modelo | StrOutputParser()
)

rag_chain.invoke(pregunta)
