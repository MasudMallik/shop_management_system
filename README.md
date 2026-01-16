# Shop Management System — ABC Service Center

A lightweight desktop application (Tkinter) to manage repair/service workflows for a small electronics service center. The application provides a simple user interface for three user roles:

- Owner — view statistics, add/remove staff, export records, and visualize data.
- Staff — view assigned pending cases, update case status and record service details.
- Customer — lodge new service cases and check case status.

This repository contains the main GUI script `service_data.py` which connects to a MySQL database to persist data.

---

## Table of contents

- [Features](#features)
- [Demo / Screenshots](#demo--screenshots)
- [Requirements](#requirements)
- [Installation](#installation)
- [Database schema & setup](#database-schema--setup)
- [Configuration](#configuration)
- [Run the application](#run-the-application)
- [Project structure](#project-structure)
- [Security, Known issues & Improvements](#security-known-issues--improvements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- Add and remove staff members (Owner).
- Show counts of total, completed and pending jobs (Owner).
- Visualize product-type distribution and busiest weeks via Matplotlib (Owner).
- Export customer table to Excel (Owner).
- Staff login to view pending cases and mark them complete.
- Customers can lodge new cases and check status using a case id.
- Simple text-based UI using Tkinter widgets.

---

## Demo / Screenshots

(Include screenshots here if available. For this README, add them to `/docs` and reference them.)

---

## Requirements

- Python 3.8+
- MySQL server (or compatible) for persistent storage
- Python packages:
  - tkinter (usually included with standard Python)
  - mysql-connector-python
  - pandas
  - matplotlib
  - tabulate
  - openpyxl (for Excel export)

Suggested install command:

```bash
python -m pip install mysql-connector-python pandas matplotlib tabulate openpyxl
```

You may also create a `requirements.txt` with:

```
mysql-connector-python
pandas
matplotlib
tabulate
openpyxl
```

and install via:

```bash
python -m pip install -r requirements.txt
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MasudMallik/shop_management_system.git
cd shop_management_system
```

2. Install dependencies (see [Requirements](#requirements)).

3. Configure the database (see next section).

---

## Database schema & setup

The application expects a MySQL database named `abc_service` and three primary tables: `staff`, `customer`, and `details`. Example SQL to create the database and tables:

```sql
-- create database
CREATE DATABASE IF NOT EXISTS abc_service;
USE abc_service;

-- staff table
CREATE TABLE IF NOT EXISTS staff (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  guardian_name VARCHAR(255),
  contact VARCHAR(20),
  aadhar_num VARCHAR(20),
  staff_id INT NOT NULL UNIQUE,
  password VARCHAR(255)
);

-- customer table
CREATE TABLE IF NOT EXISTS customer (
  case_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  contact_no VARCHAR(20),
  email_id VARCHAR(255),
  product_type VARCHAR(100),
  product_details TEXT,
  time_of_submit DATETIME DEFAULT CURRENT_TIMESTAMP,
  status ENUM('pending','complete') DEFAULT 'pending'
);

-- details table (records of service completion)
CREATE TABLE IF NOT EXISTS details (
  id INT AUTO_INCREMENT PRIMARY KEY,
  staff_id INT,
  case_id INT,
  date_of_service DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE SET NULL,
  FOREIGN KEY (case_id) REFERENCES customer(case_id) ON DELETE CASCADE
);
```

Notes:
- The code uses `staff_id` (an integer) as the staff login identifier. Ensure `staff_id` values are unique.
- The code expects MySQL user credentials and database name as set in `service_data.py`. Update configuration before running.

---

## Configuration

Open `service_data.py` and update the following connection parameters near the top of the file:

```python
my_db = sql.connect(host="localhost", user="admin", password="root", database="abc_service")
```

Replace:
- `host` with your MySQL host (default: `localhost`)
- `user` with a MySQL user that has privileges for `abc_service`
- `password` with that user's password
- `database` with `abc_service` (or your chosen DB name)

Security recommendation: Do not keep production credentials in plain source code. Use environment variables or a separate configuration file and load them securely.

---

## Run the application

From the project root:

```bash
python service_data.py
```

The main Tkinter window will open. Use the on-screen buttons to navigate Owner / Staff / Customer flows.

Important: Some flows expect certain tables and data to exist (for example, staff entries for staff login). Create sample staff rows in the database for testing.

---

## Project structure

- service_data.py — main application (Tkinter GUI + DB interactions).
- (Add) requirements.txt — recommended dependency list (optional).
- docs/ — place screenshots, SQL dumps, or additional documentation here (optional).

---

## Security, Known issues & Improvements

Current code observations and recommended improvements:

- SQL injection risk: Several queries are constructed with f-strings (e.g. `f"DELETE from staff where staff_id={staff_to_rem}"`). Prefer parameterized queries to avoid SQL injection.
- Plaintext credentials: DB credentials are hard-coded. Use environment variables or a configuration file (.env).
- Password handling: Staff passwords are stored in plaintext. Use secure hashing (bcrypt/argon2).
- Error handling and user input validation can be improved and centralized.
- The app assumes MySQL is available. Consider bundling a lightweight SQLite option for local testing.
- UI/UX: The layout can be improved for accessibility/responsiveness.

If you plan to extend this project, consider:
- Adding unit tests
- Refactoring into modules (UI, DB, models)
- Adding packaging instructions or an installer

---

## Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repository.
2. Create a feature branch: git checkout -b feat/your-feature
3. Commit your changes and push.
4. Open a Pull Request describing your changes.

Please ensure code is well-documented and add tests where applicable.

---

## License

This project is provided under the MIT License. See LICENSE for details. (Add a LICENSE file to the repository if not present.)

---

## Contact

Project owner: MasudMallik  
GitHub: https://github.com/MasudMallik

If you have questions or want to report issues, please open an issue in this repository.
