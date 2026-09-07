"""
Topic: Switch Case
Roadmap: Striver A2Z DSA
Section: Learn the Basics

Python uses match-case for switch-like behavior.
"""


def main():
    day = int(input("Enter a number (1-7): "))

    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid day")


if __name__ == "__main__":
    main()