import FreeSimpleGUI as sG
font_size = 44
label = sG.Text("Enter a Todo:", text_color="white", background_color="black", font=font_size)
input_box = sG.Input(tooltip="Enter todo", text_color="black", font=font_size)
add_button = sG.Button("Add", font=font_size)

window = sG.Window("Todo-App", layout=[[label], [input_box, add_button]], background_color="black")
window.read()
window.close()