import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image
import numpy as np
filename = "../resources/image.gif"
pilIm = Image.open(filename)    
pilIm.seek(0)

len_img = 50
# Read all images inside
images = []
try:
    k = 0
    while k<len_img:
        k += 1
        tmp = pilIm.convert() 
        a = np.asarray(tmp)
        images.append(a)
        pilIm.seek(pilIm.tell()+1)
except EOFError:
    pass


fig = plt.figure()

index = 0
im = plt.imshow(images[index], animated=True)


def updatefig(*args):
    global index
    speed = 6
    if index >= len_img-speed:
        index = 0
    index += 5
    im.set_array(images[index])
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=1, blit=True)
plt.show()