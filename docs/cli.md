
## Uso del CLI

El script cli.py proporciona las siguientes funciones:

1. Cifrar un archivo `.env`
2. Descifrar un archivo específico
3. Procesar archivos de entorno estándar
4. Verificar la correcta instalacion del CLI
5. Inicializacion de un estructura

## Funciones del CLI
### **1) Cifrar un archivo .env**
Cifra un archivo `.env` y lo almacena en la ruta correspondiente dentro de `RXD_LOCAL_ENV_PATH`.


```
rxd_cli encrypt path/to/.env --organization jalo
```

* `path/to/.env`: Ruta del archivo `.env` a cifrar.
* `--organization`: Nombre de la organización (por defecto es default_org).

### **2) Descifrar un archivo específico**

Descifra un archivo específico y lo almacena en la ruta de trabajo actual.

```
rxd_cli decrypt path/to/project filename --organization jalo
```

* `path/to/project`: Ruta del proyecto desde donde se está ejecutando el script.
* `filename`: Nombre del archivo a descifrar (puede ser development, production, staging o cualquier archivo específico).
* `--organization`: Nombre de la organización (por defecto es default_org).



### **3) Procesar archivos de entorno estándar**

Descifra y procesa los archivos de entorno estándar (development, production, staging).


```
rxd_cli process /path/to/project jalo --generate-file
```

* `/path/to/project`: Ruta del proyecto desde donde se está ejecutando el script.
* `jalo`: Nombre de la organización.
* `--generate-file`: Si se especifica, genera un archivo .env.exported con las variables de entorno procesadas.



###  **4) Verificación de la Instalación**

Para verificar que el CLI se ha instalado correctamente, puedes ejecutar el siguiente comando:

```bash
rxd_cli hello
```

Deberías ver un mensaje que dice:

```
######################################
#                                    #
#  Hello from 'Central Var RXD' CLI! #
#                                    #
######################################
```


### **5) Inicialización de la Estructura de Directorios**

Para inicializar la estructura de directorios para una nueva organización, puedes usar el siguiente comando:

```bash
rxd_cli init <organization>
```

Reemplaza <organization> con el nombre de tu organización. Esto creará la estructura de directorios necesaria en la ruta especificada por la variable de entorno RXD_LOCAL_ENV_PATH.

Por ejemplo:

```
rxd_cli init google
```

Creará los directorios necesarios para la organización google.


```
~/.rxd/
    ├── .google/
    │   ├── .envs
    │   |    ├── .
    │   |    ├── .
```