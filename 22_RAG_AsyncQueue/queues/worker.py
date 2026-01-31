from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import OpenAIEmbedding
from langchain_qdrant import QdrantVectorStore

load_dotenv()

openai_client = OpenAI()

# Vector Embeddings

embedding_model = OpenAIEmbedding(
    model="text-embedding-3-large",
    )

vector_db = QdrantVectorStore.from_existing_collection (
    url="http://localhost:6333",
    collection_name="my_collection",
    embedding=embedding_model,
)

def process_query(query:str):
    print("Searchng Chunks", query)
    search_result = vector_db.similarity_search(query=query)

    context = "\n\n\n".join(f"Page Content: {result.page_content}" for result in search_result)

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
            {"role": "user", "content": query}
        ]
    )

    print(f"🤖: {response.choices[0].message.content}")
    return response.choices[0].message.content