from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv


def divTextScrap(html, divClass, debug=False):
    soup = BeautifulSoup(html, "html.parser")

    cards = soup.find_all("div", {"class": divClass})

    if debug:
        for card in cards:
            print(card.text)
    
    return cards


def getUrlHTML(url):

    page = urlopen(url)
    return page.read().decode("utf-8")


def parseCardInfo(cardText):

    pkmnNumber = cardText.split("#")[1]
    pkmnNumber = pkmnNumber.split()[0]

    pkmnName = cardText.split("- ")[1]

    return [pkmnNumber, pkmnName]


def logIntoCSV(cardList, csvFile):
    
    for card in cardList:
        parseCardInfo(card.text)

    with open(csvFile, 'a', newline='\n') as file:
        writer = csv.writer(file)

        for card in cardList:
            cardInfo = parseCardInfo(card.text)
            writer.writerow(cardInfo)

        file.close()


def main():

    stdURL = "https://www.pokellector.com/Crown-Zenith-Expansion/"
    stdSetHTML = getUrlHTML(stdURL)

    ggURL = "https://www.pokellector.com/Crown-Zenith-Galarian-Gallery-Expansion/"
    ggSetHTML = getUrlHTML(ggURL)

    divClass = "plaque"
    stdSet = divTextScrap(html=stdSetHTML, divClass=divClass)
    ggSet = divTextScrap(html=ggSetHTML, divClass=divClass)

    coloumns = ["Number", "Name"]
    stdCSVFile = "CrownZenith - STD Set.csv"
    ggCSVFile = "CrownZenith - GG Set.csv"

    logIntoCSV(stdSet, stdCSVFile)
    logIntoCSV(ggSet, ggCSVFile)


if __name__ == "__main__":
    main()
