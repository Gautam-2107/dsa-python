"""
Topic: Input and Output
Roadmap: Striver A2Z DSA
Section: Learn the Basics

Demonstrates:
- Reading input from the user
- Converting input to integers
- Producing formatted output
"""


def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print(f"Hello, {name}!")
    print(f"You are {age} years old.")


if __name__ == "__main__":
    main()