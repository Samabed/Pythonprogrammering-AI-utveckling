import random

def få_datorns_val():
    # Funktion för att slumpa datorns val av sten, sax eller påse
    return random.choice(["sten", "sax", "påse"])

def avgöra_vinnare(spelarens_val, datorns_val):
    # Funktion för att avgöra vinnaren baserat på spelarens val och datorns val
    if spelarens_val == datorns_val:
        return "Det blev oavgjort!"
    elif (spelarens_val == "sten" and datorns_val == "sax") or \
         (spelarens_val == "sax" and datorns_val == "påse") or \
         (spelarens_val == "påse" and datorns_val == "sten"):
        return "Du vinner!"
    else:
        return "Datorn vinner!"

def sten_sax_påse():
    # Huvudfunktionen för Sten-sax-påse-spelet
    print("Välkommen till Sten-sax-påse!")
    print("Du spelar mot datorn.")

    while True:
        spelarens_val = input("Välj sten, sax eller påse (eller 'sluta' för att avsluta spelet): ").lower()
        if spelarens_val == "sluta":
            print("Tack för att du spelade!")
            break
        elif spelarens_val not in ["sten", "sax", "påse"]:
            print("Ogiltigt val. Försök igen.")
            continue

        datorns_val = få_datorns_val()
        print("Datorn valde:", datorns_val)

        vinnare = avgöra_vinnare(spelarens_val, datorns_val)
        print(vinnare)

        if vinnare == "Du vinner!" or vinnare == "Datorn vinner!":
            break

if __name__ == "__main__":
    sten_sax_påse()


