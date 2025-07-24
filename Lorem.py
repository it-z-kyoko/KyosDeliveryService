import keyboard
import time
import random

lorem_sentences = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco.",
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore.",
    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt."
]

def human_type(sentence):
    for char in sentence:
        time.sleep(random.uniform(0.05, 0.25))

        if random.random() < 0.07 and char.isalpha():
            # Type a wrong letter
            wrong_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
            keyboard.write(wrong_letter)
            time.sleep(0.2)
            keyboard.send("backspace")

        keyboard.write(char)

    keyboard.send("enter")

def main():
    print("Starting in 5 seconds. Move your cursor to the target window!")
    time.sleep(5)

    while True:
        sentence = random.choice(lorem_sentences)
        human_type(sentence)
        time.sleep(240)  # Wait 4 minutes

if __name__ == "__main__":
    main()
