import os
os.environ["OPENAI_API_KEY"] = "API key here"

from langchain.llms import OpenAI
import git
llm = OpenAI(model_name="text-davinci-003", n=1, best_of=5,max_tokens=-1)
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document
ids_to_repo = {"e4043002-b586-11ed-bddd-fd8c46e6c6fb": "https://github.com/bananaml/commitment-issues"}
embeddings = OpenAIEmbeddings()
vectorstore = Chroma("repo_embeddings", embeddings, persist_directory="repo_embeddings")
repos = {""" list repo urls here"""}
vectorstore.persist()
res, id = vectorstore.similarity_search("my build is stuck/suddenly slow",k=2)
print(id)
#print(f"Bug seems to be from {doc_to_repo[res[0].page_content]}+ or {id_to_repo[res[1].id]}")
