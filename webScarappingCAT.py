import requests
import os
from bs4 import BeautifulSoup

url="https://bschool.careers360.com/articles/cat-question-papers"

r=requests.get(url)

soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())

# Find all links to question papers
links = soup.find_all('a', href=True)
pdf_links = [link['href'] for link in links if 'Question-Paper' in link['href'] and link['href'].endswith('.pdf')]

# Create a directory to store downloaded question papers
os.makedirs('CAT_Question_Papers', exist_ok=True)

# Download each PDF
for pdf_link in pdf_links:
    pdf_url = pdf_link if pdf_link.startswith('http') else f'https://www.careers360.com{pdf_link}'
    pdf_response = requests.get(pdf_url)
    pdf_name = pdf_url.split('/')[-1]

    with open(os.path.join('CAT_Question_Papers', pdf_name), 'wb') as file:
        file.write(pdf_response.content)
    print(f'Downloaded {pdf_name}')

print('All question papers have been downloaded successfully!')