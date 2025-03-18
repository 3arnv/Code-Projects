import requests
from bs4 import BeautifulSoup

def fetch_latest_articles(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')

    latest_articles = []
    for article in articles:
        title = article.find('h2').get_text(strip=True)
        link = article.find('a')['href']
        latest_articles.append({'title': title, 'link': link})

    return latest_articles

def main():
    url = 'https://example-news-website.com'
    articles = fetch_latest_articles(url)

    if not articles:
        print("No articles found.")
        return

    print("Latest Articles:")
    for idx, article in enumerate(articles, start=1):
        print(f"{idx}. {article['title']}")
        print(f"   Link: {article['link']}")

if __name__ == "__main__":
    main()