import matplotlib.pyplot as plt
import numpy

k3 = numpy.array([[-1,-1,-1],[-1,-8,-1],[-1,-1,-1]])

def k3(size):
  A = numpy.zeros((size,size))
  for x in range (-size//2,(size//2)+1):
    for y in range (-size//2,(size//2)+1):
      inside = (x-y)**2
      inside = (-1 * inside)/ (2 * x)**2
      A[x][y] = numpy.exp(inside)
      print(A)
    return A

    J3 = ndimage.convolve(I, k3(5), mode='constant', cval=0.0)