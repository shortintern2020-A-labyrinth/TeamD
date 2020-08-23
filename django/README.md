## プロジェクト構成

https://www.django-rest-framework.org/tutorial/quickstart/

- example
  - projectの設定
- company
  - 企業に関する操作をするためのロジック
- movie
  - 動画加工に関するロジック
- youtube
  - youtubeAPIを利用するためのロジック

## migrate の手順
１．model.py上のクラス定義を変更する
２．マイグレーションファイルの作成
manage.py makemigrations
３．マイグレーションで実行されるSQLの確認
manage.py sqlmigrations マイグレーションID
４．マイグレーションの実行
manage.py migrate
５．データベースクライアント等で適用結果を確認



### rollbackしたいとき

- 特定のmigrateに対して
  - ./manage.py migrate app_name [一つ前のmigrateID]
- 全てのmigrate
  - ./manage.py migrate app_name zero



# Django-starter-kit

Django Starter Kit

## Description

yoshikawa/django-starter-kit − learning about Django REST framework

### requirements

|Lang/FrameWork|Version|
|:--|--:|
|Python|3.8.5|
|Django|3.1|
|Django REST framework|3.11.1|
|django-cors-headers|3.4.0|

Please check it!
[Django REST framework](https://github.com/encode/django-rest-framework)
[django-cors-headers](https://github.com/adamchainz/django-cors-headers)

## Usage

Install using `pip`.

```sh
pip install django
pip install djangorestframework
pip install django-cors-headers
```

Add 'rest_framework',  'corsheaders' to your INSTALLED_APPS setting.(**We have already set.**)

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
]
```

Add 'corsheaders.middleware.CorsMiddleware', 'django.middleware.common.CommonMiddleware' to your MIDDLEWARE setting.(**We have already set.**)

```python
MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]
```

Add CORS_ORIGIN_WHITELIST to your setting (for the local-environment).(**We have already set.**)

```python
CORS_ORIGIN_WHITELIST = (
    'localhost:3000/'
)
```


### Backend Server

```sh
./manage.py runserver
```

You can now open the API in your browser at `http://127.0.0.1:8000/`, and view your new 'users' API. If you use the `Login` control in the top right corner you'll also be able to add, create and delete users from the system.

You can also interact with the API using command line tools such as [`curl`](https://curl.haxx.se/). For example, to list the users endpoint:

```sh
$ curl -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/users/
[
    {
        "url": "http://127.0.0.1:8000/users/1/",
        "username": "admin",
        "email": "admin@example.com",
        "is_staff": true,
    }
]
```

Or to create a new user:

```sh
$ curl -X POST -d username=new -d email=new@example.com -d is_staff=false -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/users/
{
    "url": "http://127.0.0.1:8000/users/2/",
    "username": "new",
    "email": "new@example.com",
    "is_staff": false,
}
```

## Contribution

1. [Fork it](https://github.com/yoshikawa/django-starter-kit/fork)
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. reate new Pull Request

## Licence

[WTFPL](https://github.com/yoshikawa/django-starter-kit/blob/master/LICENSE)

## Author

[Yoshikawa Taiki](https://github.com/yoshikawa)
