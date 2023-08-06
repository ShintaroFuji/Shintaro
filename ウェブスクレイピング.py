import requests
from bs4 import BeautifulSoup

#①スクレイピング対象のURLを指定
url = "https://www.example.com"

#②URLにアクセスして、その内容を取得
response = requests.get(url)

#③BeautifulSoupを使って、取得したHTMLを解析
soup = BeautifulSoup(response.text, 'html.parser')#html.parser＝解析器

# <h1>と<p>タグのテキスト部分を取得
print(soup.select("h1"))
 
print(soup.select("p"))
