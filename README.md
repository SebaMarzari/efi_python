
# guia de uso Docker 


Se debe ejecutar los siguientes comandos

Comandos para hacer el build e inicializar la base de datos

```bash
docker compose build blog
docker compose up db
docker compose run blog bash -c "flask db init && flask db migrate"
```

Una vez completado se debe ejecutar


```bash
docker compose up -d
docker compose logs -f blog
```

# Problemas comunes

Es posible que en el inicio del docker, se inicie primero la aplicacion flask y luego la base de datos.
en ese caso se puede iniciar la app con los siguientes comandos


```bash
docker compose up -d db
docker compose up -d blog
docker compose logs -f blog
```



