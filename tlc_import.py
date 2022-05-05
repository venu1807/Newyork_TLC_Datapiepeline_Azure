import os
import csv
from _ast import List
import requests
import pandas as pd


class TlcDataImport:
    """
    This is the class for importing Newyork Taxi and Limousine Commission (TLC) Trip Record Data
    from their source into our local machine.
    """
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def pre_setup(self):
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)

    def prepare_data_url(self,start_month,end_month)-> str:
        """
        This method is used for preparing the URL of the trip record of green and yellow taxis.
        :param start_month:
        :param end_month:
        :return: URL of the file to be downloaded
        """
        urls=[]
        months = pd.date_range(start_month, end_month, freq='MS').strftime("%Y-%m").tolist()
        travels = ['yellow', 'green', 'fhv']
        #travels = ['yellow', 'green']
        for month in months:
            for travel in travels:
                url='http://s3.amazonaws.com/nyc-tlc/trip+data/{}_tripdata_{}.csv'.format(travel, month)
                print(f'The file is: {url}')
                urls.append(url)
        return urls

    def download_to_csv(self, data_urls) -> None:
        """
        This method downloads the trip record data into local directory
        :param data_urls:
        :return: None
        """
        for data_url in data_urls:
            file_name = data_url.split('/')[-1]
            r = requests.get(data_url)
            if r.status_code == 200:
                print(f'The trip record exists at {data_url} and started downloading.......')
                with open('./TLC_Data/' + file_name, 'wb') as f:
                    f.write(r.content)
                print(f'The file {file_name} has been downloaded.')
            else:
                print(f'The trip record for {file_name} doesnot exists and havenot uploaded by the authors.')


    def main(self):
        """
        This main method calls the required methods to download the csv files
        :return: None
        """
        self.pre_setup()
        urls = self.prepare_data_url('2019-01', '2019-12')
        self.download_to_csv(urls)


if __name__ == '__main__':
    output_dir = './TLC_Data'
    data_import = TlcDataImport(output_dir)
    data_import.main()