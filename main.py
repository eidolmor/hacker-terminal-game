from utils import slow_print, divider, select_difficulty
from challenges import password_crack


def show_intro():
    divider()
    print("     HACKER TERMINAL v1.0     ")
    divider()
    slow_print("Welcome, Agent.")
    slow_print("You have been assigned a mission to test system security.\n")


def main():
    show_intro()

    difficulty = select_difficulty()

    slow_print("\n[MISSION 1]")
    slow_print("Target: SecureCorp Server")
    slow_print("Objective: Crack the login password\n")

    result = password_crack(difficulty)

    if result:
        slow_print("Mission Completed!")
    else:
        slow_print("Mission Failed!")


if __name__ == "__main__":
    main()