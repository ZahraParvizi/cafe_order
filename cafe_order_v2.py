# 🍵 Cafe Order System - Python Practice Project
# Define menu with item prices
menu = {
    "coffee": 30000,
    "tea": 15000,
    "chocolate cake": 40000,
    "hot chocolate": 25000,
    "iced latte": 35000,
    "cheesecake": 45000
}
# Show the menu
def show_menu(menu):
    print("\n Our cafe menu 🍵🍩\n")
    for name,price in menu.items():
        print(f" {name:<15}: {price}")
        
# Take orders from user        
def order(menu):
    print("\nWhat do you want?\n(Write 'Done' to finish)\n")
    orders_list=[]
    while True:
        item=input("➤ ").strip()
        if item.lower() == "done":
            break
        
        # Match the entered item with the menu keys (case-insensitive)
        match=None
        for key in menu:
            if key.lower()==item.lower():
                match=key
                break
            
        if match:
            orders_list.append(match)
            print(f"{match} added to the list ✅")
        else:
            print("This item is not on the menu ❌")
    return orders_list

# Display ordered items and calculate total price             
def View_orders(orders, menu):
    total_price=0
    for item in orders:
        print(f"{item}: {menu[item]}")
        total_price+=menu[item]
    return total_price

def remove(orders,menu):
    while True:
        choice =input("\nDo you want to remove an item from your order list? (yes/no)").strip().lower()
        if choice.lower().strip() == "yes":
            iteme_remove=input("\nEnter the name of the item you want to remove : ")
            
            match= None
            for item in orders:
                if item.lower().strip()==iteme_remove:
                    match=item
                    break
            if match:
                orders.remove(match)
                print(f"{match} removed from your order.")
            else:
                print("this order is not in your order list")
        elif choice == "no":
            print("👍 Okay! No changes made to your order list.")
            break
        else:
            print("❗ Please type 'yes' or 'no'.")
   
    

show_menu(menu)
orders=order(menu)
print("\n🧺 Your order list:")    
final_price=View_orders(orders, menu)
print(f"\n💰 Total price: {final_price}")

while True:
    print("\nWhat do you want to do now?")
    print("1)  Place order")
    print("2)  Add more items")
    print("3)  Remove an item")
    print("4)  Cancel and exit")

    answer = input("Enter a number (1-4): ").strip()
    
    if answer=="1":
        print("\n🧾 Final order summary:")
        final_price=View_orders(orders, menu)
        print(f"💰 Total price: {final_price}")
        print("Your order was successfully registered.Thank you! ☕")
        break
    
    elif answer=="2":
        show_menu(menu)
        more_orders=order(menu)
        orders.extend(more_orders)
        print("\n📝update order list:")
        final_price=View_orders(orders, menu)
        print(f"\nUpdated total price: {final_price}")
        
    elif answer=="3":
        remove(orders, menu)
        print("\n📝update order list:")
        final_price=View_orders(orders, menu)
        print(f"\nUpdated total price: {final_price}")
    elif answer=="4":
        print("🚫 Order canceled. See you next time!")
        break
    else:
         print("❗ Invalid choice. Please enter a number between 1 and 4.") 
         
