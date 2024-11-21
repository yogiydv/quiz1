import random

users = {}
quiz_data = {
    "DBMS": [
        {"q": "What does SQL stand for?", "o": ["Structured Query List", "Structured Query Language", "Simple Query Language", "None"], "a": "Structured Query Language"},
        {"q": "What is a primary key?", "o": ["Unique identifier", "Null value", "Duplicate value", "None"], "a": "Unique identifier"},
        {"q": "Which of these is NOT a SQL command?", "o": ["DELETE", "INSERT", "UPDATE", "LINK"], "a": "LINK"},
        {"q": "Which normal form removes multivalued dependencies?", "o": ["1NF", "2NF", "3NF", "4NF"], "a": "4NF"},
        {"q": "What does ACID stand for in DBMS?", "o": ["Atomicity, Consistency, Isolation, Durability", "Accuracy, Completeness, Isolation, Dependability", "Atomicity, Completeness, Isolation, Durability", "None"], "a": "Atomicity, Consistency, Isolation, Durability"},
    ],
    "Python": [
        {"q": "Which keyword is used to define a function in Python?", "o": ["func", "def", "function", "define"], "a": "def"},
        {"q": "How do you create a list in Python?", "o": ["[]", "{}", "()", "<>"], "a": "[]"},
        {"q": "Which library is used for data analysis?", "o": ["numpy", "pandas", "math", "os"], "a": "pandas"},
        {"q": "What is used to install packages in Python?", "o": ["pip", "npm", "brew", "apt"], "a": "pip"},
        {"q": "Which function converts a string to an integer?", "o": ["str()", "int()", "float()", "convert()"], "a": "int()"},
    ],
    "DSA": [
        {"q": "Which data structure uses FIFO?", "o": ["Queue", "Stack", "Array", "Tree"], "a": "Queue"},
        {"q": "Which algorithm is used for sorting?", "o": ["Merge Sort", "Binary Search", "DFS", "BFS"], "a": "Merge Sort"},
        {"q": "Which data structure is a LIFO?", "o": ["Queue", "Stack", "Array", "Graph"], "a": "Stack"},
        {"q": "What is the time complexity of binary search?", "o": ["O(1)", "O(log n)", "O(n)", "O(n^2)"], "a": "O(log n)"},
        {"q": "Which data structure is used in BFS?", "o": ["Queue", "Stack", "Heap", "Graph"], "a": "Queue"},
    ],
}

def register():
    name = input("Enter a username: ")
    if name in users:
        print("User already exists!")
        return False
    pwd = input("Enter a password: ")
    users[name] = pwd
    print("Registration successful!")
    return True

def login():
    name = input("Enter your username: ")
    pwd = input("Enter your password: ")
    if users.get(name) == pwd:
        print("Login successful!")
        return name
    print("Invalid username or password!")
    return None

def quiz(subject, user, quiz_data):
    print(f"\nStarting {subject} quiz!")
    score = 0
    questions = random.sample(quiz_data[subject], len(quiz_data[subject]))

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['q']}")
        for idx, option in enumerate(q['o'], 1):
            print(f"{idx}. {option}")
        try:
            ans = int(input("Your answer (1/2/3/4): "))
            if q['o'][ans - 1] == q['a']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {q['a']}")
        except (ValueError, IndexError):
            print("Invalid input! Skipping this question.")

    print(f"\n{user}, your score is {score}/5.")

def main():
    print("Welcome to the Quiz Application!")
    user = None

    while not user:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            if register():
                continue
        elif choice == "2":
            user = login()
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice!")

    # Initialize attempts and subjects_taken
    attempts = 0
    subjects_taken = set()

    # Main loop to allow exactly 3 quizzes
    while attempts < 3:
        print("\nSubjects:\n1. DBMS\n2. Python\n3. DSA")
        choice = input("Choose a subject (1-3): ").strip()

        if choice == "1" and "DBMS" not in subjects_taken:
            quiz("DBMS", user, quiz_data)
            subjects_taken.add("DBMS")
            attempts += 1
        elif choice == "2" and "Python" not in subjects_taken:
            quiz("Python", user, quiz_data)
            subjects_taken.add("Python")
            attempts += 1
        elif choice == "3" and "DSA" not in subjects_taken:
            quiz("DSA", user, quiz_data)
            subjects_taken.add("DSA")
            attempts += 1
        else:
            if choice in ["1", "2", "3"]:
                print("You have already taken this quiz. Please choose a different subject.")
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")

    print("You have completed all 3 quizzes. Goodbye!")

if __name__ == "__main__":
    main()
