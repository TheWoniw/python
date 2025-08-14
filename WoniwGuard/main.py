from json_functions import load_json

def clear_text():
    for x in range(20):
        print("")

def scan(ip_list, total_human, total_suspicous, total_malicous):
    ip_number = int(input("|$|: "))

    clear_text()

    print("| ------  LOG  ------ |")
    print('')
    for ip_number in range(ip_number):
        ip_number += 1
        if str(ip_number) in ip_list["my_ip_list"][ip_number - 1]:
            ip_address = ip_list["my_ip_list"][ip_number - 1][str(ip_number)]['ip']
            login_attempts = ip_list["my_ip_list"][ip_number - 1][str(ip_number)]['attempts']

            if login_attempts <= 3:
                total_human += 1
                print(f"{ip_number}. {ip_address} SUSPECTED AS HUMAN       -- H")
                print(f"----> LOGIN ATTEMPTS: {login_attempts}")
                print("")
            elif login_attempts > 3 and login_attempts < 10:
                total_suspicous += 1
                print(f"{ip_number}. {ip_address} FLAGGED AS SUSPICOUS     -- S")
                print(f"----> LOGIN ATTEMPTS: {login_attempts}")
                print("")
            elif login_attempts > 10:
                total_malicous += 1
                print(f"{ip_number}. {ip_address} FLAGGED AS MALICOUS      -- A")
                print(f"----> LOGIN ATTEMPTS: {login_attempts}")
                print("")
        else:
            print("ERROR")

    print("| ------  SUMMARY  ------ |")
    print(f"TOTAL HUMAN: {total_human}")
    print(f"TOTAL SUSPICOUS: {total_suspicous}")
    print(f"TOTAL MALICOUS: {total_malicous}")

def main():
    total_human = 0
    total_suspicous = 0
    total_malicous = 0

    ip_list_json = load_json("/home/woniw/Desktop/python/ip_list.json")

    from banner import banner
    banner()
    scan(ip_list_json, total_human, total_suspicous, total_malicous)

main()