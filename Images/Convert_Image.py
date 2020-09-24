from PIL import Image

def JPEG_To_PNG(inputf,outputf):
    path='F:\\GitHub\\Image_Stenography\\Images\\{}'.format(inputf)
    o_path='F:\\GitHub\\Image_Stenography\\Images\\{}'.format(outputf)
    img = Image.open(path)
    img.save(o_path)
    
def RGB_To_Grayscale(inputf,outputf):
    path='F:\GitHub\Image_Stenography\Images\{}'.format(inputf)
    o_path='F:\GitHub\Image_Stenography\Images\{}'.format(outputf)
    img = Image.open(path).convert('LA')
    img.save(o_path)
    


