# ✅ Terminal To-Do List Manager

A minimalist, interactive, and colorful terminal-based To-Do List manager built with Python and SQLite.

---

## 📦 Features

- 📝 Add, update, delete, and mark tasks as completed
- 💾 Tasks stored persistently in an SQLite database
- 🌈 Stylish terminal interface with `pyfiglet`, `termcolor`, and `emoji`
- 📂 Detects and operates within a fixed app directory (`To Do List/`)
- 🧠 Intelligent task ID handling and auto-increment

---

## 🛠️ Installation

1. Clone or download this repo
2. Install the required packages:

```bash
pip install pyfiglet termcolor emoji
```

> SQLite is part of Python’s standard library (no need to install separately).

---

## 🚀 Usage

```bash
python "To Do List.py"
```

You'll see a menu like this:

```
1-Show Tasks
2-Add Task
3-Mark As Completed
4-Update Task
5-Delete Task
6-Exit
```

### ✅ Supported Options (Flexible Input)
- Accepts full words or initials (e.g., `Add`, `A`, `2`)
- Displays tasks with emojis for status
- Automatically creates `data.db` if not found

---

## 📁 Database

The SQLite file `data.db` will be automatically created inside the `To Do List` folder. It contains a `Tasks` table with:

- `id` (integer, unique)
- `task` (string)
- `status` (boolean: True = done, False = not done)

---

## 📌 Notes

- Make sure the folder name is exactly `To Do List` for path detection to work.
- For `.exe` packaging, `get_path()` supports both script and frozen executables.

---

## 👨‍💻 Author

**BlueEye** – crafting terminal tools with style 🧠

---

## 📃 License

MIT License. See [LICENSE](LICENSE) for details.