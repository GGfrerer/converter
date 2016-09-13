print "Hallo. Ich kann Kilometer in Meilen konvertieren."

frage = 0
while frage != "N":
    print
    eingabekilo = int(raw_input("Bitte geben Sie den Kilometer-Wert ein: "))

    ausgabemeilen = eingabekilo * 0.621371

    print str(eingabekilo) + " Kilometer sind genau: " + str(ausgabemeilen) + " Meilen."
    print

    frage = raw_input("Wollen Sie noch einen Wert konvertieren? (J/N)")

    if frage == "N":
        print "Danke und auf Wiedersehen!"
        break







