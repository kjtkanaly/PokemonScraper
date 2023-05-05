from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.action_chains import ActionChains
import time
import numpy as np


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

def webMain(url):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(2)

    cardElements = driver.find_elements(By.CLASS_NAME, "card ")

    cardLinks = []
    allCardPrices = np.zeros((1, len(cardElements)))


    for cardElement in cardElements:
        print(cardElement.text)

        linkElement = cardElement.find_element(By.XPATH, ".//a")

        cardLinks.append(linkElement.get_attribute("href"))

        #print(linkElement)
        '''
        cardElement.click()

        priceElements = driver.find_elements(By.CLASS_NAME, "price")

        cardPrices = np.empty((0))

        for priceElement in priceElements:
            if priceElement.text[0] == "$":
                cardPrices = np.append(cardPrices, float(priceElement.text[1:]))

        np.append(allCardPrices, np.round(np.mean(cardPrices), 2))

        driver.back()
        time.sleep(2)
        '''

    print(cardLinks)

def testNP():
    priceTexts = ['0.01', '0.35', '1.23']
    cardPrices = np.empty((0))

    for priceText in priceTexts:
        cardPrices = np.append(cardPrices, float(priceText))

    print(cardPrices)
    print(np.round(np.mean(cardPrices), 2))


def main():

    stdURL = "https://www.pokellector.com/Crown-Zenith-Expansion/"
    ggURL = "https://www.pokellector.com/Crown-Zenith-Galarian-Gallery-Expansion/"

    '''
    stdSetHTML = getUrlHTML(stdURL)
    ggSetHTML = getUrlHTML(ggURL)

    divClass = "plaque"
    stdSet = divTextScrap(html=stdSetHTML, divClass=divClass)
    ggSet = divTextScrap(html=ggSetHTML, divClass=divClass)

    coloumns = ["Number", "Name"]
    stdCSVFile = "CrownZenith - STD Set.csv"
    ggCSVFile = "CrownZenith - GG Set.csv"

    logIntoCSV(stdSet, stdCSVFile)
    logIntoCSV(ggSet, ggCSVFile)
    '''

    webMain(stdURL)
    # testNP()




if __name__ == "__main__":
    main()
