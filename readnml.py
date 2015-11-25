import f90nml

f0 = f90nml.read('para.nml')
f1 = f0.copy()

f1['run_params']['ncell'] = [256, 1024, 0]
print f1['run_params']['ncell']

f1.write('para1.nml', force=True)

