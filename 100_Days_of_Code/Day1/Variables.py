def main():
    a = input()
    b = input()
    
    c = a
    a = b
    b = c
    
    print("a: " + a)
    print("b: " + b)

if __name__ == "__main__":
    main()