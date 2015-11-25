import os
import f90nml

for (dirpath, dirnames, filenames) in os.walk(os.curdir):
#    print  (dirpath, dirnames, filenames) 
    
    if dirpath.endswith('s1'):
        print "dirpath = ", dirpath
        if 'para.nml' in filenames:
            print "para.nml exists"
            os.chdir(dirpath)
            f0 = f90nml.read('para.nml')
            f1 = f0.copy()
            f1['run_params']['ncell'] = [256, 1024, 0]
            f1.write('para1.nml', force=True)
            os.chdir(os.path.dirname(os.getcwd()))