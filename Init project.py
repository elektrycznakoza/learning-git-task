# zadanie: pierwsze samodzielne commity
# -*- coding: utf-8 -*-

# punkt 5
shopping_list = {
    "grocery_store": ["oranges", "bananas", "milk"],
    "bakery_store": ["bread", "eggs", "butter"],
    "convenience_store": ["water", "apple juice", "chocolate"]
}

# Inicjalizacja zmiennej na sumę produktów
total_products = 1

# Iteracja po słowniku i wyświetlanie informacji o zakupach
# punkt 6
for store, items in shopping_list.items():
    # Przetwarzanie nazw sklepów i produktów na wielkie litery
# punkt 7
    store_name_capitalized = store.capitalize()
    items_name_capitalized = [item.capitalize() for item in items]

    # Wyświetlenie informacji o zakupach w danym sklepie
    print(f"Idę do {store_name_capitalized} i kupuję tam {', '.join(items_name_capitalized)}")
    
    # Zliczanie produktów
    total_products += len(items)

# Wyświetlenie sumy produktów
print(f"W sumie kupuję {total_products} produktów.")
