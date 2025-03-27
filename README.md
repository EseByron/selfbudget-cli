# selfbudget-cli: My very first project in Python.

## Introduction

The `selfbudget-cli` is a command-line tool designed to help you manage your personal budget efficiently. With this program, you can track your income, expenses, and savings, all from the comfort of your terminal.

## How to Use

### Step 1: Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/selfbudget-cli.git
    ```
2. Navigate to the project directory:
    ```bash
    cd selfbudget-cli
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Step 2: Running the Program
1. Launch the program by running:
    ```bash
    python main.py
    ```

### Step 3: Adding Income
1. Use the `add-income` command to log your income:
    ```bash
    python main.py add-income --amount 500 --source "Freelance Work"
    ```

### Step 4: Adding Expenses
1. Use the `add-expense` command to track your expenses:
    ```bash
    python main.py add-expense --amount 200 --category "Groceries"
    ```

### Step 5: Viewing Summary
1. Use the `view-summary` command to see an overview of your budget:
    ```bash
    python main.py view-summary
    ```

### Step 6: Saving Data
1. Save your budget data to a file:
    ```bash
    python main.py save --file budget_data.json
    ```

That's it! You're now ready to manage your budget with `selfbudget-cli`.