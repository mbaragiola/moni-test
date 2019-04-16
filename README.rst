baragiola-moni
==============
# Instrucciones

## Docker

Es necesario tener instalado `docker` y `docker-compose`, por compatibilidad con Windows/macOS/Linux.

## Construir imagen sin correr

    ```
    $ docker-compose build
    ```

## Correr imagen

    ```
    $ docker-compose up
    ```

## Acceder a la GUI

Si instalaron `docker` desde `brew` o similar: http://192.168.99.100:8000

Si instalaron Docker for Mac o Docker for Windows: http://localhost:8000

Si instalaron `docker` desde APT/YUM: http://localhost:8000 


## Validación de préstamo

La validación de préstamo es realizada en baragiola_moni/prestamos/signals.py cada vez que se crea un Pedido antes de guardarse.
