import os
import requests


def download_data(file_path, file_name, url):
    """
    Function made to perform data downloads from an url to an
    specific folder
    :param file_path:
    :param file_name:
    :param url:
    :return:
    """
    full_path = os.path.join(file_path, file_name)
    try:
        os.makedirs(file_path, exist_ok=True)
        response = requests.get(url)
        if response.status_code == 200:
            with open(full_path, "wb") as file:
                file.write(response.content)

        return response.status_code
    except Exception as e:
        print(str(e))
