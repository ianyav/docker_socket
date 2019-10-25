FROM python:3.8-alpine
WORKDIR /code
ENV FLASK_APP receive_socket.py
ENV FLASK_RUN_HOST 192.168.88.156
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
