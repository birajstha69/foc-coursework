# open the file and read the data
file = open("medicines.txt", "r")
data = file.readlines()
file.close()

# create empty list to store medicines
medicines = []

# process each line
for line in data:
    line = line.strip()  # remove newline
    parts = line.split(",")  # split by commaTable of Figures

    # stores it in dictionary
    medicine = {
        "name": parts[0],
        "brand": parts[1],
        "stock": int(parts[2]),
        "price_tablet": int(parts[3]),
        "price_strip": int(parts[4]),
        "tablets_per_strip": int(parts[5])
    }

    medicines.append(medicine)

# display all the details of medicines
print("\n--- Available Medicines ---\n")

for m in medicines:
    print("Medicine Name :", m["name"])
    print("Brand         :", m["brand"])
    print("Stock         :", m["stock"], "tablets")
    print("Price/Tablet  : Rs.", m["price_tablet"])
    print("Price/Strip   : Rs.", m["price_strip"])
    print("Tablets/Strip :", m["tablets_per_strip"])
    print("----------------------------")