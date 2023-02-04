from PIL import Image
from function import Entropy 

degree =0 
def Entropy_image(image_file,degree) :
    print("openning",image_file,'...')
    image = Image.open(image_file)
    print("converting image to gray-scale ...")
    image = image.convert('L')
    print('displaying gray-scale image ...')
    image.show()
    print("converting image to binary string ...")
    pixels = image.getdata()
    image_string = ''.join(format(p , '08b') for p in pixels)
    print(image_string) 
    print('saving binary representation as << image_bin08 >> ...')
    with open('image_bin08.txt', 'w') as f:
        f.write(image_string)
    print("calculating entropy ...")
    TheEntropy = Entropy('image_bin08.txt',degree)
    return TheEntropy


H1 = Entropy_image('1.jpg',0)
H2 = Entropy_image('2.jpg',0)

print(H1)
print(H2)
if H1 == H2 :
    print("The two images matched")
else :
    print("The images did not match")

print("The percentage of similarity between the two images is: ",round(100*min(H1,H2)/max(H1,H2),2),"%")













