# Mock-Bank-Management-System


This Python application simulates a basic banking system with features for account management and transactions. It uses SQLite for data storage and pickle for file operations.

## Installation

1. Clone the repository:

2. Install dependencies if required:

3. Run the application:

## Features

- **Account Management:**
- Create new accounts with account number, name, phone number, address, and initial credit amount.
- Modify account details such as account holder name, type, and balance.
- Delete accounts from the system.

- **Transactions:**
- Perform withdrawals and deposits into accounts.
- View transaction history including withdrawal and deposit amounts.

- **Data Storage:**
- Uses SQLite to store customer details and transaction records.
- Uses pickle for file-based storage of account objects.

## Usage

Upon running `main.py`, the application displays a menu-driven interface where users can perform various operations like creating a bank account, making transactions, viewing account details, and more.

## Dependencies

- `pickle`: Used for serializing and deserializing Python objects.
- `pathlib`: Provides a platform-independent way to work with filesystem paths.

## Contributing

Contributions are welcome! Fork the repository, create a new branch, make your changes, and submit a pull request.



