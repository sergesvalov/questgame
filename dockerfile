FROM python:3.11-slim-bookworm
WORKDIR /app
RUN echo "Flask\ngunicorn" > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Открываем порт 5000 внутри
EXPOSE 5000

# Слушаем 0.0.0.0:5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]