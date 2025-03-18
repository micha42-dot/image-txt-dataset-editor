import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class TextImageViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("image-txt-dataset Editor")
        self.root.geometry("1000x600")

        # Data
        self.folder_path = ""
        self.txt_files = []
        self.current_index = 0
        self.supported_image_exts = [".jpg", ".jpeg", ".png", ".bmp"]

        # GUI Elements
        self.create_widgets()
        self.root.bind("<Left>", lambda event: self.prev_file())
        self.root.bind("<Right>", lambda event: self.next_file())

    def create_widgets(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.select_button = tk.Button(top_frame, text="Select Folder", command=self.select_folder)
        self.select_button.pack(side=tk.LEFT)

        self.filename_label = tk.Label(top_frame, text="No folder selected")
        self.filename_label.pack(side=tk.LEFT, padx=10)

        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        image_frame = tk.Frame(main_frame)
        image_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.image_filename_label = tk.Label(image_frame, text="")
        self.image_filename_label.pack()

        self.image_label = tk.Label(image_frame)
        self.image_label.pack()

        text_frame = tk.Frame(main_frame)
        text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.text_filename_label = tk.Label(text_frame, text="")
        self.text_filename_label.pack(anchor="w")

        self.text_area = tk.Text(text_frame, wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        nav_frame = tk.Frame(self.root)
        nav_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

        self.prev_button = tk.Button(nav_frame, text="Previous", command=self.prev_file)
        self.prev_button.pack(side=tk.LEFT, padx=5)

        self.next_button = tk.Button(nav_frame, text="Next", command=self.next_file)
        self.next_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(nav_frame, text="💾 Save", command=self.save_file)
        self.save_button.pack(side=tk.RIGHT, padx=10)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path = folder
            self.txt_files = [f for f in os.listdir(folder) if f.lower().endswith(".txt")]
            self.txt_files.sort()
            self.current_index = 0
            self.filename_label.config(text=folder)
            if self.txt_files:
                self.load_file()
            else:
                messagebox.showwarning("No TXT Files", "No .txt files found in the selected folder.")

    def find_image_for_txt(self, base_name):
        for ext in self.supported_image_exts:
            image_path = os.path.join(self.folder_path, base_name + ext)
            if os.path.exists(image_path):
                return image_path
        return None

    def load_file(self):
        if not self.txt_files:
            return

        txt_filename = self.txt_files[self.current_index]
        txt_path = os.path.join(self.folder_path, txt_filename)

        with open(txt_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)

        self.text_filename_label.config(text=txt_filename)

        base_name = os.path.splitext(txt_filename)[0]
        image_path = self.find_image_for_txt(base_name)

        if image_path:
            img = Image.open(image_path)
            img.thumbnail((400, 400))
            self.tk_image = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.tk_image, text="")
            self.image_filename_label.config(text=os.path.basename(image_path))
        else:
            self.image_label.config(image="", text="No image found")
            self.image_filename_label.config(text="No image")

    def save_file(self):
        txt_filename = self.txt_files[self.current_index]
        txt_path = os.path.join(self.folder_path, txt_filename)
        content = self.text_area.get(1.0, tk.END)
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("Saved", f"{txt_filename} saved.")

    def next_file(self):
        if self.current_index < len(self.txt_files) - 1:
            self.current_index += 1
            self.load_file()

    def prev_file(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.load_file()

if __name__ == "__main__":
    root = tk.Tk()
    app = TextImageViewerApp(root)
    root.mainloop()

