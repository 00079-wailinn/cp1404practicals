import csv
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display all guitars in the list."""
    print("Guitars:")
    for guitar in guitars:
        print(guitar)


def add_guitar():
    """Prompt user to add a new guitar and return it, or None if no name is entered."""
    name = input("Enter guitar name: ")
    if not name:
        return None  # Return None to indicate no more guitars to add

    year = int(input("Enter year: "))
    cost = float(input("Enter cost: "))
    return Guitar(name, year, cost)


def save_guitars(filename, guitars):
    """Save all guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    guitars = load_guitars(FILENAME)
    guitars.sort()  # Sort guitars by year using __lt__ method
    display_guitars(guitars)

    # Add new guitars from user input
    print("\nAdd a new guitar (leave name empty to finish):")
    new_guitar = add_guitar()
    while new_guitar is not None:
        guitars.append(new_guitar)
        new_guitar = add_guitar()

    # Save all guitars back to file
    save_guitars(FILENAME, guitars)
    print("\nGuitars have been saved to", FILENAME)


if __name__ == "__main__":
    main()