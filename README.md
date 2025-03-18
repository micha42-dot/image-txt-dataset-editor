# image-txt-dataset Editor

A simple Python-based GUI application to edit `.txt` files side-by-side with their corresponding image files.

## ✨ Features

- Select a folder containing `.txt` files and images
- Shows the matching image (`.jpg`, `.jpeg`, `.png`, `.bmp`) next to each text
- Displays the filenames above each item
- Easy navigation with:
  - **Previous / Next** buttons
  - **← / →** arrow keys
- Save changes with a 💾 button

## 📦 Requirements

- Python 3.7+
- Tkinter (comes preinstalled with Python)
- Pillow

Install dependencies:

```bash
pip install pillow
```

## 🚀 Run the App

```bash
python text_image_viewer.py
```

## 🛠 Build an Executable (Optional)

```bash
pip install pyinstaller
pyinstaller --noconsole text_image_viewer.py
```

You will find the executable in the `dist/` folder.

## 📄 License

MIT – free to use, modify and distribute.
