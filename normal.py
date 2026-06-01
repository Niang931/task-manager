from Tasks import Task, Tasks

def main():

    tasks = Tasks()
    print("add, update, delete, list, mark-progress")
    choice = input(">>:").lower()
    while choice != 'q':
        if choice == 'add':
            new_task = input("enter task description:")
            tasks.add_task(new_task)
            tasks.list_tasks()

        elif choice == 'update':
            if tasks.tasks:
                task_id = int(input("Enter task id:"))
                while not tasks.is_validate_id(task_id):
                    print("Invalid id")
                    task_id = int(input("Enter task id:"))
                task_description = input("Enter new description:")
                tasks.update_task(task_id, task_description)
                tasks.list_tasks()

            else:
                print("No tasks to be updated")

        elif choice =='delete':
            if tasks.tasks:
                id_to_delete = int(input("Enter task id to be deleted:"))
                while not tasks.is_validate_id(id_to_delete):
                    print("Invalid id")
                    id_to_delete = int(input("Enter task id to be deleted:"))
                tasks.delete_task(id_to_delete)
                tasks.list_tasks()
            else:
                print("No tasks to be deleted")

        elif choice == 'list':
            print("to-do, in-progress, done")
            list_choice = input('list by:')
            tasks.list_tasks(list_choice)

        elif choice =='mark-progress':
            id_to_mark = int(input("Enter the id to be marked:"))
            status = input("Status>>:")
            tasks.mark_progress(id_to_mark,status)
            tasks.list_tasks()

        else:
            print("invalid choice")
        print("add, update, delete, list")
        choice = input(">>:").lower()
    print("Thank you for managing the tasks")
    print(f'You have {tasks.calc_undone_tasks()} to finish')
    tasks.save_to_file()



if __name__ == '__main__':
    main()