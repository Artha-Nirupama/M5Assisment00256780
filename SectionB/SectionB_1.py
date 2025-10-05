inventory_list = []

class mainFuntionBlock:
    @staticmethod
    def add_Function(item_Name):
        """Adds an item to the global inventory list"""
        inventory_list.append(item_Name)
        print(f"'{item_Name}' has been added to the inventory.")

    @staticmethod
    def search_Function(item_Name):
        """Searches for an item in the inventory list"""
        found = False
        for x in inventory_list:
            if x == item_Name:
                found = True
                break
        
        if found:
            print(f"{item_Name} is already in the Inventory list! 😁")
        else:
            print(f"{item_Name} is new to the Inventory list! 😲")

def main():
    mainFuntionBlock.add_Function("Laptop")
    mainFuntionBlock.add_Function("Mouse")
    mainFuntionBlock.add_Function("Keyboard")

    print("\nCurrent Inventory:", inventory_list)
    
    print("\n--- Search Results ---")
    mainFuntionBlock.search_Function("Mouse")      
    mainFuntionBlock.search_Function("Monitor")    

if __name__ == "__main__":
    main()
