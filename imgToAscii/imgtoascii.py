from PIL import Image, ImageFilter

charsSortedByBrightness = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


path = input("Please enter the path of the image you want to convert.\n")
width = input("Please enter the desired width of the ASCII output in characters. (default = 64) \n")

try:
    width = int(width)
except ValueError:
    width = 64

def remove_transparency(im, bg_colour=(255, 255, 255)):
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
        alpha = im.convert('RGBA').split()[-1]
        bg = Image.new("RGBA", im.size, bg_colour + (255,))
        bg.paste(im, mask=alpha)
        return bg
    else:
        return im

try:
    img = Image.open(path)
    img.load()
    imgwidth, imgheight = img.size
    aspectRatio = imgwidth/imgheight
    height = int(width/aspectRatio)

    img = remove_transparency(img, bg_colour=(255, 255, 255))

    toAscii = img.resize((width*2, height), resample =  0, box = None, reducing_gap = None).convert('L')

    highest = 0
    lowest = 255

    asciiString = ""
    
    for y in range(height):
        for x in range(width*2):
            l = toAscii.getpixel((x, y))
            l = int(l/3.69565217391)
            asciiString += charsSortedByBrightness[l]
        asciiString += "\n"

    outputFile = open("asciiArt.txt","w")
    outputFile.write(asciiString)
    outputFile.close()
    
    print("Image successfully converted.")
    input()
except IOError:
    print("Can't convert image.")
    input()

