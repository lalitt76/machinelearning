
import os
import requests
from pathlib import Path
from zipfile import ZipFile

def download_data(source: str,
                  destination: str,
                  remove_source: bool = True) -> Path:
    """Downloads a zipped dataset from source and unzips to destination."""

    # Setup path to data folder
    data_path = Path("data/")
    image_path = data_path / destination
    target_file = Path(source).name # Spit out zip file name
    target_file_path = data_path / target_file

    # Checking if data is already there
    image_files = list(Path(image_path).glob("*/*/*.jpg"))


    if len(image_files):
              print(f"[INFO] Found {len(image_files)} images in {image_path}. \
      \nSkipping downloading data")
    else:
        print(f"[INFO] Did not find any images in {image_path}, creating...")
        image_path.mkdir(parents=True, exist_ok=True)

        # Downloading the target data; wb = write binary
        with open(target_file_path, "wb") as f:
            request = requests.get(source)
            print(f"[INFO] Downloading {target_file} from {source}...")
            f.write(request.content)

        # Unzipping the data
        with ZipFile(target_file_path, "r") as zip_ref:
            print(f"[INFO] Unzipping {target_file} data...")
            zip_ref.extractall(image_path)

        # Remove the unwanted zip file
        if remove_source:
            os.remove(target_file_path)

    return image_path

# # Download the data
# source = "https://github.com/mrdbourke/pytorch-deep-learning/raw/main/data/pizza_steak_sushi.zip"
# destination = "pizza_steak_sushi"
# download_data(source, destination)
