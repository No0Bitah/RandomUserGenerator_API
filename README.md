# Random User Generator
![Random User Generator](https://img.shields.io/badge/Python-API%20-blue)
## Description
This script fetches and displays random user data from the [Random User API](https://randomuser.me/api) with options to filter by gender. It presents the data in a well-formatted table and saves it to a CSV file if the number of users generated is 10 or more.

## Features
- Fetches random user data using an API
- Allows selection of user count and gender
- Displays data in a formatted table
- Saves data to a CSV file if users are 10 or more
- Provides a user-friendly CLI with animations and color formatting

## Dependencies
Ensure you have the following Python libraries installed:

```sh
pip install requests pandas prettytable
```

## Usage
Run the script using:

```sh
python randomUser.py
```

Follow the on-screen prompts to generate user data.

### Options
1. Enter the number of users to generate (recommended: 1-100)
2. Select gender:
   - 1 = Male
   - 2 = Female
   - 3 = Random

## Output
- Displays user details in a table format
- If 10 or more users are generated, a `user.csv` file is created

## Example Output
```
╔══════════════════════════════════════════╗
║           RANDOM USER GENERATOR          ║
╚══════════════════════════════════════════╝

How many users do you want to create? (1-100 recommended)
> 5

Select gender of random users:
1 = Male
2 = Female
3 = Random
> 3

Connecting to API...
Successfully retrieved user data!

+--------+-----------+----------+----------------+------------+----+----------+----------+
| gender | firstname | lastname |     email      | birthdate  | age | username | password |
+--------+-----------+----------+----------------+------------+----+----------+----------+
|  Male  |  John     |  Doe     | john@example.com | 01/01/1990 | 34 | johndoe  | abc123   |
+--------+-----------+----------+----------------+------------+----+----------+----------+

Total users displayed: 5
File created (user.csv) if Users are 10 or more!
```

## Exit
Press `Ctrl+C` to exit the script at any time.

## 🤝 Contributing
Feel free to fork, submit issues, or suggest improvements. Contributions are welcome!

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

