# Keck MIRA Codification

Code for the analysis tracking of health of Keck Obvervatory mirror segments via MIRA fits calibration images. 


## Getting Started

0. **Obtain data:** Download MIRA fits images from Keck 

1. **Sort images and get initial information:** Run `instrument_sort.py` to move Keck 1 (k1) or Keck 2 (k2) images into sorted directories according to instrument. `get_header_info.py` will print basic fits header information to screen, and `list_MIRA_dates.py` will save basic fits information (e.g. instrument, date of observation, image name) to a .csv file for a given Keck Telescope (or both).

2. **Image analysis:** To determine the fits file range over which to perform analysis, and create a list of these images, run `MIRA_PCS_dates.ipynb`. This will inform you of the MIRA range, to enter into `run_sextractor_PCSwindow.py` to run Source Extractor [^1]. 

3. **MIRA Diagnostics:** Finally, run `pipeline_4PCS_LRIS.ipynb` which is currently setup to run over 4 PCS windows. This script will gather the Source Extractor catalog files, append relevant fits header information, assess image quality, create an ideal hexagon model and measure each segment's distance from the model, then perform a simple subtraction. The output of all this information is saved in a .csv file.


[^1]: Source Extractor manual and how to install: https://sextractor.readthedocs.io/en/latest/
