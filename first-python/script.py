import random
import string
import os
import logging


logging.basicConfig(filename='script.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def commit_and_push():
    """Adds, commits, and pushes changes to a Git repository."""
    try:
        os.system("git add .")
        logging.info("git add . executed")
        os.system('git commit -m "Automated changes"')
        logging.info("git commit -m 'Automated changes' executed")
        os.system("git push")
        logging.info("git push executed")
        print("Changes committed and pushed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}")


def generate_random_string(length=50):
    """Generate a random string of specified length."""
    characters = string.ascii_letters + string.digits + " "
    return ''.join(random.choice(characters) for _ in range(length))

def update_readme():
    """Update the README.md file with random content."""
    content = f"### Update\n{generate_random_string()}\n"
    with open("README.md", "a") as file:
        file.write(content)
    print(f"Updated README.md with:\n{content}")

def create_random_file():
    """Create a random file with random content."""
    filename = f"file_{generate_random_string(8)}.txt"
    content = generate_random_string(100)
    with open(filename, "w") as file:
        file.write(content)
    print(f"Created file '{filename}' with random content.")
    return filename

def delete_random_file():
    """Delete a random file from the current directory."""
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(".txt")]
    if files:
        file_to_delete = random.choice(files)
        os.remove(file_to_delete)
        print(f"Deleted file '{file_to_delete}'")
    else:
        print("No files available to delete.")

if __name__ == "__main__":
    logging.info("Script started")
    update_readme()
    if random.choice([True, False]):
        create_random_file()
    else:
        delete_random_file()
    os.system("git add .")  # Ensure changes are staged
    commit_messages = [
        "Add some documentation",
        "Delete unused files",
        "Updated script",
        "Refactor code for better readability",
        "Fix minor bugs",
        "Improve performance",
        "Update dependencies",
        "Add new feature",
        "Remove deprecated functionality",
        "Enhance error handling"
    ]
    
    commit_message = random.choice(commit_messages)
    os.system(f'git commit -m "{commit_message}"')
    os.system("git push")
    print(f"Changes committed and pushed with message: '{commit_message}'")
    logging.info(f"Changes committed and pushed with message: '{commit_message}'")
    logging.info("Script finished")