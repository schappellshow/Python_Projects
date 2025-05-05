todo_list = []

while True:
  print("Options:")
  print("1) Add Task")
  print("2) Remove Task")
  print("3) Show Task List")
  print("4) Quit")

  choice = input()
  if choice == "1":
    new_task = input("Enter the task: ")
    todo_list.append(new_task)
    print("Adding task")
    print(f"{new_task} successfully added!")

  elif choice == "2":
    if len(todo_list) == 0:
      print("Your ToDo list is empty")
    else:
      todo_list.pop()
    
  elif choice == "3":
    if len(todo_list) == 0:
      print("Your ToDo list is empty.")
    else:
      index = 1
      for task in todo_list:
        print(f"{index}. {task}")
        index += 1
    
  elif choice == "4":
    print("Quitting")
    break
