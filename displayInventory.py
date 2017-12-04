'''
Write a function named displayInventory() that would take any possible “inventory” and display it like the following:

Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62

Hint: You can use a for loop to loop through all the keys in a dictionary.
'''
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)

#displayInventory(stuff)