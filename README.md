# selfbudget-cli: My very first project in Python

## How It Works

The `selfbudget-cli` program is a command-line tool designed to help users manage their personal budgets. Below is a guide on how to use the program effectively:

### 1. Launch the Program
To start the program, open your terminal or command prompt, navigate to the project directory, and run:
```bash
python selfbudget_v2.0.py
```

### 2. Main Menu
Once the program starts, you will see the following main menu:
```plaintext
MAIN MENU:
1) New budget
2) Load budget
3) Delete budget
4) Edit budget
0) Exit program
```
Choose an option by typing the corresponding number and pressing Enter.

### 3. Features
#### **1) New Budget**
- Create a new budget by:
  - Naming your budget.
  - Entering the total budget amount.
  - Defining categories and their percentages.
- The program calculates the amount allocated to each category.
- Optionally, save the budget as a `.json` file for future use.

#### **2) Load Budget**
- Load a previously saved budget by entering the file name (without the `.json` extension).
- The program will display the details of the loaded budget.

#### **3) Delete Budget**
- Delete an existing budget file by entering its name (without the `.json` extension).
- Confirm the deletion when prompted.
- The file will be permanently removed from the directory.

#### **4) Edit Budget**
*(Feature in progress)*

#### **0) Exit Program**
- Exit the program safely.

### 4. Error Handling
- If you attempt to load or delete a file that doesn’t exist, the program will notify you and allow you to try again.
- Invalid inputs are handled gracefully, and the program will prompt you to re-enter valid data.

### 5. File Management
All budgets are saved as `.json` files in the program's directory. You can back up, share, or manually manage these files as needed.

### Example Workflow
1. Start the program by running:
   ```bash
   python selfbudget_v2.0.py
   ```
2. Create a new budget by selecting option `1` and saving it as `my_budget.json`.
3. Load the saved budget later using option `2`.
4. Delete the budget when no longer needed using option `3`.
5. Exit the program by selecting option `0`.

This program is a simple yet powerful tool to help you organize and manage your personal finances directly from the command line!