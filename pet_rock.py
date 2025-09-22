import time

def type(phrase):
    for char in phrase:
        print(char, end = "", flush = True)
        time.sleep(0.03)
    print("")
    time.sleep(0.2)
    return None

def rock(emotion):
    with open("rock_images.txt") as file:
        print(file.read().split("%" + emotion + "%")[1])
    return None

health = 3
trauma = 0
stats = {"hunger": 0, "tiredness": 0, "cleanliness": 3}

type("Welcome to the Pet Rock Simulator!")
type("This is your pet rock")
rock("happy")
type("What do you want to name it?")
name = input("")

rock("wave")
buffer = name + " says hello"
type(buffer)

while health > 0 and trauma < 3:
    stats["hunger"] += 1
    match stats:
        case {"hunger": 0, "tiredness": 0, "cleanliness": 3}:
            rock("happy")
        case {"hunger": range(1,3), "tiredness": 0, "cleanliness": 3}:
            rock("neutral")
            health = 0