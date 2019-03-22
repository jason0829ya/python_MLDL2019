import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import ipywidgets as wg

all_images = ['0.jpg', '1.jpg', '2.jpg', '3.jpg', '4.jpg']
path = '/home/jason123/workspace/phton_MLDL2019/interactive_practice/'

def plot(index):
   lena = mpimg.imread(path + all_images[index])

   plt.imshow(lena)
   plt.axis('off')
   plt.show()
    

wg.interactive(plot, index=wg.IntSlider(min=0,max=len(all_images) -1,step=1,value=0))
print('======test======')