import FreeSimpleGUI as sG

label = sG.Text("Enter a Todo:", text_color="white", background_color="black")
input_box = sG.Input(tooltip="Enter todo", text_color="black")
add_button = sG.Button("Add")

window = sG.Window("Todo-App", layout=[[label], [input_box, add_button]], background_color="black")
window.read()
window.close()