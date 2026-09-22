# Keck MIRA Codification

Code for the analysis tracking of health of Keck Obvervatory mirror segments via MIRA fits calibration images. 


## Getting Started

0. **Obtain data:** Download MIRA fits images from Keck 

1. **Sort images and get initial information:** Run `instrument_sort.py` to move Keck 1 (k1) or Keck 2 (k2) images into sorted directories according to instrument. `get_header_info.py` will print basic fits header information to screen, and `list_MIRA_dates.py` will save basic fits information (e.g. instrument, date of observation, image name) to a .csv file for a given Keck Telescope (or both).

2. 