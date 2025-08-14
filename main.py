import random
import time
from json_functions import load_json
from json_functions import save_json

#! json stuff
json_path = "/home/woniw/Desktop/python/ip_list.json"
data = load_json(json_path)

print(data)

def generate_ip():
    generated_ip = f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'
    return generated_ip

def generate_ip_list(ip_list, range_count):
    print("generating ip lists")
    ip_list = data['my_ip_list']
    for _ in range(20):
        ip_list.append(generate_ip())
    save_json(data, json_path)  
    print("|--- IP List Has Been Generated ---|")

def clear_generated_ip_list(ip_list):
    print("clearing ip lists")
    ip_list == []
    save_json(data, json_path)  
    print("|--- IP List Has Been Cleared ---|")

def main():

    ip_list = data['my_ip_list']
    range_count = 10

    #generate_ip_list(ip_list, range_count)

    clear_generated_ip_list(ip_list)
    print(ip_list)

main()