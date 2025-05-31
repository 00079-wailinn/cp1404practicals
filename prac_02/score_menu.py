def main():
    SMALL_NUM = 0
    HIGH_NUM = 100
    score = get_valid_score(SMALL_NUM, HIGH_NUM)
    choice = input("Enter choice: ").upper()

    while choice != "Q":
        if choice == "P":
            result = check_score(score)
            print(f"{score} is {result}. ")
        elif choice == "S":
            print_asterisks(score)
        else:
            print("Invalid option.")

        choice = input("Enter choice: ").upper()
    print("farewell.")


def show_menu():
    menu = """(P)rint result
(S)how stars
(Q)uit"""
    print(menu)


def get_valid_score(small_num, high_num):
    score = int(input("Enter your score: "))
    while score < small_num or score > high_num:
        print("Invalid score.")
        score = int(input("Enter your score: "))
    show_menu()
    return score


def print_asterisks(score):
    print('*' * score)


def check_score(score):
    if score >= 90:
        text = 'Excellent'
    elif score >= 50:
        text = 'Passable'
    else:
        text = 'Bad'
    return text


main()