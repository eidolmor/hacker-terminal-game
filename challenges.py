import random
from utils import slow_print

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


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

def cipher_challenge(difficulty):
    words = ["network", "security", "database", "encryption", "firewall", "protocol", "malware", "authentication", "cyberattack", "vulnerability"]
    word = random.choice(words)
    shift = random.randint(1, 5)

    encrypted = caesar_encrypt(word, shift)

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

    # Create hints
    hints = [
    f"Shift value is {shift}",
    f"First letter is '{word[0]}'",
    f"Last letter is '{word[-1]}'",
    f"Word contains letter '{random.choice(word)}'"
    ]

    random.shuffle(hints)  # randomize order
    hint_index = 0

    slow_print("\n[MISSION 2: ENCRYPTED MESSAGE]")
    slow_print(f"Encrypted text: {encrypted}")
    slow_print("Decrypt the message.\n")
    slow_print("Type 'hint' for help.\n")

    while attempts > 0:
        answer = input(">> Your answer: ").lower()

        # 🔹 Hint system (NO repetition now)
        if answer == "hint":
            if hints_available > 0 and hint_index < len(hints):
                slow_print(f"Hint: {hints[hint_index]}")
                hint_index += 1
                hints_available -= 1
            else:
                slow_print("No hints remaining!")
            continue

        # 🔹 Check answer
        if answer == word:
            slow_print("Correct Decryption!\n")
            return True
        else:
            attempts -= 1
            slow_print(f"Wrong! Attempts left: {attempts}")

    slow_print("Decryption Failed!\n")
    return False

def log_analysis_challenge(difficulty):
    import random
    from utils import slow_print

    users = ["admin", "guest", "root", "user1", "dev", "tester"]
    ips = [
        "192.168.1.10",
        "192.168.1.23",
        "192.168.1.45",
        "10.0.0.5",
        "172.16.0.2"
    ]

    suspicious_ip = random.choice(ips)
    suspicious_user = random.choice(users)

    logs = []

    # 🔹 Generate realistic mixed logs
    actions = ["logged in", "logged out", "accessed file", "changed settings"]

    for _ in range(8):  # more normal logs
        user = random.choice(users)
        action = random.choice(actions)
        logs.append(f"User {user} {action}")

    # 🔹 Suspicious behavior patterns
    for _ in range(random.randint(2, 4)):
        logs.append(f"User {suspicious_user} failed login")

    for _ in range(random.randint(2, 4)):
        logs.append(f"IP {suspicious_ip} multiple requests detected")

    # 🔹 Noise logs
    for _ in range(3):
        logs.append(f"IP {random.choice(ips)} ping success")

    random.shuffle(logs)

    # Difficulty
    if difficulty == "easy":
        attempts = 3
        hints_available = 2
    elif difficulty == "medium":
        attempts = 2
        hints_available = 1
    else:
        attempts = 1
        hints_available = 0

    slow_print("\n[MISSION 3: LOG ANALYSIS]")
    slow_print("Identify the suspicious USER or IP.\n")

    for log in logs:
        print(log)

    # ✅ Better hints (no useless ones)
    hints = [
        f"Suspicious user starts with '{suspicious_user[0]}'",
        f"Suspicious IP starts with {suspicious_ip.split('.')[0]}",
        "Look for repeated failed login attempts",
        "Look for unusual high-frequency IP activity"
    ]

    random.shuffle(hints)
    hint_index = 0

    while attempts > 0:
        answer = input("\n>> Enter suspicious user or IP (or type 'hint'): ").lower()

        if answer == "hint":
            if hints_available > 0 and hint_index < len(hints):
                slow_print(f"Hint: {hints[hint_index]}")
                hint_index += 1
                hints_available -= 1
            else:
                slow_print("No hints remaining!")
            continue

        if answer == suspicious_user.lower() or answer == suspicious_ip.lower():
            slow_print("Correct Analysis!\n")
            return True
        else:
            attempts -= 1
            slow_print(f"Incorrect! Attempts left: {attempts}")

    slow_print("Analysis Failed!\n")
    return False