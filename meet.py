name = input("Введите имя: ")
print("Привет", name, "сколько тебе лет?")
age = input("Сколько тебе лет? ")
if (age >= "1") == (age <= "19"):
    print(f"{name}, школота")
elif (age >= "20") == (age <= "29"):
    print(f"{name}, Так тебе уже двадцатник, фига ты здоровый вымахал")
elif (age >= "30") == (age <= "39"):
    print(f"{name}, Так тебе уже тридцатник, фига ты здоровый вымахал")
elif (age >= "40") == (age <= "49"):
    print(f"{name}, Так тебе уже сорокетник, фига ты здоровый вымахал")
elif (age >= "50") == (age <= "59"):
    print(f"{name}, Так тебе уже полтос, фига ты здоровый вымахал")
elif (age >= "60") == (age <= "69"):
    print(f"{name}, Так тебе уже за 60, фига ты здоровый вымахал")
elif (age >= "70") == (age <= "79"):
    print(f"{name}, Так тебе уже за 70, фига ты здоровый вымахал")
elif (age >= "80") == (age <= "89"):
    print(f"{name}, Так ты дед 80 лет")
elif (age >= "90") == (age <= "99"):
    print(f"{name}, Так ты дед 90 лет")
elif (age >= "100")== (age <= "129"):
    print(f"{name}, претендуешь на самого старого человека на земле")
else:
    print(f"{name}, Так люди столько не живут")
