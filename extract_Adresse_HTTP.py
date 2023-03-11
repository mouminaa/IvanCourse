from bs4 import BeautifulSoup
import requests
import csv


def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')
    return [link.get('href') for link in links]


def test_get_links():
    url = "https://sputniktech.co"
    expected_output = ['/projects', '/blogs', '/team', '/projects', '/', '/blogs', '/projects', '/contact_us', '/', 'https://www.facebook.com/sputniktechspb/', 'https://www.instagram.com/sputnikmupa/',
                       'https://www.linkedin.com/company/sputnik-tech/', 'https://wa.me/message/4QJ2NGZ7FJQZF1', 'https://wa.me/message/4B662PIKJJV4K1', 'tel:+27682233859', '/cdn-cgi/l/email-protection', 'https://sputniktech.co/', None]
    output = get_links(url)
    with open('links.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Link'])
        for link in output:
            writer.writerow([link])
    print("Actual output: ", output)
    print("Expected output: ", expected_output)
    assert output == expected_output
