import os
import logging


SPEEDTEST_CMD = 'C:/Users/User/AppData/Local/Programs/Python/Python37-32/Scripts/speedtest'
LOG_FILE = 'speedtest.log'

def main():
    
    setup_logging()
    try:
        ping, download, upload = get_speedtest_results()
    
    except ValueError as err:
        logging.info(err)

    else:
        logging.info(f"{ping:5.1f} {download:5.1f} {upload:5.1f}")


def setup_logging():

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M",
    )

def get_speedtest_results():
    """
    Run test and parse results.
    Returns tuple of ping speed, download speed, and upload speed,
    or raises ValueError if unable to parse data.
    """

    ping = download = upload = None

    with os.popen(SPEEDTEST_CMD + ' --simple') as speedtest_output:

        for line in speedtest_output:

            label, value, unit = line.split()
            if 'ping' in label:
                ping = float(value)

            elif 'Download' in label:
                download = float(value)

            elif 'Upload' in label:
                upload = float(value)

    if all((ping, download, upload)): # if all 3 values were parsed
        return ping, download, upload

    else:
        raise ValueError("TEST FAILED")

def read_data():

    df = pd.io.parsers.read_csv(
        'speedtest.log',
        names = 'date time ping download upload'.split(),
        header=None,
        sep=r'\s+',
        parse_dates={'timestamp':[0,1]},
        na_values=['TEST', 'FAILED'],
    )

    print(df)
    return df[-48:] # return last 48 rows of data (i.e., 24 hours)


if __name__ == "__main__":
    main()

"""
Sample log file output:

...
2015-02-11 08:30 36.2 16.0   1.1
2015-02-11 09:00 35.4 14.2   1.1
2015-02-11 09:30 34.5 13.8   1.1
2015-02-11 10:00 31.7 16.1   0.9
2015-02-11 10:30 35.3 15.7   1.1
2015-02-11 11:00 35.4 14.2   1.1
2015-02-11 11:30 34.3 15.3   1.1
2015-02-11 12:00 92.2 16.0   1.1
2015-02-112:30 35.0 15.9   1.1
...
"""
