"""
Topic: If-Else Statements
Roadmap: Striver A2Z DSA
Section: Learn the Basics

Demonstrates:
- Conditional statements
- Comparison operators
- Multiple conditions
"""


def main():
    number = int(input("Enter a number: "))

    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")


if __name__ == "__main__":
    main()