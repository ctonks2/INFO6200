"""Python application with text-based options for user selection. It will give the user the ability to add a receipt, add line items from the receipt
and add a store location. The application will allow the user to list all line items, receipts and store locations. 

Step 1: Display menu of options for user to select.
Step 2: If user selects to add a line item, prompt for line item details (name, price, discount_price, productUPC, store_id, receipt_id(FK)).
        If user selects to add a receipt, prompt for receipt details (date, total, total_discount_save, store_id).
        If user selects to add a store location, prompt for store details (name, address, city, state, zip).
        If user selects to list ask if they want to list line items, receipts or store locations and display accordingly.
Step 3: Loop back to menu after each action until user chooses to exit. If user selects to exit, terminate the application.
"""
## Welcome message
print("Welcome to the Spend Analyzer!")

## Initialize Lists for data with fake data
##TODO: establish foreign key relationships between tables
store_locations = [
    {"name": "Walmart", "address": "123 Main St", "city": "Springfield", "state": "IL", "zip": "62701"},
    {"name": "Target", "address": "456 Oak Ave", "city": "Chicago", "state": "IL", "zip": "60601"},
    {"name": "Costco", "address": "789 Elm Rd", "city": "Evanston", "state": "IL", "zip": "60201"}
]
receipts = [
    {"date": "2024-01-15", "total": 2.99, "total_discount_save": 1, "store_id": "1"},
    {"date": "2024-01-20", "total": 2.49, "total_discount_save": 0, "store_id": "2"}, 
    {"date": "2024-01-22", "total": 7.98, "total_discount_save": 1.50, "store_id": "3"}
]
line_items = [
    {"name": "Milk", "price": 3.99, "discount_price": 2.99, "productUPC": "1234567890", "store_id": "12321", "receipt_id": "1"},
    {"name": "Bread", "price": 2.49, "discount_price": 2.49,"productUPC": "0987654321", "store_id": "242521", "receipt_id": "2"},
    {"name": "Eggs", "price": 4.99, "discount_price": 3.99, "productUPC": "1122334455", "store_id": "1424", "receipt_id": "3"},
    {"name": "Cheese", "price": 5.49, "discount_price": 4.99, "productUPC": "5566778899", "store_id": "12333", "receipt_id": "3"}
]

## Display menu function
def display_menu():
    print("\nPlease choose an option:")
    print("1. Add a line item")
    print("2. Add a receipt")
    print("3. Add a store location")
    print("4. List Data")
    print("5. Exit")

## Add line item to dictionary with a name, price, productUPC, store_id. Values cannot be empty and an error occurs if it is.
## TODO: add foreigh  key constraints for tables to associate line items with receipts and store locations
def add_line_item():
    print("\nAdding a new line item:")
    
    name = input("Enter item name: ").strip()
    if not name:
        print("Item name cannot be empty.")
        return
    
    try:
        price = float(input("Enter price: ").strip())
    except ValueError:
        print("Invalid price. Please enter a valid number.")
        return
    try:
        discount_price = float(input("Enter discount price: ").strip())
    except ValueError:
        print("Invalid price. Please enter a valid number.")
        return    
    
    product_upc = input("Enter product UPC: ").strip()
    if not product_upc:
        print("Product UPC cannot be empty.")
        return
    
    store_id = input("Enter store ID: ").strip()
    if not store_id:
        print("Store ID cannot be empty.")
        return
    
    receipt_id = input("Enter receipt ID: ").strip()
    if not receipt_id:
        print("Receipt ID cannot be empty.")
        return
    
    line_item = {
        "name": name,
        "price": price,
        "discount_price": discount_price,
        "productUPC": product_upc,
        "store_id": store_id,
        "receipt_id": receipt_id
    }
    line_items.append(line_item)
    print(f"Line item '{name}' has been added successfully.")

## Add receipt to dictionary with date, total, total_discount_save, store_id. Values cannot be empty and an error occurs if it is.   
## TODO: add foreign key constraint for store_id to associate receipt with store location
# TODO: calculate total_discount_save based on line items associated with receipt 
def add_receipt():
    print("\nAdding a new receipt:")
    
    date = input("Enter receipt date (YYYY-MM-DD): ").strip()
    if not date:
        print("Receipt date cannot be empty.")
        return
    
    try:
        total = float(input("Enter total amount: ").strip())
    except ValueError:
        print("Invalid total amount. Please enter a valid number.")
        return
    
    try:
        total_discount_save = float(input("Enter total discount save: ").strip())
    except ValueError:
        print("Invalid discount save. Please enter a valid number.")
        return

    store_id = input("Enter store ID: ").strip()
    if not store_id:
        print("Store ID cannot be empty.")
        return

    receipt = {
        "date": date,
        "total": total,
        "total_discount_save": total_discount_save,
        "store_id": store_id
    }
    receipts.append(receipt)
    print(f"Receipt for {date} has been added successfully.")

## Add store location to dictionary with name, address, city, state, zip. Values cannot be empty and an error occurs if it is.
def add_store_location():
    print("\nAdding a new store location:")
    
    name = input("Enter store name: ").strip()
    if not name:
        print("Store name cannot be empty.")
        return
    
    address = input("Enter store address: ").strip()
    if not address:
        print("Store address cannot be empty.")
        return
    
    city = input("Enter store city: ").strip()
    if not city:
        print("Store city cannot be empty.")
        return
    
    state = input("Enter store state: ").strip()
    if not state:
        print("Store state cannot be empty.")
        return
    
    zip_code = input("Enter store zip code: ").strip()
    if not zip_code:
        print("Store zip code cannot be empty.")
        return
    
    store = {
        "name": name,
        "address": address,
        "city": city,
        "state": state,
        "zip": zip_code
    }
    store_locations.append(store)
    print(f"Store location '{name}' has been added successfully.")

## List data function to list line items, receipts or store locations
## TODO: add report building here where background automates calculations and summaries for user.
def list_data():
    print("\nWhat would you like to list?")
    print("1. Line Items")
    print("2. Receipts")
    print("3. Store Locations")
    choice = input("Enter your choice (1-3): ").strip()
    
    if choice == '1':
        if not line_items:
            print("No line items available.")
        else:
            print("\nLine Items:")
            for item in line_items:
                print(item)
    elif choice == '2':
        if not receipts:
            print("No receipts available.")
        else:
            print("\nReceipts:")
            for receipt in receipts:
                print(receipt)
    elif choice == '3':
        if not store_locations:
            print("No store locations available.")
        else:
            print("\nStore Locations:")
            for store in store_locations:
                print(store)
    else:
        print("Invalid choice. Please select a valid option.")

## Main loop
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_line_item()
        elif choice == '2':
            add_receipt()
        elif choice == '3':
            add_store_location()
        elif choice == '4':
            list_data()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main() 
