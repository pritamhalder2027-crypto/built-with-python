from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://japanesecompass.com/learn/reading/read-n2-borantia/').text
soup = BeautifulSoup(html_text, 'html.parser')

#See the whole title
print(soup.title.text)

#find all headings
for h in soup.find_all(["h1", "h2", "h3"]):
    print(h.get_text(strip=True))

#Try to find the main article text
#Often inside <article>, <main>, or a div with specific class
article = soup.find("article") or soup.find("main") or soup.find("div",
class_=lambda c: c and "content" in c.lower())
if article:
    for p in article.find_all("p"):
        text = p.get_text(strip=True)
        if text:
            print(text)

# List some div classes to understand the layout
for div in soup.find_all("div", class_=True)[:20]:
    print(div["class"], "→", div.get_text(strip=True)[:80])

