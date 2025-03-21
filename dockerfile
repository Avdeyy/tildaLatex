FROM python:3.10

# Установка TeXLive
RUN apt update && apt install -y texlive-full

# Создание рабочей директории
WORKDIR /app

# Копирование файлов
COPY . .

# Установка зависимостей
RUN pip install -r requirements.txt

# Запуск FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
