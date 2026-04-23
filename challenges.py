import random
from utils import slow_print


def password_crack(difficulty):
    passwords = ["cyber123", "admin007", "secureX", "hackme99", "rootAccess", "shadow01"]
    password = random.choice(passwords)

    # Difficulty settings
    if difficulty == "easy":
        attempts = 5
        hints_available = 2
    elif difficulty == "medium":
        attempts = 3
        hints_available = 1
    else:
        attempts = 2
        hints_available = 0

    # Unique hint positions
    hint_positions = list(range(len(password)))
    random.shuffle(hint_positions)
    used_hints = 0

    slow_print("\n[ACCESS TERMINAL]")
    slow_print("Type 'help' to see available commands.\n")

    login_started = False

    while True:
        cmd = input(">> ").lower()

        # -------- HELP --------
        if cmd == "help":
            print("Commands: scan, hint, login, exit")

        # -------- SCAN --------
        elif cmd == "scan":
            slow_print("Scanning system...")
            slow_print("Open ports: 22 (SSH), 80 (HTTP)")
            slow_print("Login portal detected.\n")

        # -------- HINT (NOW AVAILABLE ALWAYS) --------
        elif cmd == "hint":
            if hints_available > 0:
                pos = hint_positions[used_hints]
                slow_print(f"Hint: character at position {pos+1} is '{password[pos]}'")
                hints_available -= 1
                used_hints += 1
            else:
                slow_print("No hints remaining!")

        # -------- LOGIN --------
        elif cmd == "login":
            if not login_started:
                slow_print("\n[LOGIN MODE ACTIVATED]")
                login_started = True

            while attempts > 0:
                guess = input("Enter password (or type 'hint'): ")

                # 🔥 Allow hint DURING login
                if guess.lower() == "hint":
                    if hints_available > 0:
                        pos = hint_positions[used_hints]
                        slow_print(f"Hint: character at position {pos+1} is '{password[pos]}'")
                        hints_available -= 1
                        used_hints += 1
                    else:
                        slow_print("No hints remaining!")
                    continue

                if guess == password:
                    slow_print("Access Granted!\n")
                    return True
                else:
                    attempts -= 1
                    slow_print(f"Access Denied! Attempts left: {attempts}")

            slow_print("System Locked!\n")
            return False

        # -------- EXIT --------
        elif cmd == "exit":
            slow_print("Exiting terminal...")
            return False

        else:
            slow_print("Unknown command. Type 'help'.")