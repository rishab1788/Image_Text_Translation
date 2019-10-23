from PIL import Image, ImageDraw, ImageFont

def main():
    try:
        # Relative Path
        g = raw_input("Enter name Of Certifier : ") 
        fontFile="/home/rishabhgupta/ImageProject/LucidaTypewriterBold.ttf"
        img = Image.open("/home/rishabhgupta/ImageProject/DSM.PNG")
        font = ImageFont.truetype(fontFile, 25)

        width, height = img.size
        area = (0, 0, width / 2, height / 2)
        d = ImageDraw.Draw(img) 
       
        #d.text((245, 245), "Hello World", fill=(101, 123, 123))
        fill=(0, 0, 0)
        d.text((110, 300), g, font=font, fill=fill)
        img.save("cropped_picture.png")
    except IOError:
        pass


if __name__ == "__main__":
    main()
