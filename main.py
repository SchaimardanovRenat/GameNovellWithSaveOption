from PIL import Image
import random
import sys
import csv
import os

inventory = []

questions = {
    "Сколько будет 2+2?": "4",
    "Какое полное название столицы Франции?": "Париж",
    "Как называется самая большая планета в Солнечной системе?": "Юпитер"
}


def write_data(file_name, player_name, inventory):
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([player_name] + inventory)


def remove_data(file_name, player_name):
    rows = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != player_name:
                rows.append(row)

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)


congratulation2 = Image.open("congratulation2.gif")


def receive_random_item():
    item = random.choice(["топор", "ложка"])
    inventory.append(item)


def read_data(file_name, player_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == player_name:
                inventory.extend(row[1:])  # Добавляем предметы игрока в инвентарь
                break


def punch_tree():
    print("Вы решили ударить дерево.")
    if 'топор' in inventory:
        print("Звук удара оглушает вас на мгновение, но в тот же момент из-под дерева падает ключ.")
        print(
            "Кажется он был тайно спрятан внутри ствола дерева. Вы поднимаете ключ с земли и понимаете, что это именно то, что нужно, чтобы выбраться из леса.")
        print(
            "С радостью и уверенностью в шагах вы направляетесь к выходу, используя ключ, вам удается открыть ворота, пересекая порог вы освобождаетесь от лабиринта леса.")
        print("Вы оказываетесь на свободе, уверенные в своих способностях и с чувством успеха.")
        print("Вы отправляетесь на поиски новых приключений")
        print("Вы прошли игру")
        congratulation2.show()
        sys.exit()
    else:
        print(
            "Сокрушенный и обескураженный, вы, потерявшись в безысходности, решаете выбраться из этой тупиковой ситуации.")
        print(
            "Вспыхивая пламенным гневом, вы собираете всю свою силу и наносите сокрушительный удар головой о ствол дерева")
        print("С таким глубоким размышлением, вы осознали, что взялись за самое безрассудное решение ")
        print("после чего вы подумали что это была ваша предпоследняя мысль")
        print("Великий путешественник погибает")
        print("Вы проиграли")
        sys.exit()


def show_status():
    print(f"У вас в инвентаре {len(inventory)} предмет{'а' if len(inventory) == 1 else 'ов'}:")
    for item in inventory:
        print("- " + item)


def random_encounter():
    print("Непредвиденная встреча!")
    if len(inventory) > 0:
        print("Вас ограбили и забрали все ваши предметы!")
        inventory.clear()
    else:
        print("Вас ограбили, но у вас ничего не было при себе.")


def show_players(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            player_name = row[0]
            items = row[1:]

            print(f"{player_name}:")
            for item in items:
                print("- " + item)

            print()
def play_round():
    question = random.choice(list(questions.keys()))
    correct_answer = questions[question]

    print(f"Магический лес задает вопрос.Вопрос: {question}")
    answer = input("Ваш ответ: ")

    if answer.lower() == correct_answer.lower():
        print("Правильно! Вы получаете награду.")
        receive_random_item()
    else:
        print("Неправильно! Вас атаковали.")


def main():
    player_name = ""
    print("Добро пожаловать в игру!")
    print("Вы находитесь в темном лесу.")
    print(
        "С множеством приключений за вашими плечами и годами путешествий, вам стало ясно, что этот лес был пропитан магией.")
    print(
        "Он словно заперает каждого под своими чарами, и чтобы выбраться отсюда, придется переубедить саму природу отпустить вас.")

    while True:
        print("Что вы будете делать?")
        print("1. Искать выход")
        print("2. Проверить инвентарь")
        print("3. Выйти из игры")
        print("4. Ударить по дереву от безысходности")
        print("5. Сохранить игру")
        print("6. Загрузить игру")
        print("7. Удалить сохранение")
        choice = input("Выберите номер: ")

        if choice == "1":
            play_round()
        elif choice == "2":
            show_status()
        elif choice == "4":
            punch_tree()
        elif choice == "3":
            print("Спасибо за игру! До свидания.")
            break
        elif choice == "5":
            player_name = input("Введите имя игрока: ")
            write_data('inventory.csv', player_name, inventory)
        elif choice == "6":
            player_name = input("Введите имя игрока: ")
            read_data('inventory.csv', player_name)

        elif choice == "7":
            player_name = input("Введите имя игрока: ")
            remove_data('inventory.csv', player_name)
        elif choice == "8":
            show_players('inventory.csv')


main()