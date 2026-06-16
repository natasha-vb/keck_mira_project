from astropy.io import fits
import glob

# choose either 'k1' or 'k2' for Keck 1 or Keck 2 
keck_tel = 'k2'

imgs = glob.glob(f'{keck_tel}/*/*.fits')

# clear text file 
with open(f"{keck_tel}/{keck_tel}_header_info.txt", "w") as f:
    f.write("")
 

# find instrument used in fits header
for im in imgs:
    with open(f'{keck_tel}/{keck_tel}_header_info.txt', 'a') as f:
        f.write(f'{im}\n')
        try:
            hdu = fits.open(im)
            hdr = hdu[0].header
            
            try:
                f.write(f'CURRINET: {hdr["CURRINST"]}\n')
            except KeyError:
                f.write('no current instrument\n')
            f.write(f'INSTRUME: {hdr["INSTRUME"]}\n')
            f.write(f'header length: {len(hdr)}\n')
            f.write('--------\n')
        
        except OSError:
            f.write('FITS FILE IS EMPTY!\n')