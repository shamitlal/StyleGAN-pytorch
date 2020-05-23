import os 
import ipdb 
st = ipdb.set_trace
dest = '/projects/katefgroup/datasets/stylegan_datasets/clevr_single_sphere_large'

folders = [os.path.join(dest,f) for f in os.listdir(dest) if os.path.isdir(os.path.join(dest,f))]
for f in folders:
    images = [os.path.join(f,img) for img in os.listdir(f) if img.endswith('png')]
    for img in images:
        if os.path.getsize(img)<10:
            os.system('rm  {}'.format(img))