lista={
    "piekarnia":["chleb","bułki","pączki", "ciasto", "pączki"],
    "warzywniak":["marchew","seler","rukola","pomidor", "ogórek"]
}
i=0
for sklep in lista.keys():
    for produkt in lista.get(sklep):
        i=i+1
        print(f"Idę do {sklep.upper()} i kupuję tam {produkt.upper()}")

print(f"W sumie kupuję: {i} produktów")
