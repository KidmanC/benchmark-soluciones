# Utiliza la imagen base de Python 3.8 slim
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el script en el directorio de trabajo
COPY sum_primes.py .

# Crea la carpeta para el output
RUN mkdir output

# Define el comando de ejecución
CMD ["python", "sum_primes.py"]