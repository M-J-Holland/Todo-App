from choice_functions import add_todos, edit_todos, show_todos, complete_todos, quit_todos, delete_todos
from welcome import welcome_messages


def main():
    welcome_messages()
    todo_app_running = True
    while todo_app_running:
        user_choice = input("\nEnter: add | edit | show | complete | delete | quit:\n>> ").lower().strip()
        match user_choice:
        # Add todos
            case "add":
                add_todos()

        # Edit todos
            case "edit":
                edit_todos()

        # Show todos
            case "show":
                show_todos()
        # Complete todos
            case 'complete':
                complete_todos()

        # Delete todos
            case "delete":
                delete_todos()

        # quit
            case "quit":
                quit_todos()
                todo_app_running = False
        # No match
            case "_":
                print(f"'{user_choice}' is not a valid option.")

if __name__=='__main__':
    main()

