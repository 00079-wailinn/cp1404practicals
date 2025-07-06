"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""

"""
CP1404 Practical - Suggested Solution
Email to name dictionary
"""


def main():
    """Create dictionary of emails-to-names."""
    eeejfefiee = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract expected name from email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()

"Prac 5 code review request"
def load_movies(filename):
    """Load movies from a CSV file into a list of lists"""
    movies = []
    with open(filename, "r", newline='') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            title = row[0]
            year = int(row[1])
            category = row[2]
            status = row[3]
            movies.append([title, year, category, status])
    return movies
def save_movies(filename,movies):
    """Save movies to CSV file"""
    with open(filename, "w",newline='') as out_file:
        writer = csv.writer(out_file)
        for movie in movies:
            writer.writerow([movie[0], movie[1], movie[2], movie[3]])

def print_menu():
    """Display menu"""
    print("\nMenu:\nD - Display movies\nA - Add new movie\nW - Watch a movie\nQ - Quit")

def display_movies(movies):
    """Display movies sorted by year, title"""
    movies_sorted = sorted(movies,key=lambda m: (m[1],m[0]))
    count_watched = 0
    count_unwatched = 0
    for i, movie in enumerate(movies_sorted,1):
        marker = "*" if movie[3] == UNWATCHED else " "
        print(f"{i}. {marker} {movie[0]:40} - {movie[1]:4} 9{movie[2]})")
        if movie[3] == WATCHED:
            count_watched += 1
        else:
            count_unwatched += 1
    print(f"{count_watched} movies watched. {count_unwatched} movies still to watch.")

def add_movie(movies):
    """Add new movie to the list"""
    title = get_non_blank_input("Title: ")
    year = get_positive_integer("Year: ")
    print("Categories available:",", ".join(VALID_CATHGORIES))
    category = input("Category: ").strip()
    if not category:
        print("Input can not be blank")
        category = "Other"
    elif category.title() not in VALID_CATEGORIES:
        print("Invalid category; using Other")
        category = "Other"
    else:
        category = category.title()
    new_movie = [title,year,category,UNWATCHED]
    movies.append(new_movie)
    print(f"{title} ({category} from {year}) added to movie list")

def watch_movie(movies):
    """Mark a movie as watched"""
    unwatched_movies = [movie for movie in movies if movie[3] == UNWATCHED]
    if not unwatched_movies:
        print("No more movies to watch!")
        return
    display_movies(movies)
    while True:
        try:
            choice = input("Enter the movie number to mark watched:\n>>> ")
            movie_number = int(choice)
            if movie_number < 1:
                print