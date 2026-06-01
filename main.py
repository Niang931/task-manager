import argparse
from Tasks import Task, Tasks
import json
import datetime
FILENAME = 'test.json'

class TasksCLI:
    def __init__(self):
        self.tasks = Tasks()
        self.load_tasks()

    def add(self, args):
        self.tasks.add_task(args.description)
        for task in self.tasks.tasks:
            print(task)
        self.tasks.save_to_file()

    def update(self, args):
        self.tasks.update_task(args.task_id, args.description)
        self.tasks.save_to_file()

    def delete(self, args):
        self.tasks.delete_task(args.task_id)
        self.tasks.save_to_file()

    def list(self, args):
        self.tasks.list_tasks(args.status)

    def load_tasks(self):
        try:
            with open(FILENAME, 'r') as f:
                data = json.load(f)

                for item in data:
                    task = Task(item['task_id'], item['description'],
                                item['status'],
                                datetime.datetime.fromisoformat(item["createdAt"]),
                                datetime.datetime.fromisoformat(item["updatedAt"]))
                    self.tasks.tasks.append(task)
        except FileNotFoundError:
            pass



cli = TasksCLI()
parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(dest='command', required=True)

add_parser = subparser.add_parser('add')
add_parser.add_argument('description')
add_parser.set_defaults(func=cli.add)

update_parser = subparser.add_parser('update')
update_parser.add_argument('task_id', type=int)
update_parser.add_argument('description')
update_parser.set_defaults(func=cli.update)

delete_parser = subparser.add_parser('delete')
delete_parser.add_argument('task_id', type=int)
delete_parser.set_defaults(func=cli.delete)

list_parser = subparser.add_parser('list')
list_parser.add_argument('--status')
list_parser.set_defaults(func=cli.list)

args = parser.parse_args()
args.func(args)



