import os

"""
Generate a list and mkdir for the simulations
"""

alphalist = [0, 1, 2, 3, 4]
betalist = [0, 1, 2, 5, 10, 100]

dirlist = []
for beta in betalist:
    if beta == 0:
        prefix = 'H'
        for alpha in alphalist:
            dirname = prefix + '%1i' % (alpha)
            dirlist.append(dirname)
    else:
        prefix = 'M'    
        for alpha in alphalist:
            dirname = prefix + '%1iB%i' % (alpha, beta)
            dirlist.append(dirname)
            
for dirname in dirlist:
    dirpath = os.path.join(os.curdir, dirname)
    if os.path.isdir(dirpath):
        print "dir exist: ", dirname
    else:
        os.mkdir(dirpath)
            
    
