   # Используем базовый образ Python
   FROM python:3.11

   # Установим рабочую директорию
   WORKDIR C:\Users\Мой Компьютер\PycharmProjects\Сайт\myproject\inTime

   # Скопируем файлы требований
   COPY requirements.txt .

   # Установим зависимости
   RUN pip install --no-cache-dir -r requirements.txt

   # Скопируем весь код приложения
   COPY . .

   # Укажем команду для запуска приложения
   CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
