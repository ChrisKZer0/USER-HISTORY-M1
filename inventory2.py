#Here I just put the inventory and the menu process

inventory=[]

#I start with a function
def add_product():

    #I ask for the product name and price
    name=input("Product name: ")
    price=input ("Price in COP: ")

    #For reflect the price I use while and try to define decimals
    while price.replace(".", " ").isdigit()==False:
        print("\033[31mInvalid price\033[0m")
        price=input("Enter product price: ")

    price=float(price)
    quantity=input("Quantity: ")

    #Here I ask about the quantity
    while quantity.isdigit()==False:
        print("\033[31mPlease put just numbers\033[0m")
        quantity=input("Quantity: ")

    quantity=int(quantity)

    #I create the dictoanary for the products
    product={
        "name": name,
        "price": price,
        "quantity": quantity
    }

    #I save here in a list
    inventory.append(product)
    print("\033[32mProduct added successfully!\033[0m")

#Now the idea is show the products in the inventory
def show_inventory():

    if len(inventory)==0:
        print("\033[31mThe inventory is empty.\033[0m")
    else:
        print("\n" + "-" * 50)
        print("\nInventory list".upper().center(35))
        print("-" * 50)

        # I use a for loop to print each product
        for product in inventory:
            print(f"Product: {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}")
        

#Here I calculating basic stadistics about the products
def calculate_total_products():
        #If the inventory is empty, I can't calculating anything
        if len(inventory)==0:
             print("\033[31mNo statistics available.\033[0m")
        else:
             total_value=0

             for product in inventory:
                  total_value +=product["price"]*product["quantity"]

             total_products=len(inventory)

             print("\n" + "-" * 30)
             print("Statistics".upper().center(30))
             print("-" * 30)

             print(f"Total inventory value: \033[32m{total_value}\033[0m")
             print(f"Total number of product: \033[32m{total_products}\033[0m")

#Here I start the meni with a variable thtat is not "4"
option=""

#I need to check the condition manually
while option !="4":
    #I print the menu
    print("\n" + "-" * 50)
    print("Inventory".upper().center(35))
    print("-" * 50)

    print("1. Add product")
    print("2. Show inventory")
    print("3. Calculate statistics")
    print("4. Exit")
    print("-" * 50)

    #I ask the user for an option
    option=input("Select an option: ")

    #Check the option
    if option=="1":
        add_product()
    elif option=="2":
        show_inventory()
    elif option=="3":
        calculate_total_products()
    elif option=="4":
        print("Exiting...")
    else:
        #If the user enter an invalid option
        print("\033[31mInvalid option. Please try again.\033[0m")
