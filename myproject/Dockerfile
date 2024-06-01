# Используем базовый образ Python
FROM python:3.11

# Установим рабочую директорию
# WORKDIR C:\Users\Мой Компьютер\PycharmProjects\Сайт\myproject\inTime
WORKDIR /Сайт/myproject

# Скопируем файлы требований
COPY requirements.txt .

# Установим зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируем весь код приложения
COPY . .

# Укажем команду для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# CMD ["uvicorn", "C.Users.Мой Компьютер.PycharmProjects.Сайт.myproject.asgi", "--host", "0.0.0.0", "--port", "8000"]

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SETTINGS_MODULE=myproject.settings
# EXPOSE 8000

# CMD bash -c 'uvicorn inTime.main:app --host 0.0.0.0 --port 8000 --reload'
# CMD ["python", "manage.py", "--host", "127.0.0.1", "--port", "8000"]
# CMD ["uvicorn", "myproject.asgi:", "--host", "0.0.0.0", "--port", "8000"]
# CMD uvicorn --host=0.0.0.0 --port=80 main:app

# CMD ["uvicorn", "myproject.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--log-level", "debug"]