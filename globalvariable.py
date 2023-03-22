x="good"
def myfunc():
  global x
  x = "fantastic"
  print("inside Python is " + x)
myfunc()

print(" outside Python is " + x)