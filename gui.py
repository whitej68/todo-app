import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
# tooltip is the text that appears when you hover over the box
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To-do App', layout=[[label], [input_box, add_button]])

# displays window on the screen
window.read()
window.close()