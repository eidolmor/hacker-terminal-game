from utils import slow_print, select_difficulty, banner
from challenges import password_crack, cipher_challenge, log_analysis_challenge


class Game:
    def __init__(self):
        self.score = 0
        self.difficulty = None

    def show_intro(self):
        banner()
        slow_print("Welcome, Agent.")
        slow_print("You have been assigned a mission to test system security.\n")

    def setup(self):
        self.show_intro()
        self.difficulty = select_difficulty()

    def run_mission(self, mission_func, mission_name):
        slow_print(f"\n[{mission_name}]")

        result = mission_func(self.difficulty)

        if result:
            self.score += 10
            slow_print(f"{mission_name} Completed!\n")
            return True
        else:
            slow_print("Mission Failed!")
            return False

    def play(self):
        self.setup()

        # Mission 1
        if not self.run_mission(password_crack, "MISSION 1"):
            return self.score

        # Mission 2
        if not self.run_mission(cipher_challenge, "MISSION 2"):
            return self.score

        # Mission 3
        if not self.run_mission(log_analysis_challenge, "MISSION 3"):
            return self.score

        # Final result
        slow_print(f"\nFinal Score: {self.score}/30")
        slow_print("All Missions Completed!")
        slow_print("You are a certified cyber agent.\n")

        return self.score


def play_again():
    choice = input("Do you want to play again? (y/n): ").lower()
    return choice == "y"


def main():
    while True:
        game = Game()   # 🔥 Object created here
        game.play()

        if not play_again():
            slow_print("Exiting game...")
            break


if __name__ == "__main__":
    main()