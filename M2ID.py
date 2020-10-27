# MapleStory2 Image Devider
# Made by. the Clock says tick tock
# Python 2.7.12
# You must need PIL
# You may install with "pip install Pillow" on cmd

BLOCKSIZE = 227

from PIL import Image

def imageProcessor(rawImage, i, j, n, m, Mode = 0):
    saveFileName = "result"
    if n >= 10 and i < 10:
        saveFileName = saveFileName + "0" + str(i)
    else:
        saveFileName = saveFileName + str(i)

    if m >= 10 and j < 10:
        saveFileName = saveFileName + "0" + str(j)
    else:
        saveFileName = saveFileName + str(j)
    saveFileName = saveFileName + ".png"
    
    if Mode >= 3:
        try:
            result = Image.open(saveFileName)
        except:
            result = Image.new("RGB", (1024, 1024), "white")
    else:
        result = Image.new("RGB", (1024, 1024), "white")
        
    width = rawImage.size[0] / n
    height = rawImage.size[1] / m
    if height > width:
        height = width
    elif width > height:
        width = height
    
    resizeImage = rawImage.crop((j*width, i*height, j*width+width, i*height+height))
    if Mode == 0: #block
        resizeImage = resizeImage.resize((230, 230), Image.ANTIALIAS)
        result.paste(resizeImage, (286,438))
    elif Mode == 1: #flat
        resizeImage = resizeImage.resize((360, 360), Image.ANTIALIAS)
        result.paste(resizeImage, (156,410))

    elif Mode == 2: #block upper face
        resizeImage = resizeImage.resize((229, 229), Image.ANTIALIAS)
        result.paste(resizeImage, (285,213))
        # some addition : left side
        tmpImage = resizeImage.crop((0,0,6,228))
        tmpImage = tmpImage.resize((229,229),Image.ANTIALIAS)
        tmpImage = tmpImage.rotate(90)
        tmpImage = tmpImage.resize((229,7),Image.ANTIALIAS)
        result.paste(tmpImage, (55, 438))

        # some addition : right side
        tmpImage = resizeImage.crop((222,0,228,228))
        tmpImage = tmpImage.resize((229,229),Image.ANTIALIAS)
        tmpImage = tmpImage.rotate(270)
        tmpImage = tmpImage.resize((229,7),Image.ANTIALIAS)
        result.paste(tmpImage, (514,438))

        # some addition : down side
        tmpImage = resizeImage.crop((0,226,228,228))
        result.paste(tmpImage, (285,442))
        
    elif Mode == 3: #Rotating block
        resizeImage = resizeImage.resize((BLOCKSIZE, BLOCKSIZE), Image.ANTIALIAS)
        result.paste(resizeImage, (57,440))
    elif Mode == 4:
        resizeImage = resizeImage.resize((BLOCKSIZE, BLOCKSIZE), Image.ANTIALIAS)
        result.paste(resizeImage, (57+BLOCKSIZE,440))
    elif Mode == 5:
        resizeImage = resizeImage.resize((BLOCKSIZE, BLOCKSIZE), Image.ANTIALIAS)
        result.paste(resizeImage, (57+2*BLOCKSIZE,440))
    elif Mode == 6:
        resizeImage = resizeImage.resize((BLOCKSIZE, BLOCKSIZE), Image.ANTIALIAS)
        result.paste(resizeImage, (57+3*BLOCKSIZE,440))
    
    #print "Save image", saveFileName
    result.save(saveFileName)







print "MapleStory2 Image Divider"
mode = int(raw_input("Mode Selection\n0 : Block (Side face)\n1 : Flat (Side face)\n2 : Block (Upper face)\n3 : Rotating Block\n"))

# Mode 0, 1, 2 which require only one image file
if mode < 3:
    inputImageName = raw_input("\nInput image file name include extension. ex) image.png\n")
    try:
        inputImage = Image.open(inputImageName)
    except:
        print "Cannot find the file"
        raw_input ("Press Enter to Exit...")
        exit()
    
    print "\nDevide image with NxM (with N columns, M rows)"
    print "input N in integer"
    n = int(input())
    print "\ninput M in integer"
    m = int(input())
    w = inputImage.size[0]/n
    h = inputImage.size[1]/m
    if w > h:
        w = h
        print "\n", 100 - w*n*100/inputImage.size[0], "% lost for width"
    else:
        h = w
    print "\n", 100 - h*m*100/inputImage.size[1], "% lost for height"

    tmpImage = inputImage.crop((0,0,w*n,h*m))
    tmpImage.save("result.png")
    
    for j in range(m):
        for i in range(n):
            imageProcessor(inputImage, j, i, n, m, mode)

# Mode 3 which require multiple image files
else:
    print "Rotating Block requires more than one image file"
    print "If you want te leave a face empty, just press enter without any typing"
    inputImageName = raw_input("\nInput first image file name include extension ex) image.png\n")
    try:
        inputImage = Image.open(inputImageName)
    except:
        print "Fail to open file"
        inputImage = Image.new("RGB", (BLOCKSIZE, BLOCKSIZE), "white")
    
    inputImageName = raw_input("\nInput second image file name include extension ex) image.png\n")
    try:
        inputImage2 = Image.open(inputImageName)
    except:
        print "Fail to open file"
        inputImage2 = Image.new("RGB", (BLOCKSIZE, BLOCKSIZE), "white")
    
    inputImageName = raw_input("\nInput third image file name include extension ex) image.png\n")
    try:
        inputImage3 = Image.open(inputImageName)
    except:
        print "Fail to open file"
        inputImage3 = Image.new("RGB", (BLOCKSIZE, BLOCKSIZE), "white")

    inputImageName = raw_input("\nInput fourth image file name include extension ex) image.png\n")
    try:
        inputImage4 = Image.open(inputImageName)
    except:
        print "Fail to open file"
        inputImage4 = Image.new("RGB", (BLOCKSIZE, BLOCKSIZE), "white")

    print "\nDevide image with NxM (with N columns, M rows)"
    print "input N in integer"
    n = int(input())
    print "\ninput M in integer"
    m = int(input())
 
    for j in range(m):
        for i in range(n):
            imageProcessor(inputImage4, j, i, n, m, 3)
            imageProcessor(inputImage, j, i, n, m, 4)
            imageProcessor(inputImage2, j, i, n, m, 5)
            imageProcessor(inputImage3, j, i, n, m, 6)

raw_input ("\nPress Enter to Exit...")
