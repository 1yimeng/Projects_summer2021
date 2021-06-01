import requests
from bs4 import BeautifulSoup

SIGNS = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
     'scorpio', 'sagitarius', 'capricorn', 'aquarius', 'pisces']
URL = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={0}"


def horoscope(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    selector = {"class": "block-horoscope-text f16 l20"}
    divs = soup.findAll("div", selector, text=True)
    return divs[0].text.strip()


def main():
    print("The signs are: {}".format(" ".join(SIGNS)))
    sign = ""
    while sign not in SIGNS:
        sign = input("Enter your sign: ").lower().strip()
    url = URL.format(SIGNS.index(sign) + 1)
    print("Your horoscope for {}:". format(sign))
    print(horoscope(url))

if __name__ == "__main__":
    main()
