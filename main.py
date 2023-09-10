from pokemontcgsdk import RestClient
import TcgPKMN as TP
import config

def LoopOverEachSet(setsList):
    for set in setsList:
        setName = set[0]
        setID = set[1]
        setFileName = setName + ".csv"

        GetSetCardsInfo(setID, setFileName)

def GetSetCardsInfo(setID, setCSVFile):
    csvColumn = ["ID", "Set Number", "Card Name", "Rarity", "Artist",
                 "Normal Price($)", "Holo Foil Price ($)", "Reverse Holo Price ($)", 
                 "First Edition Holo Price ($)", "First Edition Normal Price ($)",
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

def main():
    pokeAPIkey = config.getPokeAPIkey()
    RestClient.configure(pokeAPIkey)

    stdCSVFile = "CrownZenith - STD Set.csv"
    stdId = "swsh12pt5"
    # GetSetCardsInfo(stdId, stdCSVFile)

    idsFileName = "All Pokemon Set IDs.csv"
    # GetSetIDs(idsFileName)

    setsListCSV = "Sets we have.csv"
    setsList = GetSetIDsFromCSV(setsListCSV)
    LoopOverEachSet(setsList)


if __name__ == "__main__":
    main()
