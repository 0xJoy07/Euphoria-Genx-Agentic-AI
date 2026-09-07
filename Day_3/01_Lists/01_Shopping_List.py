def update_shopping_list(items, add_item, remove_item, index, new_item):
    shopping = items.copy()
    print(shopping[0])
    print(shopping[-1])
    shopping.append(add_item)
    shopping.remove(remove_item)
    shopping[index] = new_item
    return shopping


shopping = ["Milk", "Bread", "Eggs", "Rice"]
result = update_shopping_list(shopping, "Butter", "Bread", 3, "Pasta")
print(result)
