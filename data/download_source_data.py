import os

import requests
from requests.exceptions import RequestException

temp_folder = "tmp"
os.chdir("data")
try:
    os.mkdir(temp_folder)
except OSError:
    print(f"Creation of the directory {temp_folder} failed")
    exit(1)


with open("data_source_urls.txt", "r") as urls:
    for csv_url in urls:
        csv_url = csv_url.strip()
        filename = temp_folder + "/" + csv_url.split("/")[-1]
        try:
            with requests.get(csv_url) as response:
                url_content = response.content
                with open(filename, "wb") as csv_file:
                    csv_file.write(url_content)
        except RequestException as err:
            print(f"Downloading {csv_url} failed due to {err}")
