#In this space, the idea is to welcome you.
print("Welcome to the inventory")

#We request the main data with variables.
#Here I put the information about the product and price
name=str(input("name of the product: "))
price=float(input("price of the product in COP: "))

#While serves as a guide becouse I don't knowwhich product
while price <20000:
    print("Enter a valid value")
    price=float(input("put the valid value: "))
   
quantity=int(input("quantity of product: "))

total_price= price*quantity 
print("\n product description".upper()+"\n")

print(f"| {'Product name':15}| {name:<10}|\
      \n| {'Price':15}| {price:<10}|\
      \n| {'Quantity':15}| {quantity:<10}|\
      \n| {'Total price':15}| {total_price:<10}|")