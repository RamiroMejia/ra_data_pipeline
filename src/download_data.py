
# Script to execute Interact with kaggle API and download the data

import os
import zipfile
import shutil
from kaggle.api.kaggle_api_extended import KaggleApi

# Set up your Kaggle credentials
api = KaggleApi()
api.authenticate()

# Download the Instacart Market Basket Analysis dataset

dataset_name = 'instacart-market-basket-analysis'
download_path = '../data/download'

os.makedirs(download_path, exist_ok=True)

# Download the dataset files
api.competition_download_files(dataset_name, path=download_path)



def extract_nested_zips(directory_path):
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)

        if zipfile.is_zipfile(file_path):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(directory_path)

            os.remove(file_path)

            extract_nested_zips(directory_path)

    print("Download succesfully!")

    # Remove the __MACOSX folder
    macosx_folder = os.path.join(directory_path, '__MACOSX')
    if os.path.exists(macosx_folder) and os.path.isdir(macosx_folder):
        shutil.rmtree(macosx_folder)


# Call the function to extract all nested zip files
extract_nested_zips(download_path)