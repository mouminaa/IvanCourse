from bs4 import BeautifulSoup
import requests

Adresse_HTTP = requests.get("https://www.larousse.fr/dictionnaires/francais/rouge/70007")
soup = BeautifulSoup(Adresse_HTTP.content, 'html.parser')
links = soup.find_all('a')
with open('links.txt', 'w') as f:
    for link in links:
        f.write(link.get('href') + '\n')