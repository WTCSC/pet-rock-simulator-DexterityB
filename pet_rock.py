import time
import random

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
hunger = 0
tiredness = 0
cleanliness = 3

type("Welcome to the Pet Rock Simulator!")
type("This is your pet rock")
rock("happy")
type("What do you want to name it?")
name = input("")

rock("wave")
buffer = name + " says hello"
type(buffer)
print("")

while health > 0 and trauma < 3:
    print(f"Health: {health}, Hunger: {hunger}, Tiredness: {tiredness}, Cleanliness: {cleanliness}, Trauma: {trauma}")

    emotion = None

    if hunger == 0 and tiredness == 0 and cleanliness == 3:
        buffer = name + " is happy"
        type(buffer)
        rock("happy")
    else:
        if tiredness > 2:
            buffer = name + " is really tired and needs a nap"
            type(buffer)
            print("")
            emotion = "sleepy"
            trauma += 1
            rock("sleepy")
            buffer = "Time passes and " + name + " wakes up"
            type(buffer)
            print("")
            tiredness = 0
            print(f"Health: {health}, Hunger: {hunger}, Tiredness: {tiredness}, Cleanliness: {cleanliness}, Trauma: {trauma}\n")
        if hunger == 1:
            buffer = name + " is a little bit hungry"
            type(buffer)
            emotion = "neutral"
        elif hunger == 2:
            buffer = name + " is pretty hungry"
            type(buffer)
            emotion = "hangry"
        if tiredness == 1:
            buffer = name + " is kind of tired, but not really"
            type(buffer)
            emotion = "neutral"
        elif tiredness == 2:
            buffer = name + " is very tired, and needs a nap"
            type(buffer)
            emotion = "tired"
        if cleanliness == 2:
            buffer = name + " is a little bit dirty"
            type(buffer)
            if emotion == None or emotion == "neutral":
                emotion = "derpy"
        elif cleanliness == 1:
            buffer = name + " is really dirty"
            type(buffer)
            if emotion == None or emotion == "neutral":
                emotion = "dirty"
        if trauma == 1:
            if emotion == None or emotion == "neutral":
                emotion = "gabberflasted"
        elif trauma == 2:
            if emotion == None or emotion == "neutral":
                emotion = "robotic"

        rock(emotion)

    type("What do you do?")
    buffer = "1) Feed " + name
    type(buffer)
    buffer = "2) Wash " + name
    type(buffer)
    buffer = "3) Play with " + name
    type(buffer)
    type("4) Nap time")
    buffer = "5) Neglect " + name
    type(buffer)

    decision = None
    while True:
        decision = input("")
        match decision:
            case "1":
                buffer = "You feed " + name
                type(buffer)
                hunger -= 2
                break
            case "2":
                buffer = "You wash " + name
                type(buffer)
                cleanliness = 3
                break
            case "3":
                buffer = "You play with " + name
                type(buffer)
                cleanliness -= 1
                tiredness += 1
                break
            case "4":
                tiredness = 0
                buffer = name + " takes a nap"
                rock("sleepy")
                type(buffer)
                print("")
                break
            case "5":
                buffer = "You neglect and therefore traumatize " + name
                type(buffer)
                trauma += 1
                break

    if health < 1:
        buffer = name + " has passed away"
        rock("dead")
        type(buffer)
        exit()
    if trauma > 2:
        buffer = "You neglected " + name + " too much and " + name + " takes revenge"
        rock("deranged")
        type(buffer)
        exit()
    if hunger > 3:
        buffer = name + " starves to death"
        rock("dead")
        type(buffer)
        exit()
    if hunger < 0:
        buffer = "You fed " + name + " too much food"
        rock("dead")
        type(buffer)
        exit()
    if cleanliness < 1:
        buffer = name + " is extremely dirty and takes damage"
        rock("dirty")
        type(buffer)
        health -= 1

    print(f"Health: {health}, Hunger: {hunger}, Tiredness: {tiredness}, Cleanliness: {cleanliness}, Trauma: {trauma}\n")
    type("Time passes\n")
    
    rng = random.randint(0, 2)
    match rng:
        case 0:
            hunger += 1
        case 1:
            tiredness += 1
        case 2:
            hunger += 1
            tiredness += 1
