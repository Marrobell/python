name = input("Введите имя: ")
print("Привет", name, "сколько тебе лет?")
age = input("Сколько тебе лет? ")
if (age >= "20") and (age <= "29"):
    print(f"{name}, Так тебе уже двадцатник, фига ты здоровый вымахал")
elif (age >= "30") and (age <= "39"):
    print(f"{name}, Так тебе уже тридцатник, фига ты здоровый вымахал")
elif (age >= "40") and (age <= "49"):
    print(f"{name}, Так тебе уже сорокетник, фига ты здоровый вымахал")
elif (age >= "50") and (age <= "59"):
    print(f"{name}, Так тебе уже полтос, фига ты здоровый вымахал")
elif (age >= "60") and (age <= "69"):
    print(f"{name}, Так тебе уже за 60, фига ты здоровый вымахал")
elif (age >= "70") and (age <= "79"):
    print(f"{name}, Так тебе уже за 70, фига ты здоровый вымахал")
elif (age >= "80") and (age <= "89"):
    print(f"{name}, Так ты дед 80 лет")
elif (age >= "90") and (age <= "99"):
    print(f"{name}, Так ты дед 90 лет")
elif (age >= "100") and (age <= "999999"):
    print(f"{name}, Так люди столько не живут")

