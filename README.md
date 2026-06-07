# 📝 Todo List – CLI Task Manager

A command‑line todo list application built with Python. Add, view, and remove tasks with input validation.

> *“Every line of code is a step toward better healthcare.”* – NaijaCodeClinician

## ✨ Features

- ✅ Add multiple tasks at once (choose how many)
- ✅ View all pending tasks
- ✅ Remove specific tasks by number
- ✅ Input validation:
  - Non‑empty task names
  - No duplicate tasks
  - Valid numeric input for task count and removal
  - Rejects decimals and negative numbers
- ✅ Graceful exit

## 🚀 How to Run

1. **Install Python 3** (I use Termux on Android, but it works on any system).
2. Clone this repository or download `todo_list.py`.
3. Open a terminal in the project folder and run:

```bash
python todo_list.py
```
## 🛠️ Dependencies

· Python 3 (standard library only – no external packages)

## 📁 Files

· todo_list.py – main program
· validation.py – helper module for numeric input validation (reused from other projects)

## 🔮 What I’ve Learned & Next Steps

This project taught me:

· How to handle multiple user inputs (number of tasks, dynamic task entry)
· List operations (append, del, membership checks)
· Input validation for positive integers and decimals

Future improvements (when I learn more):

· Save tasks to a file (Chapter 14 – Files)
· Edit existing tasks
· Set deadlines or priorities
· Add a graphical interface with Flask (Chapter 15)

## 💬 Feedback Welcome

I’m still learning, so any suggestions, code reviews, or ideas are highly appreciated.
Feel free to open an issue or contact me via GitHub.

---

Author:``` NaijaCodeClinician```

License: MIT

---
