# Internship Technical Challenge – Command-Line To-Do App

This repository contains my submission for **Option 2 – Command-Line To-Do App** from the Internship Technical Challenge.

The To-Do App is a terminal-based task manager that allows you to add, list, mark as done, and delete tasks, all stored in a JSON file for persistence.

---

## Features

- Add new tasks
- List all tasks with index numbers
- Mark a task as done
- Delete a task
- Persistent storage in JSON format (`tasks.json`)

---

## Requirements

- Python 3.7+
- No external dependencies

---

## How to Run

1. **Navigate to the project folder:**

   - Right click on the `todo_app` folder and copy the path
   - In your terminal, type:
     ```bash
     cd <paste the copied path here>
     ```

2. **Add a task:**

   ```bash
   python todo.py add "Buy milk"
   ```

3. **List all tasks:**

   ```bash
   python todo.py list
   ```

4. **Mark a task as done:**

   ```bash
   python todo.py done 1
   ```

5. **Delete a task:**

   ```bash
   python todo.py delete 1
   ```

6. **View help menu:**
   ```bash
   python todo.py -h
   ```

---

## Quick Command Reference

| Command                     | Description                |
| --------------------------- | -------------------------- |
| `python todo.py add "Task"` | Add a new task             |
| `python todo.py list`       | List all tasks             |
| `python todo.py done N`     | Mark task number N as done |
| `python todo.py delete N`   | Delete task number N       |
| `python todo.py -h`         | Show help menu             |

---

## File Structure

```
internship-challenge/
├── todo_app/
│   └── todo.py
├── README.md
└── .gitignore
```

---

## Notes

- The `tasks.json` file will be automatically created when you add your first task.
- Tasks remain saved even after you close the program.
- The app uses `argparse` for parsing commands and `json` for data storage.
