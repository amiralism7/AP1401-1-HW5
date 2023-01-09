import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image
import copy

def f(x):
    global delay
    return np.sin(15 * x + delay) + 3

delay = 0
def plot_total():
    global delay
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.axis('off')

    x = np.linspace(0, 2 * np.pi, 300) 
    delay += np.pi/15

    plt.xlim(0,119)
    plt.ylim(0,11)
    plt.plot(f(x), "k")
    fig.canvas.draw()
    sine = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8).reshape(fig.canvas.get_width_height()[::-1] + (3,))
    sine_no_border = copy.deepcopy(sine[:,150:640])
    plt.close()
    sine_no_border[:,0:3,:] = np.zeros_like(sine_no_border[:,0:3,:])
    sine_no_border[:,-2:,:] = np.zeros_like(sine_no_border[:,-2:,:])
    sine_no_border[0:3,:,:] = np.zeros_like(sine_no_border[0:3,:,:])
    sine_no_border[-2:,:,:] = np.zeros_like(sine_no_border[-2:,:,:])

    red_back = np.zeros((sine_no_border.shape[0]+40, sine_no_border.shape[1]+40, 3))
    red_back[:,:,0] = np.ones_like(red_back[:,:,0]) * 1.0
    red_back[20:-20, 20:-20,:] = sine_no_border/255


    
    filename = "../resources/image.jpeg"
    pilIm = Image.open(filename)    
    newsize = (red_back[22:-22, 22:-22,:].shape[1], red_back[22:-22, 22:-22,:].shape[0])
    d_size = (int(newsize[0]/2), int(newsize[1]/2))
    daemon = pilIm.resize(newsize)
    blck_d = pilIm.resize(d_size)
    daemon = np.asarray(daemon.convert())/255.0
    blck_d = (np.asarray(blck_d.convert())/255.0)
    blck_d[:,:,1] = blck_d[:,:,0]
    blck_d[:,:,2] = blck_d[:,:,0]
    blck_d = blck_d/2
    daemon[np.invert(red_back[22:-22, 22:-22,:].astype(bool))] = 0

    red_daemon = red_back
    red_daemon[22:-22, 22:-22,:] = daemon

    with_blck = copy.deepcopy(red_daemon)
    with_blck[0:blck_d.shape[0],-blck_d.shape[1]:,:] = blck_d
    plt.text(6, 520, 'DAEMON', fontsize = 22, 
             bbox = dict(facecolor = 'white', alpha = 1))
    plt.imshow(with_blck)
def get_img_array():
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.axis('off')
    plot_total()
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8).reshape(fig.canvas.get_width_height()[::-1] + (3,))
    image_no_border = copy.deepcopy(image)[60:-60,330:-305,]
    plt.close()
    return image_no_border

fig = plt.figure()
im = plt.imshow(get_img_array(), animated=True)
def updatefig(*args):
    im.set_array(get_img_array())
    return im,


ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
plt.show()