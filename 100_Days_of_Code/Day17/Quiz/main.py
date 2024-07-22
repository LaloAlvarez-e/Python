#!E:\GIT\Python\100_Days_of_Code\Day17\venv\Scripts\python.exe
from question import Question
from data import question_data
import random

def main():
    print("Welcome to the Quiz Game!")
    question_bank = []
    for question in question_data:
        questionObject = Question(question["question"], question["correct_answer"], question["incorrect_answers"])
        question_bank.append(questionObject)          
    
    running = True
    while True == running: 
        score = 0
        questionNumber = 1
        questionAvailable = list(range(len(question_bank)))
        while questionAvailable: 
            questionIndex = random.choice(questionAvailable) 
            questionAvailable.remove(questionIndex)
            question = question_bank[questionIndex]
            answers = question.get_shuffle_answers()
            answers = ", ".join(answers)
            user_answer = input(f"Q.{questionNumber}: {question.text}  ({answers}) :")
            isCorrect = question.check_answer(user_answer)
            if True == isCorrect:
                score += 1
                print("You got it right!")
            else:
                print("That's wrong.")
            correctAnswers = question.get_correct_answers()
            correctString = "The correct answer was:"
            if(type(correctAnswers) == list):  
                correctAnswers = ", ".join(correctAnswers)
                correctString = "The correct answers were:"
            print(f"{correctString} {correctAnswers}")
            print(f"Your current score is {score}/{questionNumber}\n")
            questionNumber += 1
        play_again = input("Would you like to play again? (yes/no): ")
        if play_again.lower() != "yes":
            running = False

if __name__ == "__main__":
    main()