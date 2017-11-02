class test:
  "This is test"
  def __init__(self, i=0, j=0):
    self.i = i
    self.j = j
    print(j)
  def getdata(self):
    print(self.i)

ob1 = test(1,2)
#ob1.attr = 2
ob1.getdata()


