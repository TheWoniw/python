import random
import time
from json_functions import load_json
from json_functions import save_json
from avaiable_commands_list import availaible_commands_list
# json data
#?json_path = "/home/woniw/Desktop/python/ip_list.json"
data = load_json("ip_list.json")


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


def generate_ip():
    generated_ip = f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'
    return generated_ip

def generate_ip_list(ip_list):
    range_input = int(input("Input Range: "))
    print('')
    time.sleep(1)

    for count in range(range_input):
        count += 1

        random_number = generate_attempts()
        if random_number <= 0:
            human = human_func()
            ip_list.append({count: {"ip": generate_ip(), "attempts": human}})

        elif random_number > 0 and random_number < 0.3:
            anomoly = anomoly_func()
            ip_list.append({count: {"ip": generate_ip(), "attempts": anomoly}})
        elif random_number > 0:
            suspicous = suspicous_func()
            ip_list.append({count: {"ip": generate_ip(), "attempts": suspicous}})

    save_json(data, "ip_list.json")  
    print("|--- IP List Has Been Generated ---|")
    print('')
    time.sleep(3)

def clear_generated_ip_list(ip_list):
    ip_list.clear()
    save_json(data, "ip_list.json")  
    print("|--- IP List Has Been Cleared ---|")
    print('')
    time.sleep(3)

available_commands = {
    "1": generate_ip_list,
    "2": clear_generated_ip_list
}


def main():

    ip_list = data['my_ip_list']

    while True:
        from avaiable_commands_list import banner
        print('')
        banner()
        print('')
        availaible_commands_list()
        print('')
        user_in = str(input("Select Creation Option: "))
        print('')  

        if user_in == "3":
            break
        
        if user_in in available_commands:
            available_commands[user_in](ip_list)
        elif user_in not in available_commands:
            print("not a valid command")
            continue
main()