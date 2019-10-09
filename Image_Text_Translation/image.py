
from PIL import Image, ImageDraw


def main():
    try:
        # Relative Path
        img = Image.open("dp.jpg")
        width, height = img.size
        area = (0, 0, width / 2, height / 2)

        d = ImageDraw.Draw(img)
        d.text((45, 45), "Hello World", fill=(255, 255, 0))
        # Saved in the same relative location
        img.save("cropped_picture.jpg")
    except IOError:
        pass


if __name__ == "__main__":
    main()