#In this space, the idea is to welcome you.
print("Welcome to the inventory".upper().center(50))

#I request the main data with variables.
#Here I put the information about the product and price
name=input("name of the product: ")
price=input("price of the product in COP: ")

#While serves as a guide becouse I don't knowwhich product
while price.replace (".","").isdigit()==False:
    print("\033[31mPlease put just numbers\033[0m")
    price=input("Put tha price again: ")

price=float(price)
quantity=input("Enter the quantity: ")

#Here I validate the quantity 
while quantity.isdigit()==False:
    print("\033[31mPlease put just number\033[0m")
    quantity=input("Enter the quantity again: ")

quantity=int(quantity)

total=price*quantity

#Summary of the product
print("\n" + "-" * 30)
print("Product description".upper().center(30))
print("-" * 30)

print(f"| {'Product':15}| {name:<10}|\
      \n| {'Price':15}| {price:<10}|\
      \n| {'Quantity':15}| {quantity:<10}|\
      \n| {'Total price':15}| \033[32m{total:<10}\033[0m|\n")

