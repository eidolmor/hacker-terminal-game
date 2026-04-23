import time


def slow_print(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def divider():
    print("=" * 35)


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