
# Quizz questions Path 
QUIZQUESTION_PATH = r"MINI PROJECTS\01_Python Fundamentals\01_Quiz APP with Score Tracking\data\questions.txt"

# Report Summary Path 
REPORT_PATH = r"MINI PROJECTS\01_Python Fundamentals\01_Quiz APP with Score Tracking\data\report_card.txt"

# Title banner display 
def showBanner():
    """
    Displays the title banner for the quiz application.
    This function is purely for UI/UX enhancement.
    """
    title = "Welcome to the Quiz Challenge!"
    print("=" * 40)
    print(title.center(40))  # centre-align title within 40 characters
    print("=" * 40)


# loading questions so it can be displayed on terminal one by one 
def load_questions():
    """
    Loads quiz questions from the text file.

    Each question block must have:
    - 1 line question text
    - 4 lines of options
    - 1 line correct answer (A/B/C/D)

    Returns:
        list of tuples -> (questionText, questionsOptions, correctAnswer)
    """
    try:
        with open(QUIZQUESTION_PATH, "r") as questionFile:
            questionsContent = questionFile.read().strip()

        if not questionsContent:
            print("Question file empty.")
            return []

        questionsBlock = questionsContent.split("\n\n")
        questions = []

        # traversing question 
        for question in questionsBlock:
            lines = question.strip().split("\n")

            # Check if all lines are present in a question 
            if len(lines) != 6:
                print("Malformed Question block detected. Skipping question.")
                continue

            questionText = lines[0]
            questionsOptions = lines[1:5]
            correctAnswer = lines[5].upper()

            # If correct answer itself is invalid, mark it as None
            # This ensures quiz logic treats it as a wrong question
            if correctAnswer not in ["A", "B", "C", "D"]:
                print("Invalid Correct answer in question File. Marking as invalid.")
                correctAnswer = None

            # using tuples to store all question data 
            questions.append((questionText, questionsOptions, correctAnswer))

        return questions

    except FileNotFoundError:
        print("Erorr : Question.txt file not found check in data folder.")
        return []


# run the quiz main logic 
def run_quiz(questions):
    """
    Runs the quiz question-by-question.

    Tracks:
    - total questions
    - attempted questions
    - correct answers
    - wrong answers

    Handles:
    - Invalid user input
    - Early exit using Ctrl+C
    """
    #total_Questions = len(questions)
    correctAnswer_count = 0
    wrongAnswer_count = 0
    attemptedQuestions = 0

    for idx, (question, options, answer) in enumerate(questions, start=1):  # unpacking tuple
        print(f"\nQ{idx}. {question}")
        for option in options:
            print(option)

        try:
            while True:
                user_choice = input("Your answer (A/B/C/D): ").strip().upper()
                if user_choice in ["A", "B", "C", "D"]:
                    break
                print("Invalid input. Please enter A, B, C, or D.")

            attemptedQuestions += 1

            # If answer from file is invalid (None), force it as wrong
            if answer is None:
                print("Wrong Answer. Question has invalid correct answer.")
                wrongAnswer_count += 1

            elif user_choice == answer:
                print("Correct Answer!")
                correctAnswer_count += 1

            else:
                print(f"Wrong Answer. Correct answer is {answer}")
                wrongAnswer_count += 1

        except KeyboardInterrupt:
            # Allows clean exit in middle of quiz
            print("\nQuiz interrupted by user.")
            break

    return attemptedQuestions, correctAnswer_count, wrongAnswer_count


# genrating reports After quiz 
def generate_reports(total_Questions, correctAnswer_count, wrongAnswer_count):
    """
    Generates a report card file after quiz completion.

    Handles:
    - Partial quiz attempts
    - Division by zero safety
    """
    if total_Questions == 0:
        print("No questions attempted. Report not generated.")
        return

    scorePercentage = (correctAnswer_count / total_Questions) * 100
    status = "Pass" if scorePercentage >= 50 else "Fail"

    with open(REPORT_PATH, "w") as file:
        file.write("QUIZ REPORT CARD\n")
        file.write("=" * 40 + "\n")
        file.write(f"Total Questions     : {total_Questions}\n")
        file.write(f"Attempted Questions : {total_Questions}\n")
        file.write(f"Correct Answers     : {correctAnswer_count}\n")
        file.write(f"Wrong Answers       : {wrongAnswer_count}\n")
        file.write(f"Final Score         : {scorePercentage:.2f}%\n")
        file.write(f"Result              : {status}\n")

    print("Report card generated successfully.")

# Main QuizApp code 
def QuizzApp():
    """
    Main controller function for the Quiz App.
    """
    showBanner()

    try:
        questions = load_questions()

        if not questions:
            print("No valid questions found. Exiting quiz.")
            return

        totalQuestions, correctAnswer, wrongAnswer = run_quiz(questions)
        generate_reports(totalQuestions, correctAnswer, wrongAnswer)

    except KeyboardInterrupt:
        print("\nExiting Cleanly!") 


QuizzApp()