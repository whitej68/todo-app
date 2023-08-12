from functions import get_todos, write_todos
import time

# date time format codes
print(time.strftime("It is %b %d, %Y %H:%M:%S"))

while True:
    user_action = input("Type add or show, edit, complete or exit:").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]      # list slicing operation

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]  list comprehension

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            todos = get_todos()

            new_todo = input("New todo:")
            todos[number - 1] = new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            write_todos(todos)
            print(f"Todo {todo_to_remove} was removed from the list")

        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye")
