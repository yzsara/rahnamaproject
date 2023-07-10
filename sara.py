import random

names = []
cities = []
foods = []
colors = []

score_unique = 10
score_same = 5
score_wrong = 0

def generate_letter():
    letter = random.choice('abcdefghijklmnopqrstuvwxyz')
    print("letter:", letter)

def calculate_scores():
    user_scores = {}

    for user in names:
        name_score = len(set(names)) * score_unique - (names.count(user) - 1) * score_same
        color_score = len(set(colors)) * score_unique - (colors.count(user) - 1) * score_same
        city_score = len(set(cities)) * score_unique - (cities.count(user) - 1) * score_same
        food_score = len(set(foods)) * score_unique - (foods.count(user) - 1) * score_same

        total_score = name_score + color_score + city_score + food_score
        user_scores[user] = total_score

    # Print the scores for each user
    for user, score in user_scores.items():
        print(f"User: {user}, Score: {score}")

        

def add_name():
    name = input("name : ")
    names.append(name)

def add_city():
    city = input("city: ")
    cities.append(city)

def add_food():
    food = input("food")
    foods.append(food)

def add_color():
    color = input("color ")
    colors.append(color)

harf=generate_letter()
users=input("tedad bazikona :  ")
print("harf : "+ harf)

for i in range(int(users)):
        while True:
            action = input("command: ")

            if action == "name":
                add_name()
            elif action == "city":
                add_city()
            elif action == "food":
                add_food()
            elif action == "color":
                add_color()
            # elif action == "calculate":
            #     calculate_scores()
            elif action == "exit ":
                break
            else:
                print("invalid")


calculate_scores()
