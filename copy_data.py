import os 
import shutil
import ipdb 
st= ipdb.set_trace

root = '/home/shamitl/projects/output/'
ext = ['CLEVR_SINGLE_LARGE_SPHERE_256_A','CLEVR_SINGLE_LARGE_SPHERE_256_B','CLEVR_SINGLE_LARGE_SPHERE_256_C']
dest = '/projects/katefgroup/datasets/stylegan_datasets/clevr_single_sphere_large'

for e in ext:
    dirname = os.path.join(root, e, 'images','train')
    folders = [os.path.join(dirname,f) for f in os.listdir(dirname) if os.path.isdir(os.path.join(dirname, f))]
    for f in folders:
        print('copying {}'.format(f))
        os.system('cp -r {} {}'.format(f, dest))
