import json
import argparse
from datetime import datetime
from pathlib import Path

TASK_FILE = Path('tasks.json')

# Load Tasks From Json File
def load_tasks():
    if not TASK_FILE.exists():
        return []
    with open(TASK_FILE,'r') as f:
        return json.load(f)

# Save Task To Json File
def save_tasks(tasks):
    with open(TASK_FILE,'w') as f:
        json.dump(tasks,f,indent = 4)

# Adding A New Task
def add_task(title):
    tasks = load_tasks()
    new_task = {
        "title":title,
        "done": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added:{title}")

# List All Tasks 
def list_tasks():
    tasks = load_tasks()
    if not tasks: 
        print("No Tasks Found")
        return
    for i, task in enumerate(tasks):
        status = "[X]" if task["done"] else "[ ]"
        print(f"{i+1}. {task["title"]} {status}")

# Mark Task as done

def mark_done(index):
    tasks = load_tasks()
    try:
        tasks[index-1]["done"] = True
        save_tasks(tasks)
        print(f"Task #{index}. {tasks[index-1]["title"]} Marked as done.")
    except IndexError:
        print("The task number is not valid. Type list to view tasks")

# Deleting A Task

def delete_task(index):
    tasks = load_tasks()   
    try:
        index = int(index)
        deleted = tasks.pop(index-1)
        save_tasks(tasks)
        print(f"Task #{index} {deleted["title"]} was deleted.")
    except IndexError:
        print("The task number is not valid. Type list to view tasks")
    except Exception as e:
        print(f"An unexpected error occurred: {e} Type -h for help")

# CLI FUNCTIONALITY

def main():
    parser = argparse.ArgumentParser(description="Command-Line To-Do App")
    subparsers = parser.add_subparsers(dest="command")

    #Add Task Command
    add_parser = subparsers.add_parser("add", help = "Add a new task")
    add_parser.add_argument("title", type=str, help = "Task title")

    # List Command
    subparsers.add_parser("list", help = "List all tasks")

    # Mark Done Command
    done_parser = subparsers.add_parser("done", help = "Mark a task as done")
    done_parser.add_argument("index" , type = int, help = "Task number")

    # Delete Command  
    delete_parser = subparsers.add_parser("delete", help = "Delete a task")
    delete_parser.add_argument("index", help = "Task number")

    args = parser.parse_args()

    match(args.command):
        case "add":
            add_task(args.title)
        case "list":
            list_tasks()
        case "done":
            mark_done(args.index)
        case "delete":
            delete_task(args.index)
        case _:
            parser.print_help()



if __name__ == "__main__":
    main()


