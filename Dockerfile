FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir aiogram
RUN pip install --no-cache-dir python-dotenv
RUN pip install --no-cache-dir requests

CMD ["python3", "bot.py"]
