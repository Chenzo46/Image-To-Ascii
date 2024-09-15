from PIL import Image
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog

ascii_depth = list(reversed(list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'.")))

def main():

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    im = Image.open(file_path)

    output = open("out.txt", "w")
    content = ""
    pxCount = im.size[0] * im.size[1]

    for lookY in tqdm(range(0,im.size[1]), f'Parsing Image...'):
        for lookX in range(0, im.size[0]):
            px = im.getpixel([lookX, lookY])
            highestPix = max(list(px))
            content += get_asc(highestPix)
        content += "\n"
            
    output.write(content)

    output.close()

    print("Image parsing complete!")

def get_asc(num:int)->str:
    st = ascii_depth[len(ascii_depth)-1]
    ascii_depth_len = len(ascii_depth)
    step = int(255/ascii_depth_len)
    lm = 255-step
    for idx in range(ascii_depth_len):
        if num >= lm:
            st = ascii_depth[idx]
            break;
        lm -= step
    return st


if __name__ == "__main__":
    main()