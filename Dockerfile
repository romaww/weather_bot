FROM debian:bullseye

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

WORKDIR /app

COPY . .

# RUN pip3 install --no-cache-dir -U aiogram==3.0.0b7
RUN pip3 install --no-cache-dir aiogram
RUN pip install --no-cache-dir python-dotenv
RUN pip install --no-cache-dir requests

CMD ["python3", "bot.py"]
