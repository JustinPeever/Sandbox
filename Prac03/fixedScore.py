"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    state = method_name(score)

    print(state)
    print(score)


def method_name(score):
    if score < 0 or score > 100:
        state = "Invalid score"
        print("Invalid score")
    elif score < 50:
        state = "Bad"
    elif score > 90:
        state = "Excellent"
    elif score > 49:
        state = "Passable"
    return state


main()