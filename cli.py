import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("The time is below:")
print("It is", now)

while True:

    user_action = input("Enter an action: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_toremove = todos[index].strip('\n')
            todos.pop(index)

            message = f"Todo {todo_toremove} was removed from the list."
            print(message)

            functions.get_todos()

        except IndexError:
            print("No item with corresponding index number")
        except ValueError:
            print("Please enter todo number to complete")

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Bye!")
