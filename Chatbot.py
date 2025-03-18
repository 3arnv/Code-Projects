import random
from datetime import datetime
import string
import requests


def get_weather(city):
    url = f"http://wttr.in/{city}?0"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "Could not retrieve weather information."


def get_moon():
    url = f"http://wttr.in/moon"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "Could not retrieve moon information."


def play_rock_paper_scissors(user_choice):
    choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(choices)

    if user_choice == bot_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and bot_choice == "scissors")
        or (user_choice == "scissors" and bot_choice == "paper")
        or (user_choice == "paper" and bot_choice == "rock")
    ):
        result = f"You win! I chose {bot_choice}."
    else:
        result = f"I win! I chose {bot_choice}."

    return result


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password


print("Hello! I am a simple chatbot :)")
print("What is your name?")

user_name = input("You: ")
print("Hello, " + user_name + "! Nice to meet you.")
print("")
print("I can help you with the following:")
print("- Tell you a fact")
print("- Tell you a joke")
print("- Tell you the current time")
print("- Tell you the current day")
print("- Play Rock, Paper, Scissors")
print("- Give a quote")
print("- Recommend a movie")
print("- Recommend a TV show")
print("- Recommend a song")
print("- Get the weather for a city")
print("- Get the moon phase")
print("")
print("Say 'bye' or 'quit' to exit")
print("")
print("What can I help you with?")

while True:
    user_input = input("You: ").lower()

    if "bye" in user_input or "quit" in user_input:
        print("Goodbye " + user_name + "! Have a great day!")
        break
    elif "weather" in user_input:
        print("Which city would you like the weather for?")
        city = input("City: ")
        weather_info = get_weather(city)
        print(weather_info)
    elif "moon" in user_input:
        moon_info = get_moon()
        print(moon_info)
    elif "fact" in user_input:
        facts = [
            "The Chess computer Deep Blue beat Garry Kasparov in 1997",
            "Bananas are berries, but strawberries aren't",
            "Honey never spoils",
        ]
        print(random.choice(facts))
    elif "joke" in user_input:
        jokes = [
            "What's brown and sticky? A stick!",
            "Why don't skeletons fight each other? They don't have the guts.",
            "What did the grape do when he got stepped on? Nothing, he just let out a little wine.",
        ]
        print(random.choice(jokes))
    elif "time" in user_input:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        print("The current time is " + current_time)
    elif "day" in user_input:
        now = datetime.now()
        current_day = now.strftime("%d %B, %Y")
        print("Today is " + current_day)
    elif "rock" in user_input or "paper" in user_input or "scissors" in user_input:
        user_choice = user_input
        result = play_rock_paper_scissors(user_choice)
        print(result)
    elif "password" in user_input:
        print(generate_password())
    elif "quote" in user_input:
        quotes = [
            "The best time to plant a tree was 20 years ago. The second best time is now.",
            "Your time is limited, so don't waste it living someone else's life.",
            "Not everything that is faced can be changed, but nothing can be changed until it is faced.",
            "The only way to do great work is to love what you do.",
        ]
        print(random.choice(quotes))
    elif "movie" in user_input:
        movies = [
            "The Shawshank Redemption",
            "The Godfather",
            "The Dark Knight",
            "Pulp Fiction",
            "Forrest Gump",
            "Inception",
            "The Matrix",
            "Fight Club",
            "The Lord of the Rings: The Return of the King",
            "Interstellar",
        ]
        print("I recommend you watch: " + random.choice(movies))
    elif "show" in user_input:
        shows = [
            "Breaking Bad",
            "Game of Thrones",
            "Stranger Things",
            "The Office",
            "Friends",
            "The Mandalorian",
            "Sherlock",
            "The Crown",
            "Westworld",
            "The Witcher",
        ]
        print("I recommend you watch: " + random.choice(shows))
    elif "song" in user_input:
        songs = [
            "Bohemian Rhapsody by Queen",
            "Imagine by John Lennon",
            "Hotel California by Eagles",
            "Hey Jude by The Beatles",
            "Smells Like Teen Spirit by Nirvana",
            "Billie Jean by Michael Jackson",
            "Stairway to Heaven by Led Zeppelin",
            "Like a Rolling Stone by Bob Dylan",
            "What's Going On by Marvin Gaye",
            "Sweet Child O' Mine by Guns N' Roses",
        ]
        print("I recommend you listen to: " + random.choice(songs))
    else:
        print("I'm sorry, I don't understand.")