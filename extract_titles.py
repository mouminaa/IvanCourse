from bs4 import BeautifulSoup
import csv

def extract_article_titles(html):
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all(['h1', 'h2', 'h3'])
    return [title.get_text() for title in titles]

def main(page):
    with open(page) as f:
        html = f.read()
    titles = extract_article_titles(html)
    with open('article_titles.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Title:'])
        for title in titles:
            writer.writerow([title])

if __name__ == '__main__':
    main('contact.html') 
    main('Page.html') 
    
