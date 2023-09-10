from pokemontcgsdk import RestClient
import TcgPKMN as TP
import config

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

def main():
    pokeAPIkey = config.getPokeAPIkey()
    RestClient.configure(pokeAPIkey)

    stdCSVFile = "CrownZenith - STD Set.csv"
    stdId = "swsh12pt5"
    # GetSetCardsInfo(stdId, stdCSVFile)

    idsFileName = "All Pokemon Set IDs.csv"
    GetSetIDs(idsFileName)


if __name__ == "__main__":
    main()
