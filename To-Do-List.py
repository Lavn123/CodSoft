class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task added: {description}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def update_task(self, task_number, new_description):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].description = new_description
            print(f"Task {task_number} updated to: {new_description}")
        else:
            print("Invalid task number.")

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_completed()
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task removed: {removed_task.description}")
        else:
            print("Invalid task number.")
def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to update: "))
            new_description = input("Enter new task description: ")
            todo_list.update_task(task_number, new_description)
        elif choice == '4':
            task_number = int(input("Enter task number to mark as completed: "))
            todo_list.complete_task(task_number)
        elif choice == '5':
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
