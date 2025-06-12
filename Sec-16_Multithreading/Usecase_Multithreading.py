'''
Real-world Example : Multithreading for I/O-bound Tasks
Scenario : Web Scraping
Web Scraping ogten involves making numerous network requests to fetch web pages. These tasks are I/O-bound because they spend a lot of time waiting for responses from servers. Multithreading can significantly.
'''


import threading
import requests
from bs4 import BeautifulSoup

urls=[
    'https://python.langchain.com/v0.2/docs/tutorials/',
    'https://python.langchain.com/v0.2/docs/concepts/',
    'https://python.langchain.com/v0.2/docs/integrations/platforms/'
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
print("All web pages fetched")