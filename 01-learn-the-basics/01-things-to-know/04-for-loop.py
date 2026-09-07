"""
Topic: For Loops
Roadmap: Striver A2Z DSA
Section: Learn the Basics

Demonstrates:
- Iterating over a range
- Iterating over a collection
- Using loop variables
"""


def main():
    print("Numbers from 1 to 5:")

    for number in range(1, 6):
        print(number)

    print("\nElements in a list:")

    numbers = [10, 20, 30, 40, 50]

    for number in numbers:
        print(number)


if __name__ == "__main__":
    main()