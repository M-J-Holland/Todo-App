import json

FILENAME = "todos.json"

def read_todos():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def write_todos(todos_arg):
    with open(FILENAME, "w") as file:
        json.dump(todos_arg, file, indent=2)
