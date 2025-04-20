import FreeSimpleGUI as sG
from read_write_functions import read_todos, write_todos

label = sG.Text("Enter a Todo:", background_color="Black")
input_box = sG.Input(tooltip="Enter todo", key="todo")
add_button = sG.Button("Add")

window = sG.Window("Todo-App",
                   layout=[[label], [input_box, add_button]],
                   background_color="black", font=("Helvetica", 20))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = read_todos()
            new_todo = values['todo']
            todos.append(new_todo)
            write_todos(todos)

        case 'Show':
            pass

        case 'Edit':
            pass

        case 'Complete':
            pass

        case "Quit":
            pass


        case sG.WIN_CLOSED:
            break
window.close()
