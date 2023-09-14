from pokemontcgsdk import RestClient
import TcgPKMN as TP
import config

def LoopOverEachSet(setsList):
    for set in setsList:
        setName = set[0]
        setID = set[1]
        setFileName = "CSVs/" + setName + ".csv"

        GetSetCardsInfo(setID, setFileName)

def GetSetCardsInfo(setID, setCSVFile):
    csvColumn = ["ID", "Set Number", "Card Name", "Rarity", "Artist",
                 "TCG Normal", "TCG Holo", "TCG Reverse",
                 "Normal Price($)", "Reverse Holo Price ($)", 
                 "Updated At (YYYY/MM/DD)"]

    TP.InitPokeCSV(setCSVFile, csvColumn)
    infoList = TP.GetCardsInSet(setID)
    TP.AppendPokeCSV(setCSVFile, infoList)

def GetSetIDs(idsFileName):
    setsInfo = TP.GetAllSetIDs()

    csvColumn = ["Name", "ID"] 
    TP.InitPokeCSV(idsFileName, csvColumn)
    TP.AppendPokeCSV(idsFileName, setsInfo)

def GetSetIDsFromCSV(setsListCSV):
    # Get List of sets and their ids
    return TP.ReadInSetCSV(setsListCSV)

def GetPriceOfCard(cardID):
    cardPriceInfo = TP.GetCardPriceInfo(cardID)
    print(cardPriceInfo)


def main():
    pokeAPIkey = config.getPokeAPIkey()
    RestClient.configure(pokeAPIkey)

    stdCSVFile = "Jungle" # "CrownZenith - STD Set.csv"
    stdId = "base2" # "swsh12pt5"
    # GetSetCardsInfo(stdId, stdCSVFile)

    idsFileName = "All Pokemon Set IDs.csv"
    # GetSetIDs(idsFileName)

    setsListCSV = "Sets we have.csv"
    setsList = GetSetIDsFromCSV(setsListCSV)
    LoopOverEachSet(setsList)

    # Playing With Prices
    cardID = "base2-56"
    # GetPriceOfCard(cardID)

if __name__ == "__main__":
    main()