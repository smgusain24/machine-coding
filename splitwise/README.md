# Splitwise-Style Expense Sharing Application

This project is a terminal-based Python application that replicates basic functionality of Splitwise.

## Features

- **Add Users**: Create users to participate in expenses.
- **Add Expenses**: Record expenses with customizable split options.
- **View Balances**: Display outstanding balances between users.
- **Flexible Splitting**: Supports equal, exact, and percentage-based splitting of expenses.

## Class Structure

### 1. `User` Class
   - **Purpose**: Represents a user who can pay for or participate in expenses.
   - **Attributes**:
     - `user_id`: Unique identifier for each user.
     - `name`: The user's name.
   - **Methods**:
     - `get_id()`: Returns the user ID.
     - `get_name()`: Returns the user's name.
     - `__str__()`: Provides a string representation of the user for easy display.

### 2. `Expense` Class
   - **Purpose**: Represents an expense with details on the payer, amount, participants, and split type.
   - **Attributes**:
     - `expense_id`: Unique identifier for each expense.
     - `title`: Title or description of the expense.
     - `amount`: Total amount of the expense.
     - `payer`: The `User` who paid for the expense.
     - `participants`: List of `User` objects involved in the expense.
     - `split_type`: Type of split (equal, exact, percent).
     - `split_details`: Dictionary mapping each `User` to the amount they owe, depending on the split type.
   - **Methods**:
     - `calculate_split()`: Calculates each participant’s share based on the split type and updates `split_details`.

### 3. `Balance` Class
   - **Purpose**: Manages and tracks the outstanding balance between two users.
   - **Attributes**:
     - `user1`: The `User` who is owed the amount.
     - `user2`: The `User` who owes the amount.
     - `amount_owed`: The amount that `user1` owes to `user2`.
   - **Methods**:
     - `update_balance(amount)`: Updates the balance between users based on a new expense or adjustment.
     - `get_balance_summary()`: Returns a formatted string indicating who owes whom and how much
