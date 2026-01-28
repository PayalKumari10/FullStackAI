from multiprocessing import context
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

openai_client = OpenAI()

# Vector Embedding
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333", 
    collection_name="learning_rag" ,
    embedding=embedding_model
)


#Take user input 

user_query = input("Ask something: ")

#Relevant chunks from the vector db
search_result = vector_db.similarity_search(query=user_query)

SYSTEM_PROMPT = f"""
You are a helpful AI Assistant who answers user query based on the available context 
retrived from a PDF file along with page_contents and page number.

You should only ans the user based on the context and navigate the user to open the right page number to know more.


Context:
{context}
"""

response = openai_client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]
)

print(f"🤖: {response.choices[0].message.content}")