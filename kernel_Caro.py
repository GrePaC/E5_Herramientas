
sharpen = numpy.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

def sin_func():
  A = numpy.zeros((3,3))
  for x in range (-1, 2):
    for y in range (-1, 2):
      A[x][y] = (math.sin(x) + y)
      print(A)
  return A
