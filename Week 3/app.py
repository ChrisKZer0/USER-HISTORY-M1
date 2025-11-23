#

from services import(
    add_product,
    show_inventory,
    search_product,
    update_product,
    delete_product,
    calculate_statistics)

from archive import save_inventory, load_inventory

inventory=[]

option=""

while option !="9":
    print("\n" + "-" * 30)
    print("Inventory menu".upper().center(30))
    print("-" * 30)

    print("1. Add product")
    print("2. Show inventory")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Statistics")
    print("7. Save inventory")
    print("8. Load inventory")
    print("9. Exit")
    print("-" * 30)

    option=input("\nChoose an option: ")

    if option=="1":
        add_product(inventory)

    elif option=="2":
        show_inventory(inventory)

    elif option=="3":
        name=input("Product name to search: ")
        product=search_product(inventory, name)

        if product:
            print("\033[32mProduct found!\033[0m")
        else:
            print("\033[31mProduct not found!\033[0m")

    elif option=="4":
        update_product(inventory)

    elif option=="5":
        delete_product(inventory)

    elif option=="6":
        stats=calculate_statistics(inventory)
        print("\n" + "-" * 30)
        print("Statistics".upper().center(30))
        print("-" * 30)

        print(f"Total units: \033[32m{stats['total_units']}\033[0m")
        print(f"Total value: \033[32m{stats['total_values']}\033[0m")
        print(f"Most expensive product: \033[32m{stats['most_expensive']}\033[0m")
        print(f"Products with highest stock: \033[32m{stats['highest_stock']}\033[0m")
        print("-" * 30)
        
    elif option=="7":
        save_inventory(inventory)

    elif option=="8":
        print("\nHow do you want to load the inventory?")
        print("1. Overwrite")
        print("2. Merge")

        load_option=input("Choose if 1 or 2: ")

        if load_option=="1":
           inventory, skipped=load_inventory("Overwrite")
        elif load_option=="2":
           loaded, skipped=load_inventory("Merge")
           inventory.extend(loaded)
        else:
            print("\033[32mInvalid option\033[0m")
            continue

        print("Skipped rows: {skipped}")

    #Here just the last option that is exit    
    elif option=="9":
        print("\033[32mExit\033[0m")

    else:
        print("\033[32mInvalid. Try again.\033[0m")