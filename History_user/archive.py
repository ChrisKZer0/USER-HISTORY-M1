#Here I can sae and load the inventory from a CSV file
#the function that I use is csv
import csv

#First the idea is save the inventory
def save_inventory(inventory, filename="inventory.csv"):

    try:
        with open(filename, mode="w", newline='', encoding='utf-8') as file:
            writer=csv.writer(file)
            writer.writerow(["name", "price", "quantity"])
            
            for product in inventory:
                writer.writerow([product["name"], product["price"], product["quantity"]])

        print("\033[32mInventory saved\033[0m")
            
    except Exception as e:
    #With this the app can to work
        print("\033[31mError saving CSV file\033[0m", str(e))

#Now the idea is load the inventory
def load_inventory(option, filename="inventory.csv"):
    #I use this parameters for open and read the CSV file
    loaded_inventory=[]
    skipped_rows=0

    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader= csv.reader(file)
            next(reader, None)

            #The validation for every each row
            for row in reader:
                if len(row)!=3:
                    skipped_rows +=1
                    continue
            
                name, price, quantity=row

                #The validation for price and quantity but numeric format
                if not price.replace(".", "", 1).isdigit() or not quantity.isdigit():
                    skipped_rows +=1
                    continue

                loaded_inventory.append({
                    "name": name,
                    "price": float(price),
                    "quantity": int(quantity)            
                    })
        
        #Now the parameters for the other part of each option have progress
        if option=="overwrite":
            print("Inventory overwritten with CSV data")
            return loaded_inventory, skipped_rows
        
        elif option=="merge":
            print("CSV data merged with current inventory")
            return loaded_inventory, skipped_rows
        
        else:
            print("\033[31mInvalid loading option\033[0m")
            return [], skipped_rows
        
    except FileNotFoundError:
        print("\033[31mCSV file not found\033[0m")
        return [], skipped_rows
    
    except Exception as e:
        print("\033[31mError loading CSV file\033[0m", str(e))
        return [], skipped_rows
