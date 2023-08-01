"""!pip install google_images_search
"""
from google_images_search import GoogleImagesSearch
import zipfile
import os
# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
gis = GoogleImagesSearch('AIzaSyCGyqf36D5k3QghaZLhAqb1R2OUtRFraF8' , '0d386b282da5209ea' , validate_images=True)
def search(keyword, imageNumber):
    _search_params = {
        'q': keyword,
        'num': imageNumber,
        # 'safe': 'medium',
        # 'fileType': 'jpg',
        # 'imgType': 'photo',
        # 'imgSize': 'MEDIUM',
        # 'imgDominantColor': 'brown',
        # 'rights': 'cc_publicdomain'
    }

    #path_to_dir: where the downloaded images must be stored
    gis.search(search_params=_search_params, path_to_dir='./images/')

##calling search function to download 10 motorbike images
search('motorbike',10)
     