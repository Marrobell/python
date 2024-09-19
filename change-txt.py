file = open("devices.txt", "r")
for item in file:
    item = item.strip()
    print(item)
file.close()
while True:
    newtext = input("Enter 'T'ext to read file" "\n" "Enter new device name" "\n" "enter exit to close: ")
    if newtext == "exit":
        break
    elif newtext == "T":
        file = open("devices.txt", "r")
        for item in file:
            item = item.strip()
            print(item)
        file.close()
    file = open("devices.txt", "a")
    if newtext != "T":
        file.write(newtext + "\n")
    file.close()
file.close()
