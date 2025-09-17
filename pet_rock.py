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

type("Welcome to the Pet Rock Simulator!")
type("This is your pet rock")

rock("neutral")
time.sleep(1)
rock("sleepy")
time.sleep(1)
rock("gabberflasted")
time.sleep(1)
rock("robotic")
time.sleep(1)
rock("angry")
time.sleep(1)
rock("hangry")
time.sleep(1)
rock("deranged")
time.sleep(1)
rock("derpy")
time.sleep(1)
rock("happy")