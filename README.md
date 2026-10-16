# Week 7 Assignment: Shopping List Manager

This repository contains my Python list practice programs.

- `list_warmup.py` — demonstrates list indexes, `.append()`, `.remove()`, and `len()`.
- `shopping_list.py` — an interactive menu for adding, removing, and showing shopping items safely.
- `list_report.py` — prints a numbered list, counts names longer than four characters, and finds the longest name.
- `screenshots/` — output examples for the three programs.

Checking whether an item is in the list before calling `.remove()` is safer because `.remove()` raises a `ValueError` if the item is missing. Using `in` lets the program show a helpful message instead of stopping with an error. This keeps the shopping list manager running even when a user tries to remove something that is not there.
