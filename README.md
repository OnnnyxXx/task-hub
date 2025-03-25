Task-Hub: Платформа для Публикации и Решения Задач
---

## Описание

**Task-Hub** - это платформа, предназначенная для публикации и решения задач. Пользователи могут создавать задачи в
различных категориях, а другие пользователи могут предлагать свои решения.

---

## Возможности

- **Аутентификация**: Регистрация и вход для управления задачами.
- **Категоризация**: Задачи разделены для удобного поиска.
- **Публикация**: Авторизованные пользователи могут создавать задачи с описанием и категорией.
- **Решения**: Пользователи предлагают решения для задач.
- **Оценка**: Автор задачи оценивает профиль пользователя, предложившего решение.

---

## Технологии

- **Python**: 3.11
- **Django**: 4.2.7
- **PostgreSQL**: Хранение данных
- **Docker & Docker Compose**: Упрощение развертывания
- **Redis**: Кэширование и обмен сообщениями

---

## Как начать

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/OnnnyxXx/task-hub.git
2. Перейдите в директорию проекта:
   ```bash
   cd task-hub

## Через Docker Compose

1. Запустите Docker Compose
   ```bash
    docker-compose up --build

2. Создать миграции и суперпользователя
   ```bash
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser

---

## Классический метод (без Docker)

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt

2. Создайте миграции и суперпользователя:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser

3. Запустите сервер разработки:
   ```bash
   python manage.py runserver
