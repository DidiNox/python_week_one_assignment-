import random

# List of programming and Python jokes
jokes = [
    "Why do programmers prefer dark mode? Because the light attracts bugs! 🐛", 
    "How does a Java developer fix a broken code? They call System.out.println('debugging...'); 🖥️🔍", 
    "Why do Python programmers prefer snakes? Because they love using 'import this' 🐍", 
    "Why did the C# developer bring a ladder to work? Because they wanted to work with higher-order functions!", 
    "Why did the Python programmer break up with his partner? Because they couldn’t 'tuple' together anymore.", 
    "How do you comfort a JavaScript bug? You console it! 🖥️", 
    "Why was the JavaScript developer sad? Because he didn’t know how to 'null' his feelings. 💔", 
    "What’s a programmer's favorite hangout place? The Foo Bar. 🍻", 
    "How many JavaScript developers does it take to change a light bulb? None. They just setTimeout() the bulb change until it’s too late. 💡⏳", 
    "Why do programmers hate nature? It has too many bugs. 🌳", 
    "C++ is a lot like being in a relationship... You spend hours writing code, only to realize you forgot to define a constructor. 💔💻", 
    "What did the Python say when it encountered a syntax error? 'Oh no, an exception!' 🐍💥", 
    "Why did the Python developer break up with the JavaScript developer? Because they were tired of dealing with callbacks. 💔📞", 
    "Why did the PHP developer go to therapy? They had too many unresolved issues. 🛋️💬",
    "Why was the developer's code like a good joke? Because it had no bugs and everyone understood it! 😄", 
    "Why do C++ programmers have great parties? Because they know how to handle exceptions! 🥳", 
    "C# and Java walk into a bar... The bartender says, 'Sorry, we don't serve your type'. 🍻🚫" , 
    "Why do Java developers wear glasses? Because they don’t see sharp. 👓", 
    "Why do SQL developers never get lost? Because they always know how to join the right tables. 🧭", 
    "How do C programmers fix a broken program? They #include a 'solution.h' file. 🔧"
]

def tell_joke():
    # Select a random joke from the list
    joke = random.choice(jokes)
    print(joke)

def main():
    print("Welcome to the Python Programming Joke Machine! 🎉")
    tell_joke()

if __name__ == "__main__":
    main()
