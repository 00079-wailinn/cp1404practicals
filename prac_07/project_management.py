import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"


def load_projects(filename=DEFAULT_FILENAME):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip header
        for line in file:
            name, start_date, priority, cost, completion = line.strip().split('\t')
            projects.append(Project(name, start_date, priority, completion, cost))
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost\tCompletion\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t${project.cost:.2f}\t{project.completion_percentage}\n")
    print(f"Projects saved to {filename}")


def display_projects(projects):
    """Display incomplete and complete projects separately, sorted by priority."""
    incomplete_projects = sorted([p for p in projects if not p.is_complete()])
    complete_projects = sorted([p for p in projects if p.is_complete()])
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("\nCompleted projects:")
    for project in complete_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, date_string):
    """Filter projects that start after a given date."""
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if p.start_date >= date]
    print(f"Projects starting after {date.strftime('%d/%m/%Y')}:")
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(f"  {project}")


def add_new_project():
    """Prompt user to add a new project and return it."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    return Project(name, start_date, priority, completion, cost)


def update_project(projects):
    """Choose and update a project’s completion or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    completion = input("New completion percentage (leave blank to keep current): ")
    priority = input("New priority (leave blank to keep current): ")
    project.update(completion or project.completion_percentage, priority or project.priority)


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    running = True  # Loop control variable

    while running:
        print(
            "\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_string)
        elif choice == 'a':
            projects.append(add_new_project())
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? (y/n): ").lower()
            if save_choice == 'y':
                save_projects(DEFAULT_FILENAME, projects)
            print("Thank you for using custom-built project management software.")
            running = False  # Stop the loop
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()