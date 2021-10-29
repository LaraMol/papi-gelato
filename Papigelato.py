print ('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')

def AantBolletjes():
    while True:
        bolletjes = int(input ("Hoeveel bolletjes wilt u?: "))
        if bolletjes > 8 or bolletjes <= 0:
            print("Zulke grote bakken hebben we niet!")
        else:
            return bolletjes


bolletjes = AantBolletjes()
if bolletjes <= 3:
    while True:
        onderkant = input (f"Wilt u deze {bolletjes} bolletje(s) in een (A)hoorntje of (B)bakje?: ")
        if onderkant.lower() == 'b':
            print('Bakje')
            break
        elif onderkant.lower() == 'a': 
            print ('Hoorntje')
            break
        else:
            print("Sorry, dat snap ik niet...")
elif bolletjes >= 4 and bolletjes <= 8:
    print (f"Hier is uw {bolletjes} bolletjes")

def meerBestellen():
    bestellen = input ("Wilt u nog meer bestellen? Y/N: ")
    if bestellen == "Y" or bestellen == "y":
        print ("Met genoegen")
        AantBolletjes()

    elif bestellen == "N" or bestellen == "n":
        print ("Bedankt ent tot ziens!")
    else:
        print ("Sorry, Dat snap ik niet")
        meerBestellen()




meerBestellen()