"""yf_example3.py
download stock price data for Qantas for a given year and save the information in a CSV file.
"""

import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year:int):

    """ qan_prc_to_csv
    Download Qantas stock prices for a given year into a CSV file

    Parameters
    ----------
    year:an integer
    """

    tic = "QAN.AX"
    start=f"{year}-01-01"
    end=f"{year+1}-01-01"   #including the last day of the year
    fn=f"qan_prc_{year}.csv"
    pth=os.path.join(cfg.DATADIR,fn)
    df = yf_example2.yf_prc_to_csv(tic,pth,start,end)

if __name__ == "__main__" :
    qan_prc_to_csv(year=2020)