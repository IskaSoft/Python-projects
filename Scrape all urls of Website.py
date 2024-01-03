from bs4 import BeautifulSoup
import requests
# creating empty list
urls = []
#function created
def scrape(site):
  r = requests.get(site)
  s = BeautifulSoup(r.text, "html.parser")
  for i in s.find_all("a"):
    href = i.attrs['href']
    if href.startswith("/"):
      site = site + href
      if site not in urls:
        urls.append(site)
        print(site)
        scrape(site)
if __name__ == "__main__":
# website to be scrape
site = "http://example.webscraping.com//"
# calling function
scrape(site)