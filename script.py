import requests
from bs4 import BeautifulSoup
import pandas as pd
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new.settings')  

django.setup()
from news.models import NewsArticle  # 

def scrape_indiatv_news_headings(url):
   
    response = requests.get(url)

    # 
    soup = BeautifulSoup(response.content, 'html.parser')

  
    headings = soup.find_all('h2', class_='title')  #

    #
    news_data = []
    for heading in headings:
        title = heading.text.strip()
        link = heading.find('a')['href'] if heading.find('a') else None
        news_data.append({'title': title, 'link': link})

    return news_data


indiatv_url = 'https://www.indiatvnews.com/'


headings_and_links = scrape_indiatv_news_headings(indiatv_url)

# 
df = pd.DataFrame(headings_and_links)
excel_file = 'indiatvnews.xlsx'
df.to_excel(excel_file, index=False)
print(f"Scraped data saved to {excel_file}")

# l
for data in headings_and_links:
    news_article = NewsArticle.objects.create(title=data['title'], url=data['link'])
    news_article.save()

print("Data inserted into the NewsArticle model.")
