FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

#Flask espera essa variavel
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

#O 'command' no docker-compose vai rodar 'python app.py'
#Mas para desenvolvimento, 'flask run' é melhor
CMD ["flask", "run"]

