import requests
from colorama import Fore, Style
import os
import random
import string

# Username generation function
def generate_username(min_length=4, max_length=15):
    # Define the characters to be used in the username
    characters = string.ascii_letters + string.digits
    username_length = random.randint(min_length, max_length)
    username = ''.join(random.choice(characters) for _ in range(username_length))
    return username

# Validate a single username using the Roblox API
def validate_username(username):
    url = f"https://auth.roblox.com/v1/usernames/validate?birthday=2006-09-21T07:00:00.000Z&context=Signup&username={username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['code'] == 0:  # Username is valid and available
            return f"{Fore.GREEN}Valid: {username}{Style.RESET_ALL}"
        elif data['code'] == 1:
            return f"{Fore.RED}Invalid: {username} (already in use){Style.RESET_ALL}"
        elif data['code'] == 2:
            return f"{Fore.RED}Invalid: {username} (not appropriate for Roblox){Style.RESET_ALL}"
        elif data['code'] == 10:
            return f"{Fore.YELLOW}Invalid: {username} (might contain private information){Style.RESET_ALL}"
    else:
        return f"{Fore.RED}Unable to access Roblox API{Style.RESET_ALL}"

# Save valid username to a file
def save_valid_username(username):
    filename = "valid.txt"  # Save all valid usernames in a single file
    with open(filename, 'a') as file:
        file.write(username + '\n')

# Developer Info
def show_developer_info():
    print(f"\n{Fore.CYAN}Thank you to jprocks101 for the base idea and concept!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}This script was expanded and improved by Void with additional features such as random username generation, improved handling, and better user interface.{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Follow Void at: https://www.twitch.tv/voidedluvr{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Check out Void's other projects at: https://github.com/VoidedLuvr{Style.RESET_ALL}")
    print("\n")
    input(f"{Fore.MAGENTA}[{Fore.RESET}Press Enter to return to the menu{Fore.MAGENTA}]{Fore.RESET}")  # Wait for user to press Enter

# Main function to handle user choices
while True:
    print()
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
    print(f"{Fore.BLUE}██   ██  ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████  ")
    print(f" ██ ██  ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ ")
    print(f"  ███   ██      ███████ █████   ██      █████   █████   ██████  ")
    print(f" ██ ██  ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ ")
    print(f"██   ██  ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██ {Style.RESET_ALL}")
    print()
    print(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} Choose an option:")
    print(f"{Fore.MAGENTA}[{Fore.RESET}1{Fore.MAGENTA}]{Fore.RESET} Manually enter a username")
    print(f"{Fore.MAGENTA}[{Fore.RESET}2{Fore.MAGENTA}]{Fore.RESET} Check a list of usernames from a file")
    print(f"{Fore.MAGENTA}[{Fore.RESET}3{Fore.MAGENTA}]{Fore.RESET} Generate random usernames")
    print(f"{Fore.MAGENTA}[{Fore.RESET}4{Fore.MAGENTA}]{Fore.RESET} Developer Info")
    print(f"{Fore.MAGENTA}[{Fore.RESET}0{Fore.MAGENTA}]{Fore.RESET} Exit")
    choice = input(f"{Fore.MAGENTA}[{Fore.RESET}>{Fore.MAGENTA}]{Fore.RESET} ")

    if choice == '1':
        username = input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} Enter a username: ")
        result = validate_username(username)
        print(result)
    elif choice == '2':
        filename = input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} Enter the filename of the usernames file (must include .txt): ")
        with open(filename, "r") as file:
            usernames = file.read().splitlines()
        for username in usernames:
            result = validate_username(username)
            print(result)
    elif choice == '3':
        # Ask user for the length of the username
        min_len = int(input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} Enter the minimum length for the username (4-15): "))
        max_len = int(input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} Enter the maximum length for the username (4-15): "))

        if 4 <= min_len <= 15 and 4 <= max_len <= 15 and min_len <= max_len:
            # Ask for how many usernames to generate
            num_usernames = int(input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} How many usernames would you like to generate? "))

            # Variables to track username lists
            valid_usernames = []
            invalid_usernames = []

            # Loop to generate usernames
            for _ in range(num_usernames):
                generated_username = generate_username(min_len, max_len)
                print(f"{Fore.CYAN}Generated Username: {generated_username}{Style.RESET_ALL}")
                
                result = validate_username(generated_username)
                print(result)

                # Categorize usernames
                if "Valid" in result:
                    valid_usernames.append(generated_username)
                    save_valid_username(generated_username)  # Save valid usernames to the file
                else:
                    invalid_usernames.append(generated_username)

            # Display the status summary after all generations
            print(f"\n{Fore.GREEN}Usernames Generated: {num_usernames}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Valid Usernames: {len(valid_usernames)}{Style.RESET_ALL}")
            print(f"{Fore.RED}Invalid Usernames: {len(invalid_usernames)}{Style.RESET_ALL}")
            for username in invalid_usernames:
                print(f"Invalid: {username} (already in use)")

        else:
            print(f"{Fore.RED}Invalid length. Please enter values between 4 and 15 for both min and max length.{Style.RESET_ALL}")
    elif choice == '4':
        show_developer_info()
    elif choice == '0':
        break
    else:
        print(f"{Fore.RED}Invalid choice{Style.RESET_ALL}")
