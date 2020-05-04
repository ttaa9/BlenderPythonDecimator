import os, sys, subprocess

#TARGET_FOLDER = '/home/wug/.ttaa/3DR2N2-data/CARS-Gathered/FullSizeCarMeshes'
TARGET_FOLDER = '/home/wug/.ttaa/3DR2N2-data/PLANES' # CARS-Gathered/FullSizeCarMeshes'
NUM_FACES = 1200 #3500

#os.makedirs(OUT_FOLDER)
CMD = "blender -b -P blenderSimplifyNumFaces.py -- --nfaces %d --inm '%s' --outm '%s'"

for i, f in enumerate( os.listdir(TARGET_FOLDER) ):
    cf = os.path.join(TARGET_FOLDER, f)
    print(i, 'On', cf)
    #new_name = os.path.join(OUT_FOLDER, f.replace('.obj','-simp.obj'))
    new_name = "./" + f.replace('.obj','-simp.obj')
    curr_cmd = CMD % (NUM_FACES, cf, new_name)
    print('Running\n\t', curr_cmd)
    subprocess.run(curr_cmd, shell=True)



#
