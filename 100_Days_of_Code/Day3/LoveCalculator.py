def main():
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")
    combined_name = name1 + name2
    lower_case_name = combined_name.lower()
    t = lower_case_name.count("t")
    r = lower_case_name.count("r")
    u = lower_case_name.count("u")
    e = lower_case_name.count("e")
    true = t + r + u + e
    l = lower_case_name.count("l")
    o = lower_case_name.count("o")
    v = lower_case_name.count("v")
    e = lower_case_name.count("e")
    love = l + o + v + e
    love_score = (true*10) + love
    if (love_score < 10) or (love_score > 90):
        auxiliaryMessage = ", you go together like coke and mentos."
    elif (love_score >= 40) and (love_score <= 50):
        auxiliaryMessage = ", you are alright together."
    else:
        auxiliaryMessage = "."
    
    print(f"Your score is {love_score}{auxiliaryMessage}")

if __name__ == "__main__":
    main()