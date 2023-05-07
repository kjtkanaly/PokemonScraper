import csv
import numpy as np
from pokemontcgsdk import Card
from pokemontcgsdk import RestClient
import config


def getCardsInSet(setID, fileName):

    cards = Card.where(q=("set.id:" + setID))

    for card in cards:
        cardPrices = card.tcgplayer.prices

        cardInfo = [card.id, card.number, card.name, card.rarity, card.artist, 
                    checkIfPokeCardHasPrice(cardPrices.normal), 
                    checkIfPokeCardHasPrice(cardPrices.holofoil),
                    checkIfPokeCardHasPrice(cardPrices.reverseHolofoil), 
                    checkIfPokeCardHasPrice(cardPrices.firstEditionHolofoil),
                    checkIfPokeCardHasPrice(cardPrices.firstEditionNormal),
                    card.tcgplayer.updatedAt]

        appendPokeCSV(fileName, cardInfo)


def checkIfPokeCardHasPrice(cardPrice):
    if not(cardPrice == None):
        return cardPrice.market
    else:
        return None


def initPokeCSV(fileName, column):
    with open(fileName, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(column)


def appendPokeCSV(fileName, cardInfo):
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(cardInfo)


def main():

    stdCSVFile = "CrownZenith - STD Set.csv"
    ggCSVFile = "CrownZenith - GG Set.csv"
    csvColumn = ["ID", "Set Number", "Card Name", "Rarity", "Artist",
                 "Normal Price($)", "Holo Foil Price ($)", "Reverse Holo Price ($)", 
                 "First Edition Holo Price ($)", "First Edition Normal Price ($)",
                 "Updated At (YYYY/MM/DD)"]

    initPokeCSV(stdCSVFile, csvColumn)
    initPokeCSV(ggCSVFile, csvColumn)

    pokeAPIkey = config.getPokeAPIkey()
    RestClient.configure(pokeAPIkey)

    stdId = "swsh12pt5"
    ggId = "swsh12pt5gg"

    getCardsInSet(stdId, stdCSVFile)
    getCardsInSet(ggId, ggCSVFile)


if __name__ == "__main__":
    main()
