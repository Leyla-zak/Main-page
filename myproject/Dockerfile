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
# CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
EXPOSE 8000

CMD bash -c 'uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload'