studentScores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

def convert2Grade(score):
    returnCode = "Fail"
    if(type(score) == int or type(score) == float) :
        if score > 90:
            returnCode = "Outstanding"
        elif score > 80:
            returnCode = "Exceeds Expectations"
        elif score > 70:
            returnCode = "Acceptable"
    return returnCode

def convertDict2Grade(dict):
    for key in dict:
        dict[key] = convert2Grade(dict[key])
    return dict

studentGrades = {}
def main():
    studentGrades = convertDict2Grade(studentScores)
    print(studentGrades)

if __name__ == "__main__":
    main()