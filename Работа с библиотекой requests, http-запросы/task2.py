import requests
from pprint import pprint

HADERS = {'Authorization': 'OAuth твой_скопированный токен' } # В Яндексе необходимо указывать токен в формате 'Authorization': 'OAuth твой_скопированный токен'

class YaUploader:
    def __init__(self, token: str):
        self.token = token
        resp1 = requests.get(
            'https://cloud-api.yandex.net/v1/disk/resources/upload',
            params={'path': '/avesome2.gif', 'overwrite': 'true'},
            headers=token
        )
        resp1.raise_for_status()
        d = resp1.json()
        global href
        href = d['href']

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        # Тут ваша логика

        with open(file_path, 'rb') as f:
            resp2 = requests.put(href, files={'file': f})

        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader(HADERS)
    result = uploader.upload('../../dz1_Python/lecture9_gifs/Obey the Flame.gif')
