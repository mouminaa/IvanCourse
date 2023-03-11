from bs4 import BeautifulSoup
import csv

def extract_article_titles(html):
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all(['h1', 'h2', 'h3'])
    return [title.get_text() for title in titles]



# `pytest extract_title_in_html.py::test_extract_article_titles` to run the test
def test_extract_article_titles():
    with open('test.html', 'r') as file:
        html = file.read()
    expected_output = ['Test Heading 1', 'Test Heading 2',
                       'Test Heading 3', 'Another Test Heading 2']
    output = extract_article_titles(html)
    with open('titles.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title'])
        for title in output:
            writer.writerow([title])
    assert output == expected_output
    
    

    
