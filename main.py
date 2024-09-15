from PIL import Image
from tqdm import tqdm



def main():
    im = Image.open("imgs/download.jpg")

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
    st = ""
    if num >= 204:
        st = " "
    elif num >= 153:
        st = "."
    elif num >= 102:
        st = "-"
    elif num >= 51:
        st = "="
    else:
        st = "#"
    return st


if __name__ == "__main__":
    main()