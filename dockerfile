# Используем официальный образ Python на базе Alpine как базовый
FROM python:3.11-slim-bookworm

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы приложения (app.py, data.py, и папку templates)
# Предполагается, что структура проекта выглядит так:
# .
# ├── app.py
# ├── data.py
# ├── requirements.txt
# └── templates/
COPY . .

# Приложение будет слушать порт 8080
EXPOSE 8080

# Команда запуска приложения с помощью Gunicorn
# -w 4: 4 рабочих процесса
# -b 0.0.0.0:8080: Слушаем все интерфейсы на порту 8080
# app:app: Запускаем приложение 'app' из файла 'app.py'
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]