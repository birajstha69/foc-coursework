def read_file(filename):
    medicines = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            medicines.append({
                "name": parts[0],
                "brand": parts[1],
                "stock": int(parts[2]),
                "price_tablet": int(parts[3]),
                "price_strip": int(parts[4]),
                "tablets_per_strip": int(parts[5])
            })
    return medicines


def write_file(filename, medicines):
    with open(filename, "w") as file:
        for m in medicines:
            line = f"{m['name']},{m['brand']},{m['stock']},{m['price_tablet']},{m['price_strip']},{m['tablets_per_strip']}\n"
            file.write(line)