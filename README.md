# Brute-force attack

**Author:** Peyman Majidi Moein (aka Peymanx) and Ai

This project is related to a YouTube video on the [peymanx](https://www.youtube.com/@peymanx) channel.

## Table of Contents

- [Introduction](#introduction)
- [Sample Code](#sample-code)
- [Resources](#resources)
- [License](#license)
- [TODO](#todo)

## Introduction

This repository contains various scripts and tools for performing brute-force attacks on different systems. The primary goal is to demonstrate the vulnerabilities and educate users on the importance of strong passwords and security measures.  

This repository contains a list of commonly used [passwords in Iran](./passwords/commons_iranians.txt). It's designed to help developers and security professionals understand password patterns in the region, improve password policies, and enhance security measures

## Preview

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


## Resources

- [SecLists is the security tester's companion. It's a collection of multiple types of lists used during security assessments](https://github.com/danielmiessler/SecLists)
- [Persian Words Jadi 😍](https://github.com/jadijadi/persianwords)
- [Iranian-Password-list](https://github.com/Dih4v/Iranian-Password-list)
- [Wikipedia](https://en.wikipedia.org/wiki/List_of_the_most_common_passwords)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## TODO

- [x] **Windows Login Authentication (SMB) Brute-force**  
- [x] **WiFi Network Password Cracking (Brute-force)**  
- [x] **Encrypted Archive (ZIP, RAR, etc.) Password Cracking**  
- [ ] **Email Account Credential Brute-force**  
- [ ] **PDF File Password Recovery (Brute-force)**  
- [ ] **SSH Remote Login Brute-force Attack**  
- [ ] **RDP (Remote Desktop Protocol) Credential Brute-force**  
- [ ] **SQL Server Database Login Brute-force**  
- [ ] **MySQL Database Authentication Brute-force**  
- [ ] **Telnet Service Credential Brute-force**  
- [ ] **FTP Server Login Brute-force**  
- [ ] **HTTP/HTTPS Basic Authentication Brute-force**  
- [ ] **LDAP Directory Login Brute-force**  
- [ ] **VNC (Virtual Network Computing) Login Brute-force**  
- [ ] **Oracle Database Credential Brute-force**  
- [ ] **VPN Connection Authentication Brute-force**  
- [ ] **WordPress Admin Panel or Joomla CMS Admin Login Brute-force**
- [ ] TODO for updating TODOs ? 
- [ ] Error ckecking and validation
- [ ] Add GUIs: Graphical User Interface

