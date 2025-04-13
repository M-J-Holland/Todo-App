from read_write_functions import read_todos, write_todos

def add_todos():
    todo = input("Enter your todo: ")
    todos = read_todos()
    todos.append({"task": todo, "completed": False})
    write_todos(todos)
    print(f"Todo {todo} has been added")


def show_todos():
    try:
        todos = read_todos()
        if not todos:
            print("No todos to show")

        todo_view_choice = input("Would you like to see all | completed | incomplete?\n>> ").strip().lower()
        for index, todo in enumerate(todos, start=1):
            todo_status = "✅" if todo["completed"] else "❌"
            if todo_view_choice == "all":
                print(f"{index} - {todo['task']} [{todo_status}]")
            elif todo_view_choice == 'completed':
                if todo['completed']:
                    print(f"{index} - {todo['task']} [{todo_status}]")
            elif todo_view_choice == 'incomplete':
                if not todo['completed']:
                    print(f"{index} - {todo['task']} [{todo_status}]")
            else:
                print("That is not a valid choice.")
    except ValueError:
        print("No Value")


def edit_todos():
    try:
        todo_to_edit = int(input("What number todo would you like to edit?\n>> ")) - 1
        todos = read_todos()
        old_todo = todos[todo_to_edit]["task"]
        new_todo = input("Enter your new todo:\n>> ")
        todos[todo_to_edit]['task'] = new_todo
        write_todos(todos)
        print(f"Todo '{old_todo}' has been changed to '{new_todo}'")
    except IndexError:
        print("That is not a valid number. Try again.")
    except ValueError:
        print("That is not a valid number. Try again.")


def complete_todos():
    todos = read_todos()
    todo_to_complete = int(input("Enter the number for the todo you would like to complete: ")) - 1
    try:
        todos[todo_to_complete]['completed'] = True

        write_todos(todos)
        print(f"Todo '{todos[todo_to_complete]['task']}' is completed")
    except IndexError:
        print("That is not a valid number. Try again.")
    except ValueError:
        print("That is not a valid number. Try again.")


def delete_todos():
    try:
        todos = read_todos()
        for index, todo in enumerate(todos, start=1):
            todo_status = "✅" if todo["completed"] else "❌"
            print(f"{index} - {todo['task']} [{todo_status}]")
        todo_to_delete = int(input("Enter the number of the todo you want to delete:\n>> ")) - 1
        deleted = todos.pop(todo_to_delete)
        write_todos(todos)
        print(f"Todo '{deleted['task']}' has been deleted.")
    except IndexError:
        print("That number doesn't exist.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def quit_todos():
    print("Your todos have been saved. \nGoodbye.")


