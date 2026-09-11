# cli_tool.py

import argparse
from lib.models import Task, User
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Global dictionary to store users and their tasks
users = {}

def add_task(args):
    user_name = args.user
    title = args.title
    
    if user_name not in users:
        users[user_name] = User(user_name)
    
    user = users[user_name]
    task = Task(title)
    user.add_task(task)

def complete_task(args):
    user_name = args.user
    title = args.title
    
    if user_name not in users:
        print(f"User '{user_name}' not found.")
        return
    
    user = users[user_name]
    task = user.get_task_by_title(title)
    
    if task:
        task.complete()
    else:
        print(f"Task '{title}' not found for user '{user_name}'.")

# CLI entry point
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    # Subparser for adding tasks
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    # Subparser for completing tasks
    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
