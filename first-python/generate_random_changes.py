import random
import string
import os

def commit_and_push():
    """Adds, commits, and pushes changes to a Git repository."""
    try:
        os.system("git add .")
        os.system('git commit -m "some changes"')
        os.system("git push")
        print("Changes committed and pushed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def generate_random_string(length=10):
    """Generate a random string of specified length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def append_random_string_to_file(filename="random_changes.txt"):
    """Append a random string to the specified file."""
    random_string = generate_random_string()
    with open(filename, "a") as file:
        file.write(random_string + "\n")
    print(f"Appended '{random_string}' to '{filename}'")

if __name__ == "__main__":
    append_random_string_to_file()
    commit_and_push()