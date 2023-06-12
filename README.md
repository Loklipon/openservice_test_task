# Тестовое задание в компанию OpenService

### _Стек технологий_
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

### _Описание задания_
Интернет-магазин имеет приложение, БД которого находится в отдельном
приложении и общается с ним через API.

Написать сервис для хранения товаров. Сделать CRUD API для всех моделей. В админ-панели вывести в удобном виде информацию о записях в таблицах.

Товар:
• Название
• Цена
• Количество
• Штрихкод
• Дата обновления
• Тип
Тип:
• Название
• Описание
Цена:
• Валюта
• Стоимость

Опционально:
• Добавить поиск в товары в админ-панель
• Реализовать в API метод для уменьшения остатка товара на складе

### _Как запустить проект_ 
* Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Loklipon/openservice_test_task/
```
```
cd openservice_test_task/backend
```
* Собрать образ из Dockerfile
```
 docker build -t image_name .
```
* Запустить контейнер из образа
```
docker run --name my_project -it -p 8000:8000 image_name
```
* Проект будет доступен по адресу 127.0.0.1:8000
* Учетные данные:
```
логин: admin
пароль: password
```
