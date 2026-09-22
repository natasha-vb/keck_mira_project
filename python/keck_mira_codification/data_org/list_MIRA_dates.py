from astropy.io import fits
import glob
import numpy as np
import pandas as pd
import regex as re

# choose either 'k1' or 'k2' for Keck 1 or Keck 2 
# or '*' for both
keck_tel = '*'

imgs = glob.glob(f'{keck_tel}/*/*.fits')

dates_df = pd.DataFrame(columns=['date', 'datetime', 'date_obs', 'telescope', 'instrument', 'image_name'])

# find date, keck telescope, and instrument used in fits header
for im in imgs:
    print(f'IMAGE: {im}')

    if re.search('raw', im) or re.search('sky', im):
        print('is a calibration image')
        print('skipping...\n')
    else:
        try:
            hdu = fits.open(im)
            hdr = hdu[0].header
            
            date = hdr["DATE-OBS"] 
            k_tel = im.split('/')[0]
            inst = hdr["INSTRUME"]
            im_name = im.split('/')[-1]
            try:
                date_obs = hdr["DATE_BEG"]
            except:
                date_obs = np.nan
            try:
                datetime = (hdr["DATE-OBS"] + 'T' + hdr['UTC']).split('.')[0]
            except:
                date_obs = np.nan

            temp_df = pd.DataFrame({'date':[date], 'datetime':[datetime], 'date_obs':[date_obs], 'telescope':[k_tel], 'instrument':[inst], 'image_name':[im_name]})

            dates_df = pd.concat([dates_df, temp_df], axis=0)
            print('data added to table\n')

        except OSError:
            print('FITS FILE IS EMPTY!\n')


dates_df.to_csv('MIRA_image_dates.csv')
print('table saved!')
