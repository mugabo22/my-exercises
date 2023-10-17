#Implementing Dictionaries in python
import time
my_dict={}
def add_item():
        item_name = input("Enter the name of the item: ")
        item_price = float(input("Enter the price of the item: "))
        print(f"Added {item_name} with a price of ${item_price}.")
        my_dict.update({item_name:item_price})
def view_items():
    print("Below Are the items in the Dict..")
    print(my_dict)
   
def search_item():
        try:
                item=input("Which item are you searching?? :")
                if item in my_dict:
                        print(f'Your search item is at ${my_dict[item]}')
                else:
                        print("Item not in dictionary")
        except:
                print("Please make a good selection of items")               
def main():
    item_dictionary = {}

    while True:
        print("\nMenu:")
        print("1. Add an item")
        print("2. View items")
        print("3. Search for an item")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_item()
            continue
        elif choice == '2':
            view_items()
            time.sleep(1)
        elif choice == '3':
            search_item()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 
    
    