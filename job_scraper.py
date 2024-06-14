import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

# Set up the Selenium WebDriver
driver = webdriver.Chrome()

# URL of the job site
job_site_url = "https://example-job-site.com"  # Replace with the actual job site URL

# Open the job site
driver.get(job_site_url)

# Wait for the page to load completely
time.sleep(3)

# Locate job listings (modify as per the site's structure)
job_elements = driver.find_elements(By.CLASS_NAME, 'job-listing-class')  # Modify the class name
job_links = [elem.get_attribute('href') for elem in job_elements]

# Function to extract job details
def extract_job_details(job_url):
    driver.get(job_url)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Extract job details (modify selectors as per the site's structure)
    title = soup.find('h1', class_='job-title').text.strip()
    company = soup.find('div', class_='company-name').text.strip()
    location = soup.find('div', class_='location').text.strip()
    description = soup.find('div', class_='job-description').text.strip()
    
    return {
        'Title': title,
        'Company': company,
        'Location': location,
        'Description': description,
    }

# Scrape job details
job_listings = []
for link in job_links:
    job_details = extract_job_details(link)
    job_listings.append(job_details)

# Close the driver
driver.quit()

# Create a DataFrame and save to CSV
df = pd.DataFrame(job_listings)
df.to_csv('data/job_listings.csv', index=False)
