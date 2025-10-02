#!C:\git\Python\Datacamp\Introduction_to_functions_in_python\venv\Scripts\python.exe


# -*- coding: utf-8 -*-
""" 
Created on Mon Jun  3 11:20:28 2019

"""


from pyparsing import nums


def main():
    nums = (3, 4, 6)
    print(nums)
    print(type(nums))
    
    (num1, num2, num3) = nums

    even_nums = (2, num2, num3)
    print(even_nums)


if __name__ == "__main__":
    main()

