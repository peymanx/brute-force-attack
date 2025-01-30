import os
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
from tkinter import ttk
from tqdm import tqdm
from threading import Thread

# متغیر کمکی برای بررسی پیدا شدن پسورد
password_found = False

# تابع برای نمایش باکس
def print_box(message):
    messagebox.showinfo("نتیجه", message)

# تابع برای امتحان پسوردها
def try_passwords():
    global password_found
    with open(password_file_path, 'r') as file:
        passwords = file.readlines()
    total_passwords = len(passwords)
    progress_bar['maximum'] = total_passwords
    for i, password in enumerate(tqdm(passwords, desc="Trying passwords")):
        password = password.strip()  # حذف کاراکترهای اضافی مانند \n
        log_text.insert(tk.END, f'{password}\n')
        log_text.see(tk.END)
        command = f'7z.exe x "{archive_path}" -p{password} -y >nul 2>&1'
        result = os.system(command)

        if result == 0:  # اگر استخراج موفقیت‌آمیز بود
            print_box(f'پاسورد پیدا شد:\r\n{password}')
            password_found = True
            break

        # به‌روزرسانی progress bar
        progress_bar['value'] = i + 1
        root.update_idletasks()

    if not password_found:
        print_box('Password not found!')

    # پنهان کردن progress bar بعد از اتمام فرآیند
    progress_bar.pack_forget()

# تابع برای شروع امتحان پسوردها در یک ترد جداگانه
def start_bruteforce():
    # نمایش progress bar
    progress_bar.pack(pady=10)
    Thread(target=try_passwords).start()

# تابع برای انتخاب فایل فشرده
def select_archive():
    global archive_path
    archive_path = filedialog.askopenfilename()
    archive_label.config(text=f"فایل فشرده انتخاب شده: {archive_path}")

# تابع برای انتخاب فایل پسوردها
def select_password_file():
    global password_file_path
    password_file_path = filedialog.askopenfilename()
    password_label.config(text=f"فایل پسورد انتخاب شده: {password_file_path}")

# ایجاد رابط گرافیکی
root = tk.Tk()
root.title("Archive Brute-force by @peymanx")
root.configure(bg="#550b9c")

# ایجاد و تنظیم ویجت‌های رابط گرافیکی
image_label = tk.Label(root, bg="#550b9c")
image_label.pack(pady=10)

# بارگذاری عکس
image = tk.PhotoImage(file="./images/archive_banner.png")
image_label.config(image=image)

archive_button = tk.Button(root, text="مسیر فایل فشرده", command=select_archive, bg="white", fg="black", font=("Helvetica", 12))
archive_button.pack(pady=10)

archive_label = tk.Label(root, text="No file selected", bg="#550b9c", fg="white", font=("Helvetica", 10))
archive_label.pack(pady=5)

password_button = tk.Button(root, text="مسیر بانک پسوردها", command=select_password_file, bg="white", fg="black", font=("Helvetica", 12))
password_button.pack(pady=10)

password_label = tk.Label(root, text="No file selected", bg="#550b9c", fg="white", font=("Helvetica", 10))
password_label.pack(pady=5)

log_text = scrolledtext.ScrolledText(root, width=80, height=10, bg="black", fg="white", font=("Helvetica", 10))
log_text.pack(pady=20)

start_button = tk.Button(root, text="Brute-force شروع حمله  🔑 ", command=start_bruteforce, bg="#fcad0e", fg="black", font=("Helvetica", 12))
start_button.pack(pady=10)

# ایجاد و تنظیم ویجت progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack_forget()

# اجرای حلقه اصلی رابط گرافیکی
root.mainloop()