from datetime import *
import pandas as pd

UTC_OFSET_TIMEDELTA = datetime.utcnow() - datetime.now()


def convert_date_string_to_ts(date_string):
    # date_string format is 'YYYY/MM/DD'
    
    year, month, day = [int(date_info) for date_info in date_string.split("/")]
    dtime = datetime(year,month,day) + UTC_OFSET_TIMEDELTA
    ts = int(dtime.timestamp())
    
    return ts

def save_result_data(dict_list, file_path):
    result_df = pd.DataFrame(dict_list)
    result_df.to_csv(file_path)