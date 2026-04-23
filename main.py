from utils import slow_print, divider, select_difficulty, banner
from challenges import password_crack, cipher_challenge, log_analysis_challenge


def show_intro():
    banner()
    slow_print("Welcome, Agent.")
    slow_print("You have been assigned a mission to test system security.\n")


def play_game():
    score = 0

    show_intro()
    difficulty = select_difficulty()

    # ---- MISSION 1 ----
    slow_print("\n[MISSION 1]")
    slow_print("Target: SecureCorp Server")
    slow_print("Objective: Crack the login password\n")

    if password_crack(difficulty):
        score += 10
        slow_print("Mission 1 Completed!\n")
    else:
        slow_print("Mission Failed!")
        return score

    # ---- MISSION 2 ----
    if cipher_challenge(difficulty):
        score += 10
        slow_print("Mission 2 Completed!\n")
    else:
        slow_print("Mission Failed!")
        return score

    # ---- MISSION 3 ----
    if log_analysis_challenge(difficulty):
        score += 10
        slow_print("Mission 3 Completed!\n")
    else:
        slow_print("Mission Failed!")
        return score

    # ---- FINAL RESULT ----
    slow_print(f"\nFinal Score: {score}/30")
    slow_print("All Missions Completed!")
    slow_print("You are a certified cyber agent.\n")

    return score


def play_again():
    choice = input("Do you want to play again? (y/n): ").lower()
    return choice == "y"


def main():
    while True:
        play_game()
        if not play_again():
            slow_print("Exiting game...")
            break


if __name__ == "__main__":
    main()