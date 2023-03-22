import pandas as pd

class DataTransform:
    def __init__(self):
        pass
        
    def flatten_data(self, data):
        flattened_timetracks_df = pd.json_normalize(data, meta=['userId', 'dayOffset', 'date'], record_path='records')
        return flattened_timetracks_df
   
    def save_to_parquet(self, df, filename):
        df.to_parquet(filename)
        return
