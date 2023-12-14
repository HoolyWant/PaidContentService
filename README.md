**Дипломный проект «Платформа для публикаций платного контента»**

Цель проекта:
Создание веб-приложения, на котоом пользователь может размещать как бесплатный контент для неавторизованных пользователей, так и платный, который могут видеть подписчики сервиса.
Перед началом работы:
Скачайте в домашнюю директорию.

Создайте виртуальное окружение poetry командой:

poetry init

Установите зависимости командой:
poetry install

Создайте миграции командами:
python manage.py makemigrations

python manage.py migrate

Создайте Базу Данных (в данном проекте используется PostgreSQL).

Перейдите в файл '.env.sample'. Заполните в этом файле все необходимые поля, создайте в директории проекта файл '.env' и перенесите туда заполненный в '.env.sample' шаблон.

Ниже приведен пример заполнения:

'''

    SECRET_KEY_DJANGO='your_personal_secret_key'
    PASSWORD_DB='database_password'
    NAME_DB='database_name'
    LOCATION='location_for_redis'
    CACHE_ENABLED='True'
    STRIPE_API_KEY='stripe_api_key'
    YOUR_DOMAIN="your_domain"
    TIME_ZONE='Zone/CityCenter'

'''

Завершение работы
Для остановки работы сервера используйте комбинацию клавиш Ctrl+C в окне терминала, где он был запущен.

Для остановки работы сервера Redis используйте команду: sudo service redis-server stop 

🐋 Docker: запуск
Для запуска контейнеров в фоновом режиме выполните команду:

docker-compose up -d --build
