import random

class Question:
    def __init__(self, text, correct_answers, incorrect_answers):
        self.text = text
        self.correct_answers = correct_answers
        self.incorrect_answers = incorrect_answers

    def check_answer(self, answer):
        returnError = False
        if(type(self.correct_answers) == list):
            for correct_answer in self.correct_answers:
                if(correct_answer == answer):
                    returnError = True
        elif(answer == self.correct_answers):
            returnError = True   
        return returnError
    
    
    def get_incorrect_answers(self):
        return self.incorrect_answers
    
    def get_correct_answers(self):
        return self.correct_answers
    
    def get_shuffle_answers(self):
        answers = []
        if(type(self.correct_answers) == list):
            answers = self.correct_answers
        else:
            answers = [self.correct_answers]
        if(type(self.incorrect_answers) == list):
            answers += self.incorrect_answers
        else:
            answers.append([self.incorrect_answers])  
        random.shuffle(answers)
        return answers
    
    def get_answers(self):
        answers = self.correct_answers
        answers.append(self.incorrect_answers)
        return answers