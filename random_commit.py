import os
import random
import datetime
import subprocess

# Generar un cambio aleatorio
def generate_random_change():
    file_name = "random_file.txt"
    with open(file_name, "a") as file:
        file.write(f"Random change at {datetime.datetime.now()}\n")
    return file_name

# Realizar el commit
def make_commit(file_name):
    subprocess.run(["git", "add", file_name])
    commit_message = f"Random commit: {random.randint(1, 100000)}"
    subprocess.run(["git", "commit", "-m", commit_message])

if __name__ == "__main__":
    file_name = generate_random_change()
    make_commit(file_name)