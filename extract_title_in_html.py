from bs4 import BeautifulSoup
import csv
import os


def extract_article_titles(html):
    # Create a BeautifulSoup object from the HTML string
    soup = BeautifulSoup(html, 'html.parser')
    # Find all the headings in the HTML
    titles = soup.find_all(['h1', 'h2', 'h3'])
    # Return the text content of the headings
    return [title.get_text() for title in titles]


def test_extract_article_titles():
    # Read the HTML file
    with open('input/test.html', 'r') as file:
        html = file.read()
    # Define the expected output    
    expected_output = ['Test Heading 1', 'Test Heading 2',
                       'Test Heading 3', 'Another Test Heading 2']
    # Call the function and store the output
    output = extract_article_titles(html)
    # Create the output directory if it doesn't exist
    os.makedirs('output', exist_ok=True)
    # Write the output to a CSV file in the output directory
    with open('output/titles.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the headings of the columns
        writer.writerow(['Title'])
        # Write each title in a row
        for title in output:
            writer.writerow([title])
    # Check if the output is as expected using an assertion statement of pytest     
    assert output == expected_output
