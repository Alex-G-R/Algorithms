fieldHeight = 640
fieldWidth = 1680

def DivideTheField(height, width):
    while height != width and width != 0:
        if width > height:
            width = width % height
        else:
            height = height % width

        # Greatest common divisor (NWW polish)
        gdc = height
    return gdc

print("This is the GDC: "+DivideTheField(fieldHeight, fieldWidth))
    