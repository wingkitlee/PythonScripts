import os

print "current dir: ", os.curdir
print "full path", os.path.join(os.curdir,'this')

thispath = os.path.join(os.curdir,'this')


if os.path.isdir(thispath):
    
os.mkdir(thispath)

print "does this dir exist? ", os.path.isdir(thispath)
