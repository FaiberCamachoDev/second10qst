# P1. Listas — Gestión de nombres
# Crear una lista con al menos cinco nombres. El usuario ingresa una opción y se ejecuta solo una acción:

# Agregar un nombre nuevo que no se encuentre ya en la lista.
# Mostrar todos los nombres.
# Cambiar un nombre existente por otro.
# Eliminar un nombre por su posición.
# Debe validarse que la posición sea correcta y que no existan duplicados.

names_list = ["Daniel", "Ulith", "Isabel", "Julian", "Veronica"]

print("\n--- Options ---\n1. Add name to the list\n2. Show all the names\n3. Change name\n4. Delete name from the list")

while True:

    choice = input("What do you wanna do? (1-4): ").strip()
    
    if not choice:
        print("The choice cannot be empty\n")
        continue
    
    if not choice.isdigit():
        print("The choice has to be a number")
        continue
    
    if len(choice) != 1:
        print("The choice contains only one number")
        continue
    
    match choice:
    
        case "1":
            new_name = input("Which name you wanna add?: ").strip()
        
            if new_name in names_list:
                print("The name is already in the list, try with other")
                continue

            else:
                names_list.append(new_name)
                print("The name was add")
                break

        case "2":
            print(names_list)
            break

        case "3":
            change_name = input("Which name you wanna change?: ").strip()
        
            if not change_name in names_list:
                print("The name is not in the list, select options 2 and to see the names that are in the list or option 1 to add it")
                continue
            
            else:
                new_name = input("Enter me the new name: ")
                index = names_list.index(change_name)
                # name_list[index] = new_name
                names_list.remove(change_name)
                names_list.insert(index, new_name)
                
                print("The change is done")
                break


        case "4":
            position = input("Which name you wanna delete?: ").strip()
        
            if not position.isdigit():
                print("The position it has to be a number")
                continue

            position = int(position)
        
            if position < 0 or position >= len(names_list):
                print("Invalid position, for more infomation see 2nd option")
                continue
                
            names_list.pop(position)
            print("The name was remove")
            break
