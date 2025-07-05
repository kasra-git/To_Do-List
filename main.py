from Modouls import *
from colorama import Fore

app = ToDoList()
app.clear_screen()
print("Enter Your Chooise : ")
print("Add")
print("Remove")
print("Find")
print("Exit")
choise = input("Choise ?")
while (choise != "Exit"):
    match (choise):
        case "Add":
            app.clear_screen()
            key = input("Key : ")
            value = input("Value : ")
            app.add_item(key=key,value=value)
        case "Remove":
            app.clear_screen()
            key = input("Key :")
            app.remove_item(key=key)
        case "Find":
            app.clear_screen()
            key = input("Key :")
            app.clear_screen()
            print(Fore.RED + app.find_item(key=key) + Fore.WHITE)
        case "Exit":
            exit()
        case _:
            print("-------------------- Writed By Ego -----------------------------")

    print("Enter Your Chooise : ")
    print("Add")
    print("Remove")
    print("Find")
    print("Exit")
    choise = input("Choise ?")