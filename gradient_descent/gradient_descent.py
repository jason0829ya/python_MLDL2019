import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as wg


def lossFunction(x):
 return x**4 + 3*x**3 + (x-1)**2 + x

def lossFunction_grad(x):
   return 4*x**3 + 9*x**2 + 2*(x-1) + 1


x = np.linspace(-2.5, 0.5, num=100)
lr = 0.001

def GradientDescent(iterator):
   plt.clf()
   curposit = -2.5
   for i in range(iterator):
      curposit = curposit - lr * lossFunction_grad(curposit)

   current_loss = lossFunction(curposit)
   plt.scatter(curposit, current_loss, color='red')
   plt.plot(x, lossFunction(x))
   plt.show()
    

wg.interact(GradientDescent, iterator=wg.IntSlider(min=0, max=100, step=1, value=0))