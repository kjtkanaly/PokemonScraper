import csv
from pokemontcgsdk import Card
from pokemontcgsdk import Set

def GetCardsInSet(setID):

    cards = Card.where(q=("set.id:" + setID))
    infoList = []

    for card in cards:
        cardPrices = card.tcgplayer.prices

        cardInfo = [card.id, card.number, card.name, card.rarity, card.artist, 
                    CheckIfPokeCardHasPrice(cardPrices.normal), 
                    CheckIfPokeCardHasPrice(cardPrices.holofoil),
                    CheckIfPokeCardHasPrice(cardPrices.reverseHolofoil), 
                    CheckIfPokeCardHasPrice(cardPrices.firstEditionHolofoil),
                    CheckIfPokeCardHasPrice(cardPrices.firstEditionNormal),
                    card.tcgplayer.updatedAt]
        
        infoList.append(cardInfo)
    
    return infoList


def CheckIfPokeCardHasPrice(cardPrice):
    if not(cardPrice == None):
        return cardPrice.market
    else:
        return None
    
def InitPokeCSV(fileName, column):
    with open(fileName, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(column)


def AppendPokeCSV(fileName, infoList):
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        for info in infoList:
            writer.writerow(info)


def GetAllSetIDs():
    sets = Set.all()
    setsInfo = []

    for set in sets:
        setsInfo.append([set.name, set.id])

    return setsInfo
