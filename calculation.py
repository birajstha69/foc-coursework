.   def sell_medicine(medicines):
    cart = []
    total_bill = 0

    while True:
        try:
            # Input Validation for Medicine Index
            index = int(input("\nEnter medicine index: "))
            if index < 0 or index >= len(medicines):
                print("Error: Invalid index. Please choose a valid medicine.")
                continue
        except ValueError:
            print("Error: Please enter a valid number for the index.")
            continue

        m = medicines[index]
        tablets_per_strip = m["tablets_per_strip"]

        # Ask user for the Unit Type (Tablet or Strip)
        unit_type = input("Sell by tablet or strip? (t/s): ").strip().lower()
        if unit_type not in ['t', 's']:
            print("Error: Invalid choice. Please enter 't' for tablet or 's' for strip.")
            continue

        try:
            # Input Validation for Quantity
            qty_input = int(input(f"Enter quantity in {'tablets' if unit_type == 't' else 'strips'}: "))
            if qty_input <= 0:
                print("Error: Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Error: Please enter a valid number for quantity.")
            continue

        # Convert everything to tablets to check stock accurately
        if unit_type == "s":
            total_tablets_requested = qty_input * tablets_per_strip
            strips = qty_input
            remaining_tablets = 0
        else:
            total_tablets_requested = qty_input
            strips = total_tablets_requested // tablets_per_strip
            remaining_tablets = total_tablets_requested % tablets_per_strip

        # Check if enough stock exists
        if total_tablets_requested > m["stock"]:
            print(f"Not enough stock! Available stock: {m['stock']} tablets.")
            continue

        # Calculate prices exactly as the document specifies
        strip_price = strips * m["price_strip"]
        tablet_price = remaining_tablets * m["price_tablet"]
        total_before_discount = strip_price + tablet_price

        # Apply 5% discount if 2 or more strips are purchased
        discount = 0
        if strips >= 2:
            discount = total_before_discount * 0.05

        final_total = total_before_discount - discount

        # Update real-time stock
        m["stock"] -= total_tablets_requested

        # Add item to cart for the invoice
        cart.append({
            "name": m["name"],
            "brand": m["brand"],
            "unit": "Strip" if unit_type == "s" else "Tablet",
            "qty": total_tablets_requested,
            "strips": strips,
            "tablets": remaining_tablets,
            "total": final_total,
            "discount": discount
        })

        total_bill += final_total
        print(f"Added to cart. Total for this item: Rs.{final_total:.2f}")

        more = input("\nAdd more items to this bill? (y/n): ").strip().lower()
        if more != "y":
            break

    return cart, total_bill


def restock_medicine(medicines):
    supplier = input("Enter supplier name: ").strip()
    total_cost = 0
    items = []

    while True:
        try:
            # Input Validation for Medicine Index
            index = int(input("\nEnter medicine index: "))
            if index < 0 or index >= len(medicines):
                print("Error: Invalid index. Please choose a valid medicine.")
                continue
        except ValueError:
            print("Error: Please enter a valid number for the index.")
            continue

        try:
            # Input Validation for Restock Quantity
            qty = int(input("Enter quantity to add (in tablets): "))
            if qty <= 0:
                print("Error: Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Error: Please enter a valid number for quantity.")
            continue

        m = medicines[index]

        # Calculate restocking cost
        cost = qty * m["price_tablet"]
        m["stock"] += qty

        # Append including medicine name and brand for complete invoice generation
        items.append((m["name"], m["brand"], qty, cost))
        total_cost += cost

        print(f"Restocked {m['name']} successfully.")

        more = input("\nAdd more stock to this invoice? (y/n): ").strip().lower()
        if more != "y":
            break

    return supplier, items, total_cost
