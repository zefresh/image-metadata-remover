import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from PIL import Image


def remove_metadata(image_path):
    try:
        img = Image.open(image_path)

        # Copy only pixel data
        data = list(img.getdata())

        clean = Image.new(img.mode, img.size)
        clean.putdata(data)

        output = image_path.with_name(
            image_path.stem + "_clean" + image_path.suffix
        )

        # Save without EXIF metadata
        clean.save(output)

        return output

    except Exception as e:
        print(f"Failed: {image_path}")
        print(e)
        return None


def main():
    root = tk.Tk()
    root.withdraw()

    files = filedialog.askopenfilenames(
        title="Select images",
        filetypes=[
            ("Images", "*.jpg *.jpeg *.png *.tif *.tiff *.bmp *.webp"),
            ("All files", "*.*"),
        ],
    )

    if not files:
        return

    cleaned = []

    for filename in files:
        output = remove_metadata(Path(filename))
        if output:
            cleaned.append(output)

    messagebox.showinfo(
        "Done",
        f"Processed {len(cleaned)} image(s).\n\n"
        "New files were saved with '_clean' appended to the filename.",
    )


if __name__ == "__main__":
    main()
