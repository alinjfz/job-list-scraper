# Job List Scraper

A Python tool for scraping and extracting structured job listing
data from UK job boards. Extracts job title, company, location,
salary, and description into structured CSV format.

> This project is being evolved into
> [UK Job Market AI Radar](#) — a full pipeline with LLM-powered
> skill extraction, trend analysis, and market intelligence.

## Tech Stack
- Python 3.8+
- Selenium (browser automation)
- BeautifulSoup4 (HTML parsing)
- Pandas (data processing)

## Setup

```bash
git clone https://github.com/alinjfz/job-list-scraper.git
cd job-list-scraper
pip install -r requirements.txt
python job_scraper.py
```

## What's Next
This scraper is the foundation for a larger project that adds:
- Daily scheduled scraping via Apache Airflow
- LLM-powered skill extraction and classification
- PostgreSQL storage with trend analysis
- Graduate Visa friendly job filtering
- Market intelligence dashboard
