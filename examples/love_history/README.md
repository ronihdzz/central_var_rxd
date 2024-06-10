# Love history


## 1. `make init`

Creara una la organizacion con el nombre `google` en la ruta `RXD_LOCAL_ENV_PATH`

Comando:

```
make init
```

Esto es lo que hara graficamente:

```
~/.rxd/
    ├── .google/
    │   ├── .envs
    │   |    ├── .
    │   |    ├── .
```


## 2. `make encrypt file=.env.dev`

Encriptara el archivo cuyo nombre es: `.env.dev` y te pedira una frase de encriptacion, despues guardara dicho archivo encriptado en la ruta `RXD_LOCAL_ENV_PATH/ORGANIZATION`

Comando:

```
make encrypt file=.env.dev
```

Especificamente aqui lo guardara con el sufijo `.gpg`

```
~/.rxd/
    ├── .google/
    │   ├── .envs
    │   |    ├── .env.dev.gpg
    │   |    ├── .
```


## 3. `make decrypt file=development`

Desencriptara el archivo de varaibles de entorno cuyo nombre  pertenece al entorno `development`
dicho archivo desencriptado lo guardara en la ruta de tu proyecto dentro de la carpeta `.envs`


```
make decrypt file=development
```

Especificamente aqui lo descargara:

```
love_history/
├── .env.dev
├── .env.prd
├── .env.stg
├── .envs
│   ├── .env.exported_development   =======> aqui se encuentra el archivo desencriptado
│   └── .env.template
├── makefile
└── src
└── main.py
```


## 4. `make run-secure`

Comando: 

```
make run-secure
```

Funciona de la siguiente manera:

1. Leera el archivo de tu proyecto `.envs/template`

2. De el obtendra el entorno del cual quieres exportar las variables de entorno, para este ejemplo
en especifico como el archivo contiene lo siguiente:

    ```
    ENVIRONMENT=production
    AMOR_DICIEMBRE=
    AMOR_AGOSTO=
    ```
    cargara las variables de entorno del entorno `production`

3. Despues solo exportara las variables solo las variables de entorno que estan contenidas en tu archivo `.envs/template` 
es decir solo exportara del archivo `production` las variables:

    * ENVIRONMENT
    * AMOR_DICIEMBRE
    * AMOR_AGOSTO

4. Te pedira la clave de encriptacion del entorno de `production`

5. Si ejecutas correctamente la clave, procedera a exportarte las variables de entorno mencionadas en el paso 1, y despues
se ejecutara el proyecto con esas variables de entorno


## 5. `make hello`

Servira para corraborar que el CLI funciona**

```
make hello
```

Al ejecutar lo anterior te deberia aparecer lo siguiente:

```
2024-06-09 23:56:26,402 - INFO - Debug mode: False
######################################
#                                    #
#  Hello from 'Central Var RXD' CLI! #
#                                    #
######################################
```



