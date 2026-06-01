import datetime
import json

FILENAME = 'test.json'

class Task:
    """A task object with all attributes"""
    def __init__(self, task_id, description, status='to-do', createdAt=datetime.datetime.now(), updatedAt=datetime.datetime.now()):
        self.task_id = task_id
        self.description = description
        self.status = status
        self.createdAt =createdAt
        self.updatedAt = updatedAt

    def to_dict(self):
        return {
            'task_id':self.task_id,
            'description':self.description,
            'status':self.status,
            'createdAt':self.createdAt.isoformat(),
            'updatedAt':self.updatedAt.isoformat()
        }

    def __repr__(self):
        return (
            f"Task(id={self.task_id}, "
            f"description='{self.description}', "
            f"status='{self.status}')"
        )



class Tasks:
    """A collection of tasks"""
    def __init__(self):
        self.tasks = []

    def list_tasks(self, status=None):
        if status:
            tasks_list = [task for task in self.tasks
                          if task.status == status]
            for task in tasks_list:
                print(task.task_id, task.description)
        else:
            for task in self.tasks:
                print(task.task_id, task.description)

    def add_task(self, description):
        if not self.tasks:
            task_id = 1
        else:
            task_id = len(self.tasks) + 1
        new_task = Task(task_id, description)
        self.tasks.append(new_task)

    def update_task(self, task_id, description):
        for task in self.tasks:
            if task.task_id == task_id:
                task.description = description
                task.updatedAt = datetime.datetime.now()

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)

    def mark_progress(self, task_id, status):
        if self.tasks:
            for task in self.tasks:
                if task.task_id == task_id:
                    task.status = status

    def save_to_file(self):
        with open(FILENAME, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def is_validate_id(self, task_id):
        return task_id in [task.task_id for task in self.tasks]

    def calc_undone_tasks(self):
        return len([task for task in self.tasks if task.status != 'done'])


