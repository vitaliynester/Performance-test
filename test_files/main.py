import random as r

from locust import HttpUser, task, between

from config import Config


class WebsiteUser(HttpUser):
    wait_time = between(1, 2.5)
    user_id = r.randint(1, Config.max_user_id)

    def on_start(self):
        self.client.get('/', name="Пользователь зашел на сайт")

    @task(1)
    def create_post(self):
        new_post = {'userId': self.user_id,
                    'title': 'new random title',
                    'body': 'new random title'}
        post_create_response = self.client.post('/posts', json=new_post, name="Создание нового поста")
        if post_create_response.status_code != 201:
            raise Exception('Не удалось создать пост')
        post_id = post_create_response.json().get('id')
        post_read_response = self.client.get(f'/posts/{post_id}', name=f'Чтение созданного поста')
        if post_read_response.status_code != 200:
            raise Exception(f'Не удалось прочитать созданный пост')

    @task(5)
    def read_post(self):
        post_id = r.randint(1, Config.max_post_id)
        post_read_response = self.client.get(f'/posts/{post_id}', name=f'Чтение поста')
        if post_read_response.status_code != 200:
            raise Exception(f'Не удалось прочитать пост')

    @task(2)
    def create_comment(self):
        post_id = r.randint(1, Config.max_post_id)
        new_comment = {'postId': post_id,
                       'name': 'new comment name',
                       'email': 'example@mail.ru',
                       'body': 'test body'}
        comment_create_response = self.client.post('/comments', json=new_comment, name="Создание нового комментария")
        if comment_create_response.status_code != 201:
            raise Exception(f"Не удалось создать комментарий к посту")
        comment_id = comment_create_response.json().get('id')
        comment_read_response = self.client.get(f'/comments/{comment_id}',
                                                name=f"Чтение созданного комментария")
        if comment_read_response.status_code != 200:
            raise Exception(f"Не удалось прочитать созданный комментарий")

    @task(10)
    def read_comment(self):
        comment_id = r.randint(1, Config.max_comment_id)
        comment_read_response = self.client.get(f'/comments/{comment_id}', name=f"Чтение комментария")
        if comment_read_response.status_code != 200:
            raise Exception(f"Не удалось прочитать комментарий")

    @task(2)
    def create_album(self):
        new_album = {'userId': self.user_id,
                     'title': 'new album title'}
        album_create_response = self.client.post('/albums', json=new_album, name="Создание нового альбома")
        if album_create_response.status_code != 201:
            raise Exception(f"Не удалось создать альбом для пользователя {self.user_id}")
        album_id = album_create_response.json().get('id')
        album_read_response = self.client.get(f'/albums/{album_id}', name=f"Открытие созданного альбома")
        if album_read_response.status_code != 200:
            raise Exception(f"Не удалось открыть созданный альбом")

    @task(10)
    def read_album(self):
        album_id = r.randint(1, Config.max_albums_id)
        album_read_response = self.client.get(f'/albums/{album_id}', name=f"Открытие альбома")
        if album_read_response.status_code != 200:
            raise Exception(f"Не удалось открыть альбом")

    @task(5)
    def create_photo(self):
        album_id = r.randint(1, Config.max_albums_id)
        new_photo = {'albumId': album_id,
                     'title': 'new photo title',
                     'url': "http://vk.com/id1",
                     'thumbnailUrl': "http://vk.com/id1"}
        photo_create_response = self.client.post('/photos', json=new_photo, name="Создание новой фотографии")
        if photo_create_response.status_code != 201:
            raise Exception(f"Не удалось создать фото для албома")
        photo_id = photo_create_response.json().get('id')
        photo_read_response = self.client.get(f'/photos/{photo_id}', name=f"Открытие созданной фотографии")
        if photo_read_response.status_code != 200:
            raise Exception(f"Не удалось открыть созданную фотографию")

    @task(20)
    def read_photo(self):
        photo_id = r.randint(1, Config.max_photos_id)
        photo_read_response = self.client.get(f'/photos/{photo_id}', name=f'Открытие фотографии')
        if photo_read_response.status_code != 200:
            raise Exception(f"Не удалось открыть фотографию")

    @task(10)
    def create_todo(self):
        new_todo = {'userId': self.user_id,
                    'title': 'new todo title',
                    'completed': bool(r.getrandbits(1))}
        todo_create_response = self.client.post('/todos', json=new_todo, name="Создание новой задачи")
        if todo_create_response.status_code != 201:
            raise Exception(f"Не удалось создать задачу для пользователя {self.user_id}")
        todo_id = todo_create_response.json().get('id')
        todo_read_response = self.client.get(f'/todos/{todo_id}', name=f"Открытие созданной задачи")
        if todo_read_response.status_code != 200:
            raise Exception(f"Не удалось открыть созданную задачу")

    @task(20)
    def read_todo(self):
        todo_id = r.randint(1, Config.max_todos_id)
        photo_read_response = self.client.get(f'/todos/{todo_id}', name=f'Открытие задачи')
        if photo_read_response.status_code != 200:
            raise Exception(f"Не удалось открыть задачу")
