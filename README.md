Python project for web scrapping using [BeautifulSoup4](https://pypi.org/project/beautifulsoup4) library. The main purpose of this project is to scrape job postings from [governmentjobs.com](https://governmentjobs.com) and [Indeed](https://indeed.com/).

## Getting Started

First, create the virtual environment

```bash
python3 -m venv myenv
```

Activate the virtual environment

```bash
myenv\Scripts\activate # Windows

source myenv/bin/activate # macOS/Linux
```

Install dependencies

```bash
pip install -r requirements.txt
```

Update requirements.txt, when there is update in dependecies

```bash
pip freeze > requirements.txt
```

Run the development scraper:

```bash
python scrape_top_500_job_titles_from_indeed.py
```

## More Info

Cron Job time

```bash
"0 0 1 * *" // Will run every month
```
