import csv
import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com"

data = []

for page in range(1, 51):  # 1 al 50
    if page == 1:
        url = URL
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    try:
        response = requests.get(url)
        response.encoding="utf-8"
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article")


        for book in books:
            title = book.find("h3").find("a")["title"]
            precio = book.find("p", class_="price_color").text
            rating = book.find("p", class_="star-rating")["class"][1]
            data.append({
                'title': title,
                'price': precio,
                'rating': rating
                })
            
        print(f"✅ Page {page}/50 scraped — {len(books)} books found")

    except Exception as e:
        print(f"❌ Error on page {page}: {e}")
    
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price", "rating"])
    writer.writeheader()
    writer.writerows(data)

print(f"{len(data)} books scraped!")