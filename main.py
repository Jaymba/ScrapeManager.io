from pyhtml2pdf import converter
from bs4 import BeautifulSoup
import requests

home_URL = "https://www.manager.io/businesses"

page = requests.get(home_URL)

home = BeautifulSoup(page.content, features="html.parser")

page_list = home.find_all("a",class_="w-full")
urls = []


    
with open("src/html/urls.txt",'w',encoding='utf-8') as f:
    for page in page_list:

        url = 'https://www.manager.io/' + page['href']

        f.write("%s\n" % url)
        
        name = page['href']

        converter.convert(url, 'src/html/{}.pdf'.format(name))
            
            

with open("src/html/test.html", 'w', encoding='utf-8') as f:
    f.write(page.text)

#converter.convert("https://manager.io/businesses", "src/html/business.pdf")
#converter.convert("https://manager.io/users", "src/html/users.pdf")