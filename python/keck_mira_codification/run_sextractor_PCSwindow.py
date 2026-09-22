import glob
import numpy as np
import os
import pandas as pd
import re
import subprocess
import time as t

# SE parameters
savecats_dir   = f"./cats/"
sextractor_loc = "/fred/oz100/containers/commands/sex"
psfex_loc      = "/fred/oz100/containers/commands/psfex"
fwhm           = 1.2 #default setting 1.2
detect_minarea = 5   #default setting 5
detect_thresh  = 4 #default setting 1.5
VERBOSE_TYPE   = 'NORMAL'

nnw_path    = f"../default.nnw"
conv_path   = f"../default.conv"
config_path = f"../mira.sex"
params_path = f"../default.param"

print('CATALOG DIRECTORY: %s\n' % savecats_dir)

# Grab images in PCS window
img_path = '/home/nvbemmel/ADACS_keck_project/k1/LRISADC/'
PCS_start = 2318
PCS_end   = 2443

for fname in os.listdir('../../../k1/LRISADC/'):
    if PCS_start <= int(fname.split('_')[0]) <= PCS_end:
        f_path = img_path + fname

        catalog_name = savecats_dir + fname.replace('.fits', '.cat')
        
        # Run SE on image
        print('========================')
        print('RUNNING SOURCE EXTRACTOR')
        print('========================')
        print('FITS FILE:', f_path)
        print()

        start_time = t.time()

        command =  f'{sextractor_loc} -c {config_path} '\
                    f'-CATALOG_NAME {catalog_name} '\
                    f'-CATALOG_TYPE ASCII_HEAD '\
                    f'-PARAMETERS_NAME {params_path} -FILTER_NAME {conv_path} '\
                    f'-STARNNW_NAME {nnw_path} -PIXEL_SCALE 0 '\
                    f'-VERBOSE_TYPE {VERBOSE_TYPE} '\
                    f'-SEEING_FWHM {fwhm} -DETECT_MINAREA {detect_minarea} -DETECT_THRESH {detect_thresh} '\
                    f'{f_path}'

        print(command)

        try:
            rval = subprocess.run(command.split(), check=True)
            print(f'Success! Catalog saved: {catalog_name}\n')
        except subprocess.CalledProcessError as err:
            print('\nCould not run SExtractor with exit error %s\n'%err)
            print('Command used:\n%s\n'%command)

        end_time = t.time()
        time_diff = end_time - start_time

        print()
        print(f'Time taken for Source Extractor: {np.round(time_diff,3)} seconds')
        print('*****************************************************************')
        print()