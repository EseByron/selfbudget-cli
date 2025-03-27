# selfbudget-cli: My very first project in Python.

## Introduction

The `selfbudget-cli` is a command-line interface (CLI) tool designed to help you manage your personal budget efficiently. Built with Python, this project is perfect for users who want a simple yet powerful way to track their income, expenses, and savings directly from the terminal.

## How It Works: Step-by-Step Guide

1. **Installation**  
    Clone the repository and navigate to the project directory:
    ```bash
    git clone https://github.com/yourusername/selfbudget-cli.git
    cd selfbudget-cli
    ```
    Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. **Setup**  
    Run the initialization command to set up your budget:
    ```bash
    python selfbudget.py init
    ```
    Follow the prompts to input your initial budget details.

3. **Adding Income**  
    To add income, use the following command:
    ```bash
    python selfbudget.py add-income --amount <amount> --source <source>
    ```
    Replace `<amount>` with the income amount and `<source>` with the income source.

4. **Adding Expenses**  
    To log an expense, use:
    ```bash
    python selfbudget.py add-expense --amount <amount> --category <category>
    ```
    Replace `<amount>` with the expense amount and `<category>` with the expense category.

5. **Viewing Summary**  
    To view your current budget summary, run:
    ```bash
    python selfbudget.py summary
    ```

6. **Exporting Data**  
    Export your budget data to a file for backup or analysis:
    ```bash
    python selfbudget.py export --format <format> --output <filename>
    ```
    Replace `<format>` with the desired file format (e.g., CSV) and `<filename>` with the output file name.

7. **Help**  
    For a list of all available commands, use:
    ```bash
    python selfbudget.py --help
    ```

With these steps, you can easily manage your budget and keep track of your financial goals using `selfbudget-cli`.