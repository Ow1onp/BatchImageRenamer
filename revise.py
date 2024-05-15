import os
import re
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

def is_integer(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def batch_rename_images():
    images = [img for img in os.listdir('.') if re.match(r'.*\.(jpg|png)', img, re.I)]
    
    if not images:
        print("目录中没有 .jpg 或 .png 图像。")
        return
    
    start_number = simpledialog.askstring(title="Batch Rename",
                                         prompt="输入重新命名的起始编号（如 1、2、3）：")
    if not start_number or not is_integer(start_number):
        print("起始编号必须是整数。退出程序")
        return
    
    start_number = int(start_number)
    
    total_images = len(images)
    max_number = total_images + start_number - 1
    total_digits = len(str(max_number))

    for i, filename in enumerate(sorted(images)):
        name, extension = os.path.splitext(filename)
        new_name = f"{i + start_number:0{total_digits}d}{extension}"
        
        os.rename(filename, new_name)
        print(f"Renamed '{filename}' to '{new_name}'")

    print("重新命名已完成。")

if __name__ == "__main__":
    batch_rename_images()