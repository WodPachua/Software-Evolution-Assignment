# Task Manager

A simple command-line task manager written in Python. It lets you add, list,
complete, delete and search tasks, each with a priority level. Tasks are stored
in a local `tasks.json` file.

## Description
This project was built to practise software evolution with Git and GitHub:
incremental commits, feature branches, pull requests, issues and milestones.

## Installation
1. Make sure you have Python 3.8 or newer installed.
2. Clone the repository:
   ```
   git clone https://github.com/WodPachua/Software-Evolution-Assignment.git
   cd Software-Evolution-Assignment
   ```
3. No external libraries are required.

## Usage
Run the program:
```
python3 task_manager.py
```
Then choose an option from the menu:
- **Add task** - enter a title and a priority (low/medium/high)
- **List tasks** - see all tasks with their status
- **Complete task** - mark a task as done by its number
- **Delete task** - remove a task by its number
- **Search tasks** - find tasks by keyword

## Merge conflict resolution
While merging the two feature branches into `main` through pull requests, a merge
conflict occurred in `task_manager.py`, inside the `print_menu()` function:

- `feature-ui` had rewritten the menu with a bordered layout.
- `feature-enhancement` had added a "Search tasks" option and renumbered "Exit".

Both branches changed the same lines, so Git could not merge automatically and
marked the conflict with `<<<<<<<`, `=======` and `>>>>>>>`. I resolved it by
hand, **keeping both changes**: the bordered layout from `feature-ui` and the new
"Search tasks" option (with "Exit" as option 6) from `feature-enhancement`. After
editing the file to contain both, I ran `git add task_manager.py`, committed, and
completed the pull request. The program was then tested to confirm both work.

## Contributors
- Olara Moses (JAN24/BSE/3883U)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file.
