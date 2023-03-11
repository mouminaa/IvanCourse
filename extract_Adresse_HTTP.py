from bs4 import BeautifulSoup
import requests
import csv
import os


def get_links(url):
    # Send a GET request to the URL and retrieve the response
    response = requests.get(url)
    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all the <a> tags in the HTML
    links = soup.find_all('a')
    # Extract the 'href' attribute from each of the tags
    return [link.get('href') for link in links]


def test_get_links():
    # Define the URL to test
    url = "https://sputniktech.co"
    # Define the expected output
    expected_output = ['/projects', '/blogs', '/team', '/projects', '/', '/blogs', '/projects', '/contact_us', '/', 'https://www.facebook.com/sputniktechspb/', 'https://www.instagram.com/sputnikmupa/',
                       'https://www.linkedin.com/company/sputnik-tech/', 'https://wa.me/message/4QJ2NGZ7FJQZF1', 'https://wa.me/message/4B662PIKJJV4K1', 'tel:+27682233859', '/cdn-cgi/l/email-protection', 'https://sputniktech.co/', None]
    # Call the get_links function
    output = get_links(url)
    # Create the 'output' folder if it doesn't exist already
    os.makedirs('output', exist_ok=True)
    # Write the output to a CSV file in the 'output' folder
    with open('output/links.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header row
        writer.writerow(['Links'])
        # Write each link as a row in the CSV file
        for link in output:
            writer.writerow([link])
    # Print the output and expected output        
    print("Actual output: ", output)
    print("Expected output: ", expected_output)
    # Check if the output matches the expected output
    assert output == expected_output
