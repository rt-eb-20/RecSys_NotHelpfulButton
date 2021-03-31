import pandas as pd
import re


class ReadData:

    def __init__(self):
        pass

    def read_file(self, file_path, sampling_size):

        df = pd.read_csv(file_path,
                         compression='zip',
                         sep=',',
                         index_col=0)

        if sampling_size:
            return df.sample(sampling_size)
        else:
            df

    @staticmethod
    def extract_helpful_information(dataframe):

        not_helpful = pd.Series(dataframe.helpful.apply(lambda x: re.findall(r'\d+', x)[0]))
        helpful = pd.Series(dataframe.helpful.apply(lambda x: re.findall(r'\d+', x)[1]))
        dataframe['not_helpful_count'] = not_helpful.astype(int)
        dataframe['helpful_count'] = helpful.astype(int)

        return dataframe

    @staticmethod
    def time_manipulation(dataframe):

        dataframe.reviewTime = pd.to_datetime(dataframe.reviewTime)
        dataframe['reviewYear'] = dataframe.reviewTime.dt.year

        return dataframe