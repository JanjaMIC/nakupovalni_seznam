listek = []

while True:
    x = raw_input("Ali zelis dodati kaksen izdelek na seznam? ")


    if x == "ja":
        y = raw_input("Napisi prosim ime izdelka: ")
        listek.append(y)

    if x == "ne":
        print "Hvala in nasvidenje."
        break

    elif x != "ja" and x != "ne":
        print "Napaka. Odgovori ja ali ne."

print "V nakupovalnem seznamu so: ", listek

