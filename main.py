import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
from rembg import remove
import os


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)


def select_output_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, folder_path)


def convert_image():
    file_path = file_entry.get()
    output_folder = output_entry.get()
    target_format = format_var.get()
    remove_bg = bg_var.get()

    if not file_path:
        messagebox.showerror("Error", "Please select an image file.")
        return

    if not output_folder:
        messagebox.showerror("Error", "Please select an output folder.")
        return

    if not target_format:
        messagebox.showerror("Error", "Please select a target format.")
        return

    try:
        image = Image.open(file_path)
        if remove_bg:
            image = remove(image)

        output_filename = os.path.join(output_folder,
                                       os.path.splitext(os.path.basename(file_path))[0] + f'.{target_format}')
        image.save(output_filename)

        messagebox.showinfo("Success", f"Image converted and saved to {output_filename}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Image Converter")
root.geometry("600x400")
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12))

main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill=tk.BOTH, expand=True)

file_frame = ttk.Frame(main_frame, padding="10 10 10 10")
file_frame.pack(fill=tk.X, pady=5)

ttk.Label(file_frame, text="Select Image File:").pack(side=tk.LEFT)
file_entry = ttk.Entry(file_frame, width=50)
file_entry.pack(side=tk.LEFT, padx=10)
ttk.Button(file_frame, text="Browse", command=select_file).pack(side=tk.LEFT)

output_frame = ttk.Frame(main_frame, padding="10 10 10 10")
output_frame.pack(fill=tk.X, pady=5)

ttk.Label(output_frame, text="Select Output Folder:").pack(side=tk.LEFT)
output_entry = ttk.Entry(output_frame, width=50)
output_entry.pack(side=tk.LEFT, padx=10)
ttk.Button(output_frame, text="Browse", command=select_output_folder).pack(side=tk.LEFT)

format_frame = ttk.Frame(main_frame, padding="10 10 10 10")
format_frame.pack(fill=tk.X, pady=5)

ttk.Label(format_frame, text="Target Format:").pack(side=tk.LEFT)
format_var = tk.StringVar(value="png")
ttk.OptionMenu(format_frame, format_var, "png", "jpg", "bmp", "tiff").pack(side=tk.LEFT, padx=10)

bg_var = tk.BooleanVar()
bg_check = ttk.Checkbutton(main_frame, text="Remove Background", variable=bg_var)
bg_check.pack(pady=10)

ttk.Button(main_frame, text="Convert", command=convert_image).pack(pady=20)

root.mainloop()
