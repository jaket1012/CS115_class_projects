# === CS 115 Homework 4 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Jake Talvy
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Homework 4 ===
from hw4_library import ppm_to_list_of_lists_of_rgbs, save_string_to_txt
from functools import reduce

def change_pixel_brightness(image):
    """converts the rgb values of a pixel into a single brightness value from 0-255"""
    image = list(image)
    x = 0.299*image[0] + 0.587*image[1] + 0.114*image[2]
    if x > 255:
        x = 255
    return x

def pixel_convert_to_grayscale(image):
    """converts one pixel in the image to greyscale"""
    image[:] = list(map(change_pixel_brightness, image))

def rgb_to_grayscale(image):
    """
    Mutates a 2D list of RGB pixels to a 2D list of grayscale values.
    Uses the CCIR 601 standard brightness formula:
        gray = int (0.299*red + 0.587*green + 0.114*blue)
    Does not return anything
    """
    list(map(pixel_convert_to_grayscale, image))


def brightness_to_ascii(brightness):
    """
    converts a brightness to a symbol based on its value
    Use the table on the homework for specific ranges
    of brightness to ASCII
    """
    if brightness >= 0 and brightness < 26:
        return "@"
    if brightness >= 26 and brightness < 52:
        return "#"
    if brightness >= 52 and brightness < 77:
        return "%"
    if brightness >= 77 and brightness < 103:
        return "*"
    if brightness >= 103 and brightness < 128:
        return "="
    if brightness >= 128 and brightness < 154:
        return "+"
    if brightness >= 154 and brightness < 180:
        return "-"
    if brightness >= 180 and brightness < 205:
        return ":"
    if brightness >= 204 and brightness < 231:
        return "."
    if brightness >= 231 and brightness <= 255:
        return " "
    


def image_to_ascii_string(image):
    """
    Convert a 2D list of grayscale values (0–255)
    into a single string of ASCII characters where
    each row in the image corresponds to a line
    in the ASCII string. 

    Each line break is represented with \n\r
    to ensure compatibility with Windows 
    
    returns that string, only containing valid ASCII
    characters
    """
    if len(image) == 0:
        return ""
    if len(image) == 1:
        return reduce(lambda x,y: x+y, list(map(brightness_to_ascii, image[0])))
    return reduce(lambda x,y: x+y, list(map(brightness_to_ascii, image[0]))) + "\r\n" + image_to_ascii_string(image[1:])
    

def invert_row(image):
    """inverts one row in the given image"""
    return list(map(lambda x: 255-x, image))
    
def invert(image):
    """
    inverts the brightness of each pixel in the image

    Does not return anything. Only mutates the input.
    """
    image[:] = list(map(invert_row, image))

def lighten_pixel(pixel):
    x = pixel*1.3
    if x>255:
        return 255
    return x

def lighten_row(image):
    image[:] = list(map(lighten_pixel,image))
        
def lighten(image):
    """
    TODO: Fill in your own docstring here based on 
    the homework description

    Does not return anything. Only mutates the input.
    """
    list(map(lighten_row, image))


def darken_pixel(pixel):
    x = pixel/1.3
    if x<0:
        return 0
    return x

def darken_row(image):
    image[:] = list(map(darken_pixel,image))
    
def darken(image):
    """
    TODO: Fill in your own docstring here based on 
    the homework description

    Does not return anything. Only mutates the input.
    """
    list(map(darken_row,image))

def set_zero(image):
    image[:] = list(map(lambda x: 0, image))
    
def erase(image):
    """
    erases the image

    Does not return anything. Only mutates the input.
    """
    list(map(set_zero,image))

def load_rgb_image(image_name):
    """
    Given a filename, image_name, returns 
    a grayscale image, 
    represented as a 2D list of intensities

    Do not change this function. It is just here for reference.
    """
    image = ppm_to_list_of_lists_of_rgbs(image_name)
    return image 


if __name__ == "__main__":
    # All code you want to run goes in this indented block
    # You can change the name of ppm_image_filename
    ppm_image_filename = "treasure_map.ppm"

    # This line calls our library function to load the image as 
    # a list of lists of rgb values
    image = load_rgb_image(ppm_image_filename)

    # Uncomment this line for Task 1
    # 
    rgb_to_grayscale(image)

    # Uncomment this line for Task 2
    
    invert(image)
    darken(image)
    ascii_string = image_to_ascii_string(image)
    print(ascii_string)
    # Uncomment this to save your ascii string to a text file
    # which can be read in other applications and uploaded
    # to Gradescope
    # 
    save_string_to_txt(ascii_string)
