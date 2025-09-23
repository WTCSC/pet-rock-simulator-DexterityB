# Life Decision Simulator

This project is a simulator where you take care of a pet rock, that has its needs constantly updated. Your goal is to make sure the rock stays alive and healthy.


## Requirements

* python3


## Installation

Download as a zip file or clone from github
* git clone **_https://github.com/WTCSC/pet-rock-simulator-DexterityB.git_**

(_Unzip if neccessary_) and open **pet-rock-simulator-DexterityB** in the terminal
* cd **pet-rock-simulator-DexterityB**

Run **pet_rock.py**, using python3, in the terminal
* python3 **pet_rock.py**


## Examples

Basic usage:

```python
rng = random.randint(0, 2)
    match rng:
        case 0:
            hunger += 1
        case 1:
            tiredness += 1
        case 2:
            hunger += 1
            tiredness += 1
```


Advanced usage:

```python
def rock(emotion):
    with open("rock_images.txt") as file:
        print(file.read().split("%" + emotion + "%")[1])
    return None
```


Intended flow of the game:
1. The rock has the stats of: Health: 3, Hunger: 0, Tiredness: 0, Cleanliness: 3, Trauma: 0
2. After each scenario the rock has a random chance of increasing 1 hunger, 1 tiredness, or both
3. Each option changes statistics in a certain way
 - Feeding the rock decreases hunger by 2
 - Washing the rock resets the cleanliness to 3
 - Playing with the rock increases tiredness by 1 and decreases cleanliness by 1
 - Nap time resets the tiredness to 0
 - Neglecting the rock increases trauma by 1
4. The rock will forcibly sleep, resetting tiredness to 0 but also increasing trauma by 1, if tiredness gets to 3
5. The game will end if the hunger gets below 0 or equal to 3, if the health gets to 0, or if the trauma gets to 3
6. The health will decrease by 1 if the cleanliness < 1


Decision function:

```python
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
```


## Contributing

* The code is not very well optimized, and you could add different if statements to what happens with certain statistics
* Use push requests


## Testing

* Just run the code using python3, and run through the code to make sure it works properly, meaning:
 * Stats lead to the right scenarios
 * The rock dies when it gets to certain stats
 * The game ends when the rock dies
* Don't push if there are errors


## License

This project is not licensed


[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/3zOHVIfr)
