#In this file the idea is practice functions for the inventory system.

#I need to add a function for a new product, I put the product and the price
def add_product(inventory):
    print("-" * 30)
    print("Add product".upper().center(30))
    print("-" * 30)

    name=input("Product name: ")
    price=input("Price in COP: ")

#For use decimals, I reepalce with a function
    #while price.replace(".", "", 1).isdigit()==False:
        #print("\033[31mPlease put just numbers\033[0m")
        #price=input("Price in COP: ")

    while not price.replace(".", "", 1).isdigit():
        print("\033[31mPlease put just numbers\033[0m")
        price=input("Price in COP: ")

#I validate the price and quantity
    price=float(price)

    quantity=input("Quantity: ")

    #while quantity.isdigit()==False:
        #print("\033[31mPut just numbers\033[0m")
        #quantity=input("Quantity: ")

    while not quantity.isdigit():
        print("\033[31mPut just numbers\033[0m")
        quantity=input("Quantity: ")

    quantity=int(quantity)

    #Here I create the dictionary
    product={"name":name,
             "price":price,
             "quantity":quantity}
    
    #I save the product inside the inventory list
    inventory.append(product)

    print("\033[32mProduct added!\033[0m")

#Here show the inventory
def show_inventory(inventory):
    print("-" * 60)
    print("Inventory list".upper().center(30))
    print("-" * 60)

    if len(inventory)==0:
        print("\033[31mThe inventory is empty.\033[0m")
        return
    
    for product in inventory:
            print(f"| Product: {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}") 
    
    print("-" * 60)
   
#Here I search the product
def search_product(inventory, search_name):
 
     for product in inventory:
        if product["name"].lower()== search_name.lower():
            return product
        
     return None

def update_product(inventory):
    print("-" * 30)
    print("Update product".upper().center(30))
    print("-" * 30)

    name=input("Name of the product name to update: ")
    product=search_product(inventory, name)

    if product is None:
        print("\033[31mProduct not found.\033[0m")
        return
    
    new_price=input("New price in COP: ")

    #Here put the new price
    if new_price != "":

        while not new_price.replace(".", "", 1).isdigit():
            print("\033[31mPlease put just numbers\033[0m")
            new_price=input("New price in COP: ")
        product["price"]=float(new_price)

    #Here the new quantity
    new_quantity=input("New quantity: ")

    if new_quantity !="":
    
        while not new_quantity.isdigit():
            print("\033[31mPlease put just numbers\033[0m")
            new_quantity=input("New quantity: ")
        product["quantity"]=int(new_quantity)

    print("\033[32mProduct updated!\033[0m")

#Here I can delete the product
def delete_product(inventory):
    #Is important ask what product I want to delete
    name=input("Name of the product that you want to delete: ")
    #With this fuction I search the product
    product=search_product(inventory, name)

    #Here if the product is not found
    if product is None:
        print("\033[31mProduct not found.\033[0m")
        return
    
    #If when I delete the product
    inventory.remove(product)
    print("\033[32mProduct deleted!\033[0m")

#The statistics of the inventory
def calculate_statistics(inventory):
    if len (inventory)==0:
        print("\033[31mNo statistics available. Inventory is empty.\033[0m")
        return
    
    #Formula to calculate the total value and total units
    total_value=0
    total_units=0

    #Counting the total
    for product in inventory:
        total_value+=product["price"]*product["quantity"]
        total_units+=product["quantity"]

    most_expensive=max(inventory, key=lambda x: x["price"])
    highest_expensive=max(inventory, key=lambda x: x["quantity"])

    #Finally the total account of products
    #total_products=len(inventory)
    print("\n" + "-" * 30)
    print("Statistics".upper().center(30))
    print("-" * 30)

    #The results
    print(f"Total inventory value: \033[32m{total_value}\033[0m")
    print(f"Total units in stock: \033[32m{total_units}\033[0m")
    print(f"Most expensive product: \033[32m{most_expensive}\033[0m")
    print(f"Product with highest stock: \033[32m{highest_expensive}\033[0m")

    print("-" * 30)
