import os
import requests

class YaUploader:
	def __init__(self, token: str):
		self.token = token

	def get_headers(self):
		return {
			'Content-Type': 'application/json',
			'Authorization': 'OAuth {}'.format(self.token)
		}

	def _get_upload_link(self, file_name):
		upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
		params = {'path': file_name, 'overwrite': 'true'}
		response = requests.get(upload_url, headers=self.get_headers(), params=params)
		return response.json()['href']

	def upload(self, file_path: str):
		"""Метод загружает файлы по списку file_list на яндекс диск"""
		# Тут ваша логика
		# Функция может ничего не возвращать
		upload_url = self._get_upload_link(os.path.basename(file_path))
		response = requests.put(upload_url, data=open(path_to_file, 'rb'), headers=self.get_headers())

if __name__ == '__main__':
	# Получить путь к загружаемому файлу и токен от пользователя
	path_to_file = input('Введите путь к файлу: ') 
	token = input('Введите токен: ') # Здесь вводится полученный на полигоне токен (токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен")
	ya = YaUploader(token)
	ya.upload(path_to_file)
