# Task Tracker CLI

A simple command-line application to track and manage your tasks using a JSON file.  
Built as part of the **roadmap.sh Task Tracker** project.

## 📌 Project Overview

Task Tracker CLI is a lightweight tool that allows you to manage your to-do list directly from the terminal. You can add, update, delete, and mark tasks with different statuses. All data is stored locally in a JSON file for persistence.

This project was created to practice working with:
- Command-line arguments
- File I/O
- Basic project structure
- Error handling

## 📦 Features

- Add new tasks  
- Update existing tasks  
- Delete tasks  
- Mark tasks as `todo`, `in-progress`, or `done`  
- List all tasks  
- Filter tasks by status  
- Save tasks in a JSON file  

Each task contains:
- `id` — unique identifier  
- `description` — task description  
- `status` — `todo`, `in-progress`, or `done`  
- `createdAt` — creation timestamp  
- `updatedAt` — last update timestamp  

## 🛠 Tech Stack

- Python  
- JSON for data storage  
- Standard Python libraries only  

No extra dependencies are required.

## 🧪 How to Use

Run all commands from the project root using:

```
python main.py <command> [arguments]
```

### Add a new task

```
python main.py add "Buy groceries"
```

### Update an existing task

```
python main.py update 1 "Buy groceries and cook dinner"
```

### Delete a task by its id 

```
python main.py delete 1
```

### Mark task status

```
python main.py mark-todo 1
python main.py mark-in-progress 1
python main.py mark-done 1
```

### List tasks

List all tasks:

```
python main.py list
```

List tasks by status:

```
python main.py list todo
python main.py list in-progress
python main.py list done
```

All commands automatically update the `tasks.json` file.

## 📁 JSON Storage Format

Tasks are stored in a `tasks.json` file. Each task looks like this:

```json
{ "task_id ":{
  "id": 1,
  "description": "Buy groceries",
  "status": "todo",
  "createdAt": "2026-01-10T12:00:00Z",
  "updatedAt": "2026-01-10T12:00:00Z"
    }
}

```

The file is created automatically if it does not exist.

## 🧱 Project Structure

```
task-tracker/
├── main.py        # CLI entry point
├── tasks.json     # Stored tasks
└── README.md
```

## ❗ Error Handling

The application handles:

* Invalid commands
* Missing or invalid task IDs
* Corrupted or missing JSON files

Helpful error messages are shown in the terminal.

## 📈 What I Learned

* How to build a command-line application
* How to read and write JSON files
* How to structure a small project
* How to validate user input and handle errors

## 🚀 Future Improvements

* Add due dates and priorities
* Add an interactive mode
* Export tasks to other formats
* Add unit tests

## 🔗 Roadmap Reference

[https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)

## 📜 License

This project is licensed under the MIT License.

