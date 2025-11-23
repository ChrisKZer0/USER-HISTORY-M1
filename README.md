This repository contains the work developed over three consecutive weeks, where a simple idea gradually evolved into a structured and functional inventory system in Python. 
Each week introduced new concepts and expanded the project from basic input handling to modular architecture and file persistence.

Week 1 – Introduction, Variables & User Input

File: inventory.py

The first week focused on the basics of Python.
The program requested the name and price of a product using input(), stored the data in variables, validated the input, and displayed a simple output message.
This served as an introduction to user input, data types, and basic logic.



Week 2 – Control Flow, Lists & Interactive Menu

File: inventory2.py

In the second week, the simple script evolved into a small interactive inventory system.
This version included:

1. An interactive menu using loops and conditionals
2. A list of product dictionaries
3. Input validation
4. Options to add products, list them, and calculate statistics

This week introduced the foundations of a functional application: user interaction, control structures, and basic data management.



Week 3 – External Files, Modular Structure & Persistence

Week 3 reorganized the project into a real modular application.
Files:

1. app.py – main application and menu
2. services.py – inventory operations (add, list, calculate, etc.)
3. archives.py – handles reading/writing to CSV
4. inventory.csv – data persistence file
5. flowchart.png – visual diagram of program workflow

The logic was separated into different files, allowing cleaner and scalable code.
A CSV file was added to store products permanently, so the inventory loads and saves automatically.
A flowchart was created to clearly describe the full program flow from start to exit, ensuring all components interact correctly.

Lika a summary, across these three weeks, the project progressed from a basic input script to a structured Python application with modularity, validation, persistence, and clear architecture. 
This repository reflects that step-by-step evolution and demonstrates the application of core programming fundamentals.
