import random


def human_func():
    human = random.randint(1,3)
    return human

def suspicous_func():
    suspicous = random.randint(3,6)
    return suspicous

def anomoly_func():
    anomoly = random.randint(6,16)
    return anomoly


def generate_attempts():
    #! chance
    list_1 = [1, 2, 3, 6, 7, 5, 7, 4, 7, 1, 2, 3, 5, 2, 5, 1, 2]
    list_2 = [2, 4, 2, 3, 6, 3, 1, 7, 2, 8, 1, 2, 3, 5, 1, 2, 3]

    x = random.randint(0, 16)
    y = random.randint(0, 16)

    random_number_1 = list_1[x]
    random_number_2 = list_2[y]

    result_1 = random_number_2 - random_number_1
    result_2 = result_1 * random.uniform(0.09, 0.2)

    return result_2

for x in range(200):
    random_number = generate_attempts()
    if random_number <= 0:
        human = human_func()
        print(f"Number {x} is a human, attempt amounts: {human}")

    elif random_number > 0 and random_number < 0.3:
        anomoly = anomoly_func()
        print(f"Number {x} is a anomoly, attempt amounts: {anomoly}")

    elif random_number > 0:
        suspicous = suspicous_func()
        print(f"Number {x} is a suspicous, attempt amounts: {suspicous}")
    