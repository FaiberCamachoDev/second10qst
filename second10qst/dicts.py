# P2. Diccionarios — Inventario básico
# Crear un diccionario con al menos cuatro productos y sus precios. El usuario elige una acción:

# Agregar un nuevo producto con su precio.
# Consultar el precio de un producto existente.
# Modificar el precio de un producto existente.
# Eliminar un producto del inventario.
# Al terminar la acción seleccionada, mostrar cuántos productos hay actualmente y el promedio de precios.


dict_products = {
    "milk":3000,
    "arepas":2000,
    "meat":15000,
    "cigarret":500
}
choice = 0

while choice != 5:
    
    print("\n--- Options ---\n1. Add a product\n2. Check prices\n3. Modified a price\n4. Delete a product\n5. Exit\n")
    choice = int(input("\nWhat do you want to do?: "))

    match choice:
        case 1:
            product = input("\nWhich product do you want to add?: ").strip().lower()
            price = int(input("\nHow is it cost?: "))
            dict_products[product] = price
            print(f"\nYou add: {product}")
        
        case 2:
            for keys in dict_products.keys():
                print(keys)
            
            product = input("\nWhich price do you want to see?: ").strip().lower()
            
            if product in dict_products:
                print(f"\nThe price of {product} is {dict_products[product]}")

        case 3:
            print(dict_products)
            product = input("\nTo which product do you want to change its price?: ").strip().lower()
            price = int(input("\nHow is it costt now?: "))
            
            dict_products[product] = price
            print(f"\nNow {product} cost is {price}")

        case 4:
            print(dict_products)
            product = input("\nWhich product do you want to delete?: ").strip().lower()
            
            if product in dict_products:
                dict_products.pop(product)
                print(f"\nYou delete: {product}")

    total_products = len(dict_products)
    average_price = 0

    for price in dict_products.values():
        average_price += price
    
    average_price /= total_products
    
    print(f"Now you have {total_products} products and the average is {average_price}")
