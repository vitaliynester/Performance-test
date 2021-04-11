## Лабораторная работа №6 по дисциплине "Технологии разработки программного обеспечения"

### Задача:

Необходимо разработать и произвести тестирование производительности веб-сервиса.

### Ход работы:

Для примера сервиса была взята библиотека JSON-Server для NodeJS. Данная библиотека предлагает получить REST API сервис
исходя из строения переданного JSON файла.

Переданный JSON файл представляет собой следующую структуру, которую можно
найти [здесь](https://github.com/vitaliynester/Performance-test/blob/master/server_files/db_example.json), а также ниже:

- Пост:
    ```json
    {
      "userId": 1,
      "id": 1,
      "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
      "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }
    ```
- Комментарий
    ```json
    {
      "postId": 1,
      "id": 1,
      "name": "id labore ex et quam laborum",
      "email": "Eliseo@gardner.biz",
      "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
    }
    ```
- Альбом
    ```json
    {
      "userId": 1,
      "id": 1,
      "title": "quidem molestiae enim"
    }
    ```
- Фотография
    ```json
    {
      "albumId": 1,
      "id": 1,
      "title": "accusamus beatae ad facilis cum similique qui sunt",
      "url": "https://via.placeholder.com/600/92c952",
      "thumbnailUrl": "https://via.placeholder.com/150/92c952"
    }
    ```
- Пользователь
    ```json
    {
      "id": 1,
      "name": "Leanne Graham",
      "username": "Bret",
      "email": "Sincere@april.biz",
      "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
          "lat": "-37.3159",
          "lng": "81.1496"
        }
      },
      "phone": "1-770-736-8031 x56442",
      "website": "hildegard.org",
      "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets"
      }
    }
    ```
- Задача
    ```json
    {
      "userId": 1,
      "id": 1,
      "title": "delectus aut autem",
      "completed": false
    }
    ```

### Разворачивание проекта

Проект состоит из двух подпроектов:

1. Fake JSON-Server (NodeJS 15.14.0)
2. Python проект с использованием Locust (Python 3.9.2)

Запустить проект на собственном компьютере можно двумя способами:

#### Способ первый (без использования Docker)

1. Необходимо склонировать данный репозиторий к себе, сделать это можно с помощью следующей команды:

```bash
git clone https://github.com/vitaliynester/Performance-test.git
```

2. Перейдите в папку с загруженным проектом:

```bash
cd Performance-test
```

3. Запустите подпроект с JSON-Server

```bash
cd server_files && npm install && npm json-server --watch <db_file.js>
```

Данная команда установить все необходимые зависимости для сервера и запустит его с отслеживанием файла db_file.js.

4. Перейдите в каталог с тестированием нагрузки

```bash
cd ../ && cd test_files && pip install -r requirements.txt && locust -f main.py
```

Данная команда установит все необходимые зависимости для тестирования и запустит веб-интерфейс сервиса.

5. Запуск нагрузочного тестирования

После выполнения предыдущих шагов (по умолчанию) будет запущен JSON-Server на порте 3000 и веб-интерфейс тестирования на
порте 8089. Перейти к ним можно по [этой](http://localhost:3000) и [этой](http://localhost:8089) ссылке соответственно.

#### Способ второй (использование Docker)

1. Необходимо склонировать данный репозиторий к себе, сделать это можно с помощью следующей команды:

```bash
git clone https://github.com/vitaliynester/Performance-test.git
```

2. Перейдите в папку с загруженным проектом:

```bash
cd Performance-test
```

3. Запустить сборку контейнеров:

```bash
docker-compose up --build
```

После выполнения предыдущей команды будут собраны два контейнера.

4. Получение IP адреса JSON-Server для проведения тестирования

Чтобы получить IP адрес контейнера необходимо выполнить следующие действия:

* Выполнить команду для просмотра активных контейнеров:

```bash
docker ps
```

* Найти контейнер с запущенным JSON-Server
* Выполнить команду для получения IP адреса контейнера:

```bash
docker inspect <container_name> | grep "IPAddress"
```

Пример выполнения вышеперечисленных команд представлен ниже:

```bash
vitaly_posadnev@MacBook-Air-Vitaly ~ % docker ps
CONTAINER ID   IMAGE                         COMMAND                  CREATED          STATUS          PORTS                    NAMES
d79a85bff559   lab6performancetest_testing   "locust -f main.py"      30 seconds ago   Up 28 seconds   0.0.0.0:8090->8089/tcp   lab6performancetest_testing_1
312919f2558f   lab6performancetest_db        "docker-entrypoint.s…"   53 minutes ago   Up 29 seconds   0.0.0.0:3020->3020/tcp   lab6performancetest_db_1
vitaly_posadnev@MacBook-Air-Vitaly ~ % docker inspect 312919f2558f | grep "IPAddress"
            "SecondaryIPAddresses": null,
            "IPAddress": "",
                    "IPAddress": "172.18.0.2",
vitaly_posadnev@MacBook-Air-Vitaly ~ % 
```