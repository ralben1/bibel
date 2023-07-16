import requests
from bs4 import BeautifulSoup

class Bible:
    def __init__(self) -> None:
        self.URL = "https://dailyverses.net/de/zufalls-bibelvers"

    def get_vers(self):
        page = requests.get(self.URL)
        soup = BeautifulSoup(page.content, "html.parser")
        quote = soup.find_all("span", class_="v1")[0]
        stelle = soup.find_all("a", class_="vc")[0]
        return [quote.text, stelle.text]


