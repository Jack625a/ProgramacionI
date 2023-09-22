# PASO 1. UtiliZAR LA IMAGEN BASE
#FROM python:3.11.5
# PASO 2. Establecer el directorio de trabajo (CONTENEDOR)
#WORKDIR /usr/src/app

#PASO 3. COPIAR LOS ARCHIVOS DEL PROYECTO AL CONTENEDOR
#COPY prueba.py .

#PASO 4. ESTABLECER UN COMANDO PARA EJECUTAR EL SCRIPT
#CMD ["python", prueba.py]

FROM python:3.11.5
RUN pip install pygame
WORKDIR /app
