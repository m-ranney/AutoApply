from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def process_resume(resume):
    loader = PyPDFLoader(resume)
    pages = loader.load_and_split()

    chat = ChatOpenAI()

    embeddings = OpenAIEmbeddings()

    db = Chroma.from_documents(pages, embeddings)

    retriever = db.as_retriever()

    qa = RetrievalQA.from_chain_type(llm=chat, retriever=retriever)

    # Return the processed resume for further use.
    return qa
