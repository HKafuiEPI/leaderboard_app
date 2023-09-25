# Utilisez une image de base Python
FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

# Commande pour exécuter l'application Flask
CMD ["python", "app.py"]
