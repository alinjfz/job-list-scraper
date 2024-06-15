import requests
from bs4 import BeautifulSoup
import pandas as pd

# Read the HTML file
with open('indeed-source.html', 'r', encoding='utf-8') as file:
    page_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')

# Define a function to extract job information
def extract_job_info(job_card):
    title = job_card.find('h2', class_='jobTitle').text.strip() if job_card.find('h2', class_='jobTitle') else 'N/A'
    company = job_card.find('span', {'data-testid': 'company-name'}).text.strip() if job_card.find('span', {'data-testid': 'company-name'}) else 'N/A'
    location = job_card.find('div', {'data-testid': 'text-location'}).text.strip() if job_card.find('div', {'data-testid': 'text-location'}) else 'N/A'
    summary = job_card.find('div', class_='css-9446fg eu4oa1w0').text.strip() if job_card.find('div', class_='css-9446fg eu4oa1w0') else 'N/A'
    posted = job_card.find('span', {'data-testid': 'myJobsStateDate'}).text.strip() if job_card.find('span', {'data-testid': 'myJobsStateDate'}) else 'N/A'
    return {
        'title': title,
        'company': company,
        'location': location,
        'summary': summary,
        'posted': posted
    }
# Find all job cards on the page
job_cards = soup.find_all('li', class_='css-5lfssm eu4oa1w0')
# Extract job information from each job card
jobs = []
for job_card in job_cards:
    job_info = extract_job_info(job_card)
    jobs.append(job_info)

# # Print the extracted job information
# for job in jobs:
#     print(f"Title: {job['title']}")
#     print(f"Company: {job['company']}")
#     print(f"Location: {job['location']}")
#     print(f"Summary: {job['summary']}")
#     print('---')

# Create a DataFrame and save to CSV
df = pd.DataFrame(jobs)
df.to_csv('./data/job_listings.csv', index=False)
