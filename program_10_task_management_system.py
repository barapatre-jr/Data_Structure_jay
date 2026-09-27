from collections import deque

# Queue for task scheduling (FIFO)
task_queue = deque()

# Stack for undo operations (LIFO)
undo_stack = []


def add_task(task):
    task_queue.append(task)
    print(f"Task added: {task}")


def process_task():
    if task_queue:
        task = task_queue.popleft()
        undo_stack.append(task)
        print(f"Processed task: {task}")
    else:
        print("No tasks to process")


def undo_task():
    if undo_stack:
        task = undo_stack.pop()
        print(f"Undo last processed task: {task}")
    else:
        print("Nothing to undo")


def show_tasks():
    print("Pending Tasks (Queue):", list(task_queue))
    print("Undo Stack:", undo_stack)


# Menu Driven Program
while True:
    print("\n========== TASK MANAGER ==========")
    print("1. Add Task")
    print("2. Process Task")
    print("3. Undo Task")
    print("4. Show Tasks")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        process_task()

    elif choice == "3":
        undo_task()

    elif choice == "4":
        show_tasks()

    elif choice == "5":
        print("Exiting system...")
        break

    else:
        print("Invalid choice")