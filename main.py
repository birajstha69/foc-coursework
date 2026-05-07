from file_handler import read_file, write_file
from display import show_medicines
from calculation import sell_medicine, restock_medicine
from invoice import generate_sales_invoice, generate_restock_invoice

def main():
    filename = "medicines.txt"
    medicines = read_file(filename)

    while True:
        print("\n1. Display Medicines")
        print("2. Sell Medicine")
        print("3. Restock Medicine")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_medicines(medicines)

        elif choice == "2":
            cart, total = sell_medicine(medicines)
            generate_sales_invoice(cart, total)
            write_file(filename, medicines)

        elif choice == "3":
            supplier, items, total = restock_medicine(medicines)
            generate_restock_invoice(supplier, items, total)
            write_file(filename, medicines)

        elif choice == "4":
            break

        else:
            print("Invalid choice!")

main()
