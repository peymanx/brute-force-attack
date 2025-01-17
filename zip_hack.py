import os
from tqdm import tqdm
from colorama import Fore, Style, init

# Initialize colorama
init()

def connect_to_zip(file, password):
    command = f'7z x "{file}" -p"{password}" -y >nul 2>&1'
    result = os.system(command)
    return result == 0

def read_passwords(file_path):
    with open(file_path, 'r') as file:
        passwords = file.readlines()
    return [password.strip() for password in passwords]

def main():
    file = "path/to/file.zip"
    password_file = './passwords/10k.txt'

    passwords = read_passwords(password_file)
    total_passwords = len(passwords)
    
    print(f"Compressed file path: {file}")
    print(f"Password: **********")

    max_password_length = max(len(password) for password in passwords)
    with tqdm(total=total_passwords, desc="Trying passwords", unit="password") as pbar:
        for password in passwords:
            padded_password = password.ljust(max_password_length)
            pbar.set_description(f"{Fore.YELLOW}Trying password: {padded_password}{Style.RESET_ALL}")
            if connect_to_zip(file, password):
                print(f'\n{Fore.GREEN}{"*"*70}')
                print(f'{Fore.GREEN}Successfully extract!')  # Blinking text
                print(f'{Fore.GREEN}Password: \'\033[5m{password}\033[0m{Fore.GREEN}\'')  # Blinking text
                print(f'{Fore.GREEN}{"*"*70}{Style.RESET_ALL}\n')
                break
            pbar.update(1)
        else:
            print(f'\n{Fore.RED}Password not found{Style.RESET_ALL}')

if __name__ == '__main__':
    main()