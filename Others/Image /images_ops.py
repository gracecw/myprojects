import sys
from PIL import Image

# Helper Functions #
def region3x3 (img, x, y):
	C = getpixel(img, x, y)
	NW = getpixel(img, x-1, y-1)
	N = getpixel(img, x, y-1)
	NE = getpixel(img, x+1, y-1)
	E = getpixel(img, x+1, y)
	SE = getpixel(img, x+1, y+1)
	S = getpixel(img, x, y+1)
	SW = getpixel(img, x-1, y+1)
	W = getpixel(img,x-1,y+1)
	return [C,N,S,E,W,NW,NE,SE,SW]


def getpixel(img, x, y):
	width, height = img.size
	if x < 0:
		x = 0
	elif x >= width :
		x = width - 1
	if y < 0:
		y = 0
	elif y >= height:
		y = height - 1
	pixels = img.load()
	return pixels[x,y]


def filter(img, f):
    width, height = img.size
    imgdup = img.copy()
    pixels = imgdup.load()
    for x in range(width):
        for y in range(height):
            r = region3x3(img, x, y)
            pixels[x, y] = int(f(r))
    return imgdup


def open(filepath):
	if len(filepath)<=1:
		print ("missing image filename")
		sys.exit(1)
	img = Image.open(filepath)
	img = img.convert("L")
	return img

def showimg(filepath):
    img = open(filepath) # load file specified on the command line
    img.show()

    
# For Sharpen #

#define laplace function
def laplace (regionlist):
	value = sum(regionlist[1:5]) - 4 * regionlist[0]
	return value

def minus (A,B):
    width, height = A.size
    dupA = A.copy()
    pixelsA = A.load()
    pixelsdupA = dupA.load()
    pixelsB = B.load()
    for x in range(width):
        for y in range(height):
            pixelsdupA [x,y] = pixelsA[x,y] - pixelsB[x,y]
    return dupA

def sharpen(img):
    edges = filter(img, laplace)
    imgdup = minus(img, edges)
    return imgdup

# For Flip #
def flip(img):
	width, height = img.size
	imgdup = img.copy()
	org = img.load()
	dup = imgdup.load()
	for j in range(height):
		for i in range(width):
			dup[i,j] = org[width-i-1, j]
	return imgdup

# For Denoise #
def median (regionlist):
	regionlist = sorted(regionlist)
	m = len(regionlist)/2
	return regionlist[m]

def denoise(img):
    imgdup = filter(img, median)
    return imgdup

# For Blur #

def avg (regionlist):
	return sum(regionlist)/len(regionlist)


def blur(img):
    imgdup = filter(img, avg)
    return imgdup




