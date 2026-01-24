import random
import os
import time

# --- ANSI Color Codes for Terminal "UI" ---
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"

STAGES = [
    f"""
    {RED}  --------
      |      |
      |      O
      |     \\|/
      |      |
      |     / \\
      -{RESET}""", 
    f"""
    {RED}  --------
      |      |
      |      O
      |     \\|/
      |      |
      |     / 
      -{RESET}""",
    f"""
    {YELLOW}  --------
      |      |
      |      O
      |     \\|/
      |      |
      |      
      -{RESET}""",
    f"""
    {YELLOW}  --------
      |      |
      |      O
      |     \\|
      |      |
      |     
      -{RESET}""",
    f"""
    {CYAN}  --------
      |      |
      |      O
      |      |
      |      |
      |     
      -{RESET}""",
    f"""
    {CYAN}  --------
      |      |
      |      O
      |    
      |      
      |     
      -{RESET}""",
    f"""
    {GREEN}  --------
      |      |
      |      
      |    
      |      
      |     
      -{RESET}"""
]

# Simple, unique word bank organized by Categories
CATEGORIES = {
    "BODY PARTS": {
        "HEART": "The organ that pumps blood.",
        "BRAIN": "The control center of the nervous system.",
        "ELBOW": "The joint between the upper and lower arm.",
        "TONGUE": "Used for tasting and speaking."
    },
    "ANIMALS": {
        "TIGER": "A large cat with orange and black stripes.",
        "EAGLE": "A powerful bird of prey with great vision.",
        "SHARK": "A fast-swimming predator of the ocean.",
        "PANDA": "A bear that primarily eats bamboo."
    },
    "FRUITS": {
        "MANGO": "Known as the king of fruits.",
        "CHERRY": "Small, round, red fruit often found on cakes.",
        "BANANA": "A long yellow fruit that grows in bunches.",
        "GRAPES": "Small green or purple fruits used to make wine."
    },
    "TECH": {
        "MOUSE": "A handheld pointing device for computers.",
        "SCREEN": "The part of the computer that shows visuals.",
        "ROBOT": "A machine capable of carrying out complex actions.",
        "WIFI": "Wireless technology used to connect to the internet."
    }
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def select_category():
    while True:
        clear_screen()
        print(f"{BOLD}{MAGENTA}=== SHADOWFOX HANGMAN: CHOOSE A CATEGORY ==={RESET}")
        cat_list = list(CATEGORIES.keys())
        for i, cat in enumerate(cat_list, 1):
            print(f"{i}. {cat}")
            
        choice = input(f"\n{BOLD}Select 1-{len(cat_list)}: {RESET}")
        if choice.isdigit() and 1 <= int(choice) <= len(cat_list):
            return cat_list[int(choice)-1]
        
        print(f"{RED}Invalid selection. Try again.{RESET}")
        time.sleep(1)

def display_keyboard(guessed_letters):
    """Displays a QWERTY-style keyboard showing which letters are used."""
    rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    print(f"\n{BOLD}VIRTUAL KEYBOARD:{RESET}")
    for row in rows:
        display_row = ""
        for char in row:
            if char in guessed_letters:
                display_row += f"{RED}{char}{RESET} "
            else:
                display_row += f"{GREEN}{char}{RESET} "
        print("  " + display_row)

def start_game():
    category_name = select_category()
    word_list = CATEGORIES[category_name]
    word = random.choice(list(word_list.keys()))
    hint = word_list[word]
    
    guessed_letters = []
    tries = 6
    
    while tries > 0:
        clear_screen()
        print(f"{BOLD}{MAGENTA}CATEGORY: {category_name}{RESET}")
        print(f"{YELLOW}HINT: {hint}{RESET}")
        
        # Placing correct letters according to their exact position in the word
        display_word = ""
        for char in word:
            if char in guessed_letters:
                display_word += f"{GREEN}{char}{RESET} "
            else:
                display_word += "_ "
        
        print(STAGES[tries])
        print(f"\n{BOLD}WORD STATUS:{RESET} {display_word}")
        print(f"{BOLD}CHANCES LEFT:{RESET} {tries}")
        
        display_keyboard(guessed_letters)
        print("-" * 35)
        
        # Check if user has won
        if all(char in guessed_letters for char in word):
            print(f"\n{GREEN}{BOLD}🎉 EXCELLENT! You correctly spelled '{word}'!{RESET}")
            break
            
        guess = input(f"{BOLD}Enter your guess: {RESET}").upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print(f"{RED}(!) Please enter only one letter.{RESET}")
            time.sleep(1)
            continue
            
        if guess in guessed_letters:
            print(f"{YELLOW}(!) You already tried '{guess}'.{RESET}")
            time.sleep(1)
            continue
            
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"{GREEN}Correct! '{guess}' is in the word.{RESET}")
        else:
            print(f"{RED}Wrong! '{guess}' is not there.{RESET}")
            tries -= 1
        time.sleep(0.8)
            
    if tries == 0:
        clear_screen()
        print(STAGES[0])
        print(f"\n{RED}{BOLD}GAME OVER!{RESET}")
        print(f"The correct spelling was: {BOLD}{word}{RESET}")

if __name__ == "__main__":
    while True:
        start_game()
        play_again = input(f"\n{BOLD}Play another round? (Y/N): {RESET}").upper()
        if play_again != 'Y':
            print(f"{MAGENTA}Thanks for playing ShadowFox Hangman!{RESET}")
            break