import random
print("Welcome To The Hangman Game!")
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# Random word generator
words = ["zest", "albatross", "lettuce", "jaguar", "breadfruit", "penguin", "radish", "falcon", "narwhal", "nectar",
"yak", "hazel", "durian", "honeydew", "tomato", "tomato", "hippopotamus", "amber", "vinegar", "garnet",
"orange", "albatross", "hippopotamus", "jalapeno", "uranium", "amber", "iguana", "xigua", "hippopotamus", "whale",
"honeycrisp", "iceberg", "watermelon", "narwhal", "whale", "hazel", "yam", "date", "whirl", "urchin",
"krypton", "sapphire", "honeycrisp", "quartz", "yeast", "wasabi", "lettuce", "narwhal", "vanilla", "gorilla",
"coconut", "uranium", "wasabi", "raspberry", "uranium", "plum", "hazel", "quinoa", "strawberry", "vinegar",
"topaz", "rhinoceros", "strawberry", "kiwi", "wasabi", "kale", "yak", "okra", "honeydew", "quartz",
"lettuce", "mango", "yak", "quartz", "eggplant", "lithium", "watermelon", "urchin", "jade", "uranium",
"udon", "grapefruit", "dolphin", "spinach", "spinach", "xenon", "orange", "zebra", "yeast", "fig",
"breadfruit", "zebra", "krypton", "quince", "zest", "okra", "moonstone", "dolphin", "udon", "hazel"]

word = words[random.randint(0, len(words)- 1 )].lower()
print(word)

# Let user have a guess
wrong_guesses = 0
dashes = ['_' for i in word]
print(' '.join(dashes))

while wrong_guesses < 6:
    if "_" not in dashes:
        print("You Won!")
        print(word)
        break
    
    indices = []
    
    user_guess = input("Guess a letter: ")
    if user_guess.lower() in word:
        for i in range(len(word)):
            if word[i] == user_guess and i not in indices:
                dashes[i] = user_guess
                indices.append(i)
        print(' '.join(dashes))
                
    else:
        print(HANGMANPICS[wrong_guesses])
        wrong_guesses += 1
        print(' '.join(dashes))


if '_' in dashes:
    print("You have lost")