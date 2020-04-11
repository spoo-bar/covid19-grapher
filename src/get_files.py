import requests
from requests.exceptions import RequestException

with open('url_list.txt', 'r') as urls:
    for csv_url in urls:
        csv_url = csv_url.strip()
        filename = csv_url.split('/')[-1]

        try:
            with requests.get(csv_url) as response:
                url_content = response.content
                with open(filename, 'wb') as csv_file:
                    csv_file.write(url_content)
                
        except RequestException as err:
            print('Downloading {csv_url} failed due to {err}')