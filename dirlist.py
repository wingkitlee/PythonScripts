import os
import shutil

"""
List the directories 
"""

dirlist = [d for d in os.listdir(os.curdir) if (os.path.isdir(d) and d[0] in ['H','M'])]

if dirlist == []:
    print "Directories do not exist. "
    
# list of files to be copied
listoffiles = ['para.nml', 'antares2d', 'job_openmpi.sh']
    
for d in dirlist:
    if not d.endswith('s1'):
        newd = d + 's1'
        if not os.path.isdir(newd):
            os.mkdir(newd)
            for f in listoffiles:
                print f
                if os.path.isfile(os.path.join(d,f)):
                    print "yes."
                    shutil.copy(os.path.join(d,f),newd)
                    print "file copied: ", f
        else:
            print "Directory exists: ", newd
            for f in listoffiles:
                print f
                if os.path.isfile(os.path.join(d,f)):
                    print "yes."
                    shutil.copy(os.path.join(d,f),newd)
                    print "file copied: ", f