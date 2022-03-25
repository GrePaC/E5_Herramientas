import numpy
def demianKernel():
  k3 = numpy.zeros((3,3))
  for x in range(0,3):
    for y in range(0,3):
      cx=x-1
      cy=y-1
      k3[x,y]=cx*cy
  return demianKernel