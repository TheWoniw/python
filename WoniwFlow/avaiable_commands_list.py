
def banner():
    banner_list = [
        [" █     █░ ▒█████   ███▄    █  ██▓ █     █░  █████▒██▓     ▒█████   █     █░"],
        ["▓█░ █ ░█░▒██▒  ██▒ ██ ▀█   █ ▓██▒▓█░ █ ░█░▓██   ▒▓██▒    ▒██▒  ██▒▓█░ █ ░█░"],
        ["▒█░ █ ░█ ▒██░  ██▒▓██  ▀█ ██▒▒██▒▒█░ █ ░█ ▒████ ░▒██░    ▒██░  ██▒▒█░ █ ░█ "],
        ["░█░ █ ░█ ▒██   ██░▓██▒  ▐▌██▒░██░░█░ █ ░█ ░▓█▒  ░▒██░    ▒██   ██░░█░ █ ░█ "],
        ["░░██▒██▓ ░ ████▓▒░▒██░   ▓██░░██░░░██▒██▓ ░▒█░   ░██████▒░ ████▓▒░░░██▒██▓ "],
        ["░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▓  ░ ▓░▒ ▒   ▒ ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▓░▒ ▒  "],
        ["  ▒ ░ ░    ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░  ▒ ░ ░   ░     ░ ░ ▒  ░  ░ ▒ ▒░   ▒ ░ ░  "],
        ["  ░   ░  ░ ░ ░ ▒     ░   ░ ░  ▒ ░  ░   ░   ░ ░     ░ ░   ░ ░ ░ ▒    ░   ░  "],
        ["    ░        ░ ░           ░  ░      ░               ░  ░    ░ ░      ░    "]
    ]

    for banner_part in banner_list:
        for each_part in banner_part:
            print(each_part)
            
def availaible_commands_list():
    commands = [
        ["|-------- Command Options --------|"],
        ["1. Generate  -- Generates fake traffic"],
        ["2. Clear     -- Clears generated traffic"],
        ["3. Quit      -- exit the script"],
    ]

    for command in commands:
        for each_command in command:
            print(each_command)