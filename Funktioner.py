FILEPATH = "mainfilen.txt" #Definierar en konstant variabel som innehåller sökvägen till filen.

def hämta_listan(filepath="mainfilen.txt"):
    """Denna funktion öppnar filen mainfilen.txt, 
    läser innehållet och returnerar det som en lista.
    """
    with open(filepath, "r") as file_local:
        listan_local = file_local.readlines()
    return listan_local

def write_listan(listan_arg, filepath="mainfilen.txt"):
    """Denna funktion tar en lista som argument och skriver den till filen mainfilen.txt,
    där varje element i listan blir en rad i filen."""
    with open(filepath, "w") as file:
        file.writelines(listan_arg)

if __name__ == "__main__": #Detta gör att koden nedanför bara körs när du kör den här filen direkt, och inte när du importerar den i en annan fil.
    print("Tjena från funktioner")
    print(hämta_listan()) #Testar att hämta listan från filen och skriva ut den.
