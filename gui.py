import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
# tooltip is the text that appears when you hover over the box
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))
while True:
    # displays window on the screen
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + "\n")
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()