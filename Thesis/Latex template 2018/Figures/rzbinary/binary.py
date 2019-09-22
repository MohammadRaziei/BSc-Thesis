from skimage.data import imread
import skimage.io as io
import numpy as np
def step(t,t0=0):
    shape = t.shape; size = t.size
    out = np.squeeze(t.reshape((size,1)))
    out = np.array([1 if i > t0 else 0 for i in out ])
    return out.reshape(shape)
def show(image):
    io.imshow(image,cmap='gray')
    io.show()

fileName = 'rzbinary_car-scheme.jpg'
image = np.array(imread(fileName,as_grey=True))

# show(image)
# print(np.max(image))

io.imsave(fileName+'.png',step(image,0.5))