import csv
from pokemontcgsdk import Card
from pokemontcgsdk import Set


def GetCardsInSet(setID):
    cards = Card.where(q=("set.id:" + setID))
    infoList = []

    for card in cards:
        tcgPrices = card.tcgplayer.prices
        cardMarketPrices = card.cardmarket.prices

        if tcgPrices is None:
            continue

        cardInfo = [card.id, card.number, card.name, card.rarity, card.artist,
                    GetCardMarketPrice(tcgPrices.normal),
                    GetCardMarketPrice(tcgPrices.holofoil),
                    GetCardMarketPrice(tcgPrices.reverseHolofoil), 
                    cardMarketPrices.averageSellPrice,
                    cardMarketPrices.reverseHoloSell,
                    card.cardmarket.updatedAt]
        
        infoList.append(cardInfo)
    
    return infoList


def GetCardMarketPrice(cardPrice):
    if cardPrice is None:
        return 0.0
    else:
        return cardPrice.market
   
    
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


def ReadInSetCSV(setsListCSV):
    setsList = []

    with open(setsListCSV, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            setsList.append(row)
    
    return setsList[1:]


def GetCardPriceInfo(cardID):
    card = Card.find(cardID)

    print("TCG:")

    prices = card.tcgplayer.prices

    for attr, value in prices.__dict__.items():
        print(attr, value)
    
    print("\nCard Market:")

    prices = card.cardmarket.prices

    for attr, value in prices.__dict__.items():
        print(attr, value)

    return card.tcgplayer.prices
