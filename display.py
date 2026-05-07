def show_medicines(medicines):
    print("\nAvailable Medicines:\n")
    for i, m in enumerate(medicines):
        print(f"{i}. {m['name']} ({m['brand']}) - Stock: {m['stock']}")