
import os
import gradio as gr

from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings
)

os.environ["OPENAI_API_KEY"] = "nnnnn" #put your openai key

def setup():
    llm = OpenAI()
    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory="db", embedding_function=embedding)
    retriever = vectordb.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(llm=llm, 
                                  chain_type="stuff", 
                                  retriever=retriever, 
                                  return_source_documents=True)
    return qa_chain

chain = setup()

def get_answer(question):
    response = chain(question)
    answer = response["result"]
    source_str = ""
    for s in response["source_documents"]:
        source_str += s.page_content + "\n"

    return answer, source_str
    return "Dummy response", "Dummy source"

iface = gr.Interface(fn=get_answer, inputs="text", outputs=[
        gr.Textbox(label="Generated Answer", max_lines=5, autoscroll=False),
        gr.Textbox(label="Additional Information", max_lines=5, autoscroll=True)], 
        title="Course knowlegde bot", description="Enter your question.")
iface.launch()