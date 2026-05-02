# The Ultimate Dictionary Muscle Memory Workout
# Theme: Architecting the Ultimate AI Engineering Rig

# 1. Initialization (The standard way to build a dict)
my_rig = {
    "brand": "Lenovo Legion",
    "gpu": "RTX 4090", 
    "ram_gb": 32,
    "storage_tb": 2
}

# 2. copy() - Always backup your data before you mutate it
rig_backup = my_rig.copy()
print(f"[*] Backup created. Items in backup: {len(rig_backup)}")

# 3. update() - Bulk adding or modifying multiple key-value pairs at once
my_rig.update({"gpu": "RTX 5090", "cooling": "Liquid", "rgb": True})
print(f"[*] Upgraded rig: {my_rig}")

# 4. get() - Safe extraction. 
# If 'price' doesn't exist, it returns the default string instead of crashing with a KeyError
price = my_rig.get("price", "Priceless (or you just lack the funds)")
print(f"[*] Rig Price: {price}")

# 5. setdefault() - Adds a key-value pair ONLY if the key doesn't already exist
# We forgot the processor. Let's add it.
my_rig.setdefault("cpu", "Intel Core i9")
# If we try to set "gpu" again using setdefault, it will ignore it because "gpu" exists
my_rig.setdefault("gpu", "GTX 1060") 

# 6. items(), keys(), values() - The Holy Trinity of Dictionary Loops
print("\n--- Spec Sheet (Keys & Values) ---")
for key, value in my_rig.items():
    print(f"- {key.upper()}: {value}")

print("\n--- Just the Keys ---")
for k in my_rig.keys():
    print(k, end=" | ")

print("\n\n--- Just the Values ---")
for v in my_rig.values():
    print(v, end=" | ")

# 7. pop() - Targeted removal using a specific key
# RGB doesn't increase your coding speed. Drop it.
dropped_feature = my_rig.pop("rgb", "Feature not found")
print(f"\n\n[-] Removed feature: {dropped_feature}")

# 8. popitem() - Removes the last inserted Key-Value pair (LIFO - Last In, First Out)
last_added = my_rig.popitem()
print(f"[-] Last item removed from dict: {last_added} (Should be the CPU)")

# 9. fromkeys() - Creates a new dictionary from an existing list, giving them all the same default value
wishlist_items = ["Mechanical Keyboard", "Dual Monitors", "Ergonomic Chair"]
wishlist = dict.fromkeys(wishlist_items, "Pending Budget")
print(f"\n[*] New Wishlist initialized: {wishlist}")

# 10. clear() - Nuke the dictionary from orbit
wishlist.clear()
print(f"[*] Wishlist after actually checking your bank account: {wishlist}")