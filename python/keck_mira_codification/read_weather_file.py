import argparse
import calendar
import pandas as pd
import re


parser = argparse.ArgumentParser(description="Read Maunakea weather file and return weather information from a given date "
                                             "in YYYY-MM-DDThh:mm:ss UT format")
parser.add_argument(
        "--date",
        type = str,
        help = "Date of observation"
)
args = parser.parse_args()


# Read in Maunakea weather file from: http://mkwc.ifa.hawaii.edu/current/seeing/analysis/catalog/ 
df = pd.read_csv('../../../data/maunakea_weather.txt',sep='\t')

# Read in UT date and transform to searchable format for weather file
ut_date = args.date
ut_date_split = re.split('-|T', ut_date)

ut_month = ut_date_split[1]
month = calendar.month_abbr[int(ut_month)]
day = int(ut_date_split[2])
year = int(ut_date_split[0]) 

date_str = f'{month} {day}, {year}'
print(date_str)

# Search weather catalog for specified date
try:
    date_weather = df[df['Date'].str.contains(date_str)]
    print(date_weather)
except Exception:
    print('Date was not found in weather catalog')