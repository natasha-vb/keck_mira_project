from astropy.io import fits
import glob
import os
import shutil

# choose either 'k1' or 'k2' for Keck 1 or Keck 2 
keck_tel = 'k2'

imgs = glob.glob(f'{keck_tel}/*.fits')

# find instrument used in fits header
for im in imgs:
    print(im)
    try:
        hdu = fits.open(im)
        hdr = hdu[0].header

        try:
            inst = hdr['CURRINST']
            print(inst)
            print('-CURRINST keyword used')
        except KeyError:
            inst = hdr['INSTRUME']
            print(inst)
            print('-INSTRUME keyword used')
        # except:
        #     print('no current instrument')
        print('-' * 15)
        print('')

        # save and move to instrument directory 
        dir_name = f'./{keck_tel}/{inst}'

        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
        
        shutil.move(im, dir_name+'/'+im.split('/')[1])
        print(f'file moved to {dir_name+'/'+im.split('/')[1]}')

    except OSError:
        print('FITS FILE IS EMPTY!')

    
