import time


def slow_print(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def divider():
    print("=" * 35)

def banner():
    print("=" * 60)
    print(r"""
 _    _            _                _______                  _             _ 
| |  | |          | |              |__   __|                (_)           | |
| |__| | __ _  ___| | _____ _ __      | | ___ _ __ _ __ ___  _ _ __   __ _| |
|  __  |/ _` |/ __| |/ / _ \ '__|     | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | |
| |  | | (_| | (__|   <  __/ |        | |  __/ |  | | | | | | | | | | (_| | |
|_|  |_|\__,_|\___|_|\_\___|_|        |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_|
                                                                           
""")
    print(" " * 45 + "by EIDOLMOR")
    print("=" * 60)


def select_difficulty():
    divider()
    print("Select Difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input(">> ")

    if choice == "1":
        return "easy"
    elif choice == "2":
        return "medium"
    else:
        return "hard"