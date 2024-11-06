def ask_question(question, options, correct_answer_index):
    """
    Function to ask a single multiple-choice question
    :param question: The question to ask
    :param options: A list of possible answers
    :param correct_answer_index: The index of the correct answer in the options list
    :return: True if the user's answer is correct, False otherwise
    """
    print(f"\n{question}")
    for idx, option in enumerate(options, start=1):
        print(f"Option {idx}. {option}")
    
    # Get the user's answer
    try:
        user_answer = int(input("Please input your answer (1-4): "))
        if user_answer == correct_answer_index + 1:
            print("Correct!") # Prints correct and returns True if user selects the right option.
            return True
        else:
            print(f"Wrong! The correct answer is: Option {options[correct_answer_index]}")
            return False    # Returns False and prints correct option if user selects the wrong answer.
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")
        return False

def play_quiz():
    questions = [
        {
            "question": "What is the output of the following code: print(2 ** 3)?",
            "options": ["6", "8", "3", "5"],
            "correct_answer_index": 1
        }, 
        {
            "question": "What is the output of the following code: print(10 * 3)?",
            "options": ["20", "33", "30", "13"],
            "correct_answer_index": 2
        }, 
        {
            "question": "What does the `len()` function do in Python?",
            "options": ["Returns the length of an object", "Converts a string to lowercase", "Generates a random number", "None of the above"],
            "correct_answer_index": 0
        }, 
        {
            "question": "What is the capital of Nigeria?",
            "options": ["Lagos", "Kaduna", "Abuja", "Ogun"],
            "correct_answer_index": 2
        }, 
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "Berlin", "Madrid", "Rome"],
            "correct_answer_index": 0
        }, 
        {
            "question": "What is the output of the following code: print(12 % 5)?",
            "options": ["2", "1", "0", "5"],
            "correct_answer_index": 0
        }, 
        {
            "question": "What is the output of the following code: print(12 / 5)?",
            "options": ["2.3", "2.40", "2", "2.13"],
            "correct_answer_index": 1
        }, 
        {
            "question": "What is the output of the following code: print(12 // 5)?",
            "options": ["2.40", "1.2", "2", "2.3"],
            "correct_answer_index": 2
        }, 
        {
            "question": "What does the amperstand '&' symbol mean in programming languages (Python)?",
            "options": ["Bitwise OR", "Bitwise AND", "Bitwise NOT", " None of the above"],
            "correct_answer_index": 1
        }, 
        {
            "question": "What does '|' symbol mean in programming languages (Python)?",
            "options": ["Bitwise OR", "Bitwise AND", "Bitwise NOT", " None of the above"],
            "correct_answer_index": 0
        }
    ]
    
    score = 0

    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_answer_index"]):
            score += 1
    
    print(f"\nYour final score is {score}/{len(questions)}.")
    
def main():
    while True:
        print("\nWelcome to the Quiz!")
        play_quiz()
        
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
