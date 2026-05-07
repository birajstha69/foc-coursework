import datetime

def generate_sales_invoice(cart, total):
    name = input("Enter customer name: ")
    date = datetime.datetime.now()

    filename = f"sales_{name}_{date.strftime('%H%M%S')}.txt"

    with open(filename, "w") as f:
        f.write("==== MEDSTORE INVOICE ====\n")
        f.write(f"Customer: {name}\n")
        f.write(f"Date: {date}\n\n")

        for item in cart:
            f.write(f"{item['name']} ({item['brand']})\n")
            f.write(f"Qty: {item['qty']} (Strips: {item['strips']}, Tablets: {item['tablets']})\n")
            f.write(f"Discount: Rs.{item['discount']}\n")
            f.write(f"Total: Rs.{item['total']}\n\n")

        f.write(f"Final Total: Rs.{total}\n")

    print("Invoice generated:", filename)


def generate_restock_invoice(supplier, items, total):
    import datetime
    date = datetime.datetime.now()

    filename = f"restock_{supplier}_{date.strftime('%H%M%S')}.txt"

    with open(filename, "w") as f:
        f.write("==== RESTOCK INVOICE ====\n")
        f.write(f"Supplier: {supplier}\n")
        f.write(f"Date: {date}\n\n")

        for name, brand, qty, cost in items:
            f.write(f"{name} ({brand}) - Qty: {qty} - Cost: Rs.{cost}\n")

        f.write(f"\nTotal Cost: Rs.{total}")

    print("Restock invoice generated:", filename)
    