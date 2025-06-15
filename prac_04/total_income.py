def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("Enter the number of months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)} : "))
        incomes.append(income)

    display_report(incomes)


def display_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()