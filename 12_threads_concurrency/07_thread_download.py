import threading
import requests
import time

def download(url):
    print(f"Starting download from {url}")
    resp = requests.get(url)
    print(f"Finished downloading from {url}, size: {len(resp.content)}bytes")

urls = [
    "https://blush.design/api/download?shareUri=3rg7RA3j7&w=800&h=800&fm=png"
    "https://blush.design/api/download?shareUri=3rg7RA3j7&w=800&h=800&fm=png"
    "https://blush.design/api/download?shareUri=3rg7RA3j7&w=800&h=800&fm=png"
]    

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()    

end = time.time()

print(f"All downloads done in {end - start:.2f} seconds")