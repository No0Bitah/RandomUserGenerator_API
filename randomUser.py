import requests
import pandas as pd
import io
import time
import os
import sys
from prettytable import PrettyTable
from colorama import Fore, Style, init

# Initialize colorama for cross-platform colored terminal output
init(autoreset=True)

# Configuration dictionary
CONFIG = {
    "base_url": "https://randomuser.me/api",
    "gender_options": {
        1: "male",
        2: "female",
        3: "None"  # Random gender
    },
    "columns": ['gender', 'firstname', 'lastname', 'email', 'birthedate', 'age', 'username', 'password'],
    "header": """
    ╔══════════════════════════════════════════╗
    ║           RANDOM USER GENERATOR          ║
    ╚══════════════════════════════════════════╝
    """

}

def clear_screen():
    """Clear the terminal screen based on OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_loading_animation(seconds=2):
    """Display a simple loading animation."""
    for _ in range(seconds * 2):
        for char in ["|", "/", "-", "\\"]:
            sys.stdout.write(f"\r{Fore.CYAN}Loading {char}")
            sys.stdout.flush()
            time.sleep(0.125)
    print("\r" + " " * 20 + "\r", end="")

def create_user(num, gender_code):
    """Fetch random user data from API based on parameters."""
    # Get gender string from configuration dictionary
    gender = CONFIG["gender_options"].get(gender_code, "None")
    
    # Build query parameters
    params = {
        "results": num,
        "gender": gender if gender != "None" else "",
        "format": "csv",
        "dl": ""
    }
    
    # Make API request
    try:
        print(f"{Fore.YELLOW}Connecting to API...")
        response = requests.get(CONFIG["base_url"], params=params)
        response.raise_for_status()  # Raise exception for bad status codes
        print(f"{Fore.GREEN}Successfully retrieved user data!")
        print_loading_animation(1)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error fetching data: {e}")
        return None

def display_user(data):
    """Display user data in a formatted table."""
    if not data:
        print(f"{Fore.RED}No data to display.")
        return
    
    # Create and configure table
    pt = PrettyTable()
    pt.align = "c"  # Center align all columns
    pt.max_width = 30  # Limit column width for better display
    
    # Parse CSV data and add to table
    try:
        df = pd.read_csv(io.StringIO(data), sep=',')
        # rename the columns and date format
        df.rename(columns={'name.first': 'firstname', 'name.last': 'lastname', 'dob.date': 'birthedate', 'dob.age': 'age', 'login.username': 'username', 'login.password': 'password'}, inplace=True)
        df['birthedate'] = pd.to_datetime(df['birthedate']).dt.strftime('%m/%d/%Y')

        pt.field_names = CONFIG["columns"]
        for row in df[CONFIG["columns"]].itertuples(index=False):

            pt.add_row(row)
        
        # Create a csv file
        if len(df) >= 10:
            df[CONFIG["columns"]].to_csv('user.csv', index=False)

        print(f"{Fore.CYAN}{pt}")
        print(f"\n{Fore.GREEN}Total users displayed: {len(df)}")
        print(f"\n{Fore.GREEN}File created {Fore.RED}(user.csv) {Fore.GREEN}if Users are 10 or more!")
        
    except Exception as e:
        print(f"{Fore.RED}Error displaying data: {e}")

def check_input(prompt, gender_input=False):
    """Validate user input with improved error messages."""
    while True:
        print(f"{Fore.CYAN}{prompt}")
        user_input = input(f"{Fore.WHITE}> ")
        
        try:
            value = int(user_input)
            
            if value <= 0:
                print(f"{Fore.RED}Please enter a number greater than 0.")
                continue
                
            if gender_input and value not in CONFIG["gender_options"]:
                print(f"{Fore.RED}Please select 1, 2, or 3 for gender option.")
                continue
                
            return value
            
        except ValueError:
            print(f"{Fore.RED}Invalid input. Please enter a number.")

def display_gender_menu():
    """Display gender selection menu."""
    menu = f"""
    {Fore.CYAN}Select gender of random users:
    {Fore.WHITE}┌───────────────┐
    │ {Fore.BLUE}1 = Male      {Fore.WHITE}│
    │ {Fore.MAGENTA}2 = Female    {Fore.WHITE}│
    │ {Fore.YELLOW}3 = Random    {Fore.WHITE}│
    └───────────────┘
    """
    print(menu)

def main():
    """Main application function."""
    try:
        clear_screen()
        print(f"{Fore.CYAN}{CONFIG['header']}")
        
        # Get user inputs
        number_of_users = check_input(f"\nHow many users do you want to create? {Fore.YELLOW}(1-100 recommended)")
        
        display_gender_menu()
        user_gender = check_input("", gender_input=True)
        
        # Get and display user data
        print_loading_animation()
        user_data = create_user(number_of_users, user_gender)
        display_user(user_data)
        
        print(f"\n{Fore.CYAN}Press Ctrl+C to exit or Enter to generate more users...")
        input()
        main()  # Restart the program
        
    except KeyboardInterrupt:
        clear_screen()
        print(f"\n{Fore.YELLOW}✨ Thanks for using the Random User Generator! ✨")
        sys.exit(0)

if __name__ == '__main__':
    main()