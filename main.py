from pokemontcgsdk import RestClient
import TcgPKMN as TP
import config

def SetupSetCSV(setID, setCSVFile):
    csvColumn = ["ID", "Set Number", "Card Name", "Rarity", "Artist",
                 "Normal Price($)", "Holo Foil Price ($)", "Reverse Holo Price ($)", 
                 "First Edition Holo Price ($)", "First Edition Normal Price ($)",
                 "Updated At (YYYY/MM/DD)"]

    TP.InitPokeCSV(setCSVFile, csvColumn)
    infoList = TP.GetCardsInSet(setID)
    TP.AppendPokeCSV(infoList)


def main():
    pokeAPIkey = config.getPokeAPIkey()
    RestClient.configure(pokeAPIkey)

    stdCSVFile = "CrownZenith - STD Set.csv"
    stdId = "swsh12pt5"


if __name__ == "__main__":
    main()
