import random

# -------------------------------
# Fruits
# -------------------------------

FRUITS = {
    "easy": [
        "apple", "mango", "grapes", "banana",
        "orange", "guava", "papaya", "lemon"
    ],

    "medium": [
        "pineapple", "watermelon", "strawberry",
        "blueberry", "raspberry", "blackberry"
    ],

    "hard": [
        "pomegranate", "dragonfruit",
        "passionfruit", "cranberry"
    ]
}


# -------------------------------
# Animals
# -------------------------------

ANIMALS = {
    "easy": [
        "tiger", "zebra", "horse",
        "monkey", "rabbit", "camel"
    ],

    "medium": [
        "elephant", "kangaroo",
        "crocodile", "chimpanzee"
    ],

    "hard": [
        "hippopotamus",
        "rhinoceros",
        "alligator",
        "orangutan"
    ]
}


# -------------------------------
# Countries
# -------------------------------

COUNTRIES = {
    "easy": [
        "india", "china", "japan",
        "nepal", "bhutan", "france"
    ],

    "medium": [
        "germany", "australia",
        "singapore", "thailand"
    ],

    "hard": [
        "kazakhstan",
        "madagascar",
        "afghanistan",
        "switzerland"
    ]
}


# -------------------------------
# Technology
# -------------------------------

TECHNOLOGY = {
    "easy": [
        "python", "java", "mouse",
        "laptop", "server", "router"
    ],

    "medium": [
        "keyboard",
        "computer",
        "database",
        "compiler"
    ],

    "hard": [
        "programming",
        "cybersecurity",
        "virtualization",
        "microprocessor"
    ]
}


# -------------------------------
# Movies
# -------------------------------

MOVIES = {
    "easy": [
        "avatar",
        "jawan",
        "dangal",
        "bahubali"
    ],

    "medium": [
        "interstellar",
        "oppenheimer",
        "inception",
        "gladiator"
    ],

    "hard": [
        "shawshank",
        "parasite",
        "godfather",
        "whiplash"
    ]
}


# ==========================================
# All Categories
# ==========================================

CATEGORIES = {
    "1": ("Fruits", FRUITS),
    "2": ("Animals", ANIMALS),
    "3": ("Countries", COUNTRIES),
    "4": ("Technology", TECHNOLOGY),
    "5": ("Movies", MOVIES)
}


# ==========================================
# Display Categories
# ==========================================

def show_categories():

    print("\nChoose a Category\n")

    for key, value in CATEGORIES.items():
        print(f"{key}. {value[0]}")


# ==========================================
# Get Category Name
# ==========================================

def get_category(choice):

    if choice in CATEGORIES:
        return CATEGORIES[choice]

    return None


# ==========================================
# Random Word Generator
# ==========================================

def get_random_word(category_choice, difficulty):

    category = get_category(category_choice)

    if category is None:
        return None

    category_name, words = category

    if difficulty not in words:
        return None

    word = random.choice(words[difficulty])

    return word, category_name


# ==========================================
# Difficulty Attempts
# ==========================================

def get_attempts(difficulty):

    attempts = {
        "easy": 10,
        "medium": 7,
        "hard": 5
    }

    return attempts.get(difficulty, 10)


# ==========================================
# Difficulty Score
# ==========================================

def get_base_score(difficulty):

    scores = {
        "easy": 10,
        "medium": 20,
        "hard": 30
    }

    return scores.get(difficulty, 10)

