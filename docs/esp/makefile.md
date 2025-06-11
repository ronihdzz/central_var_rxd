
# Uso del Makefile

## 🌐 Language | Idioma
**[English](../eng/makefile.md)** | **[Español](../esp/makefile.md)**

---

El Makefile proporciona una interfaz sencilla para ejecutar las funciones del CLI y gestionar las variables de entorno.

### Variables de Entorno

* `PROJECT_PATH`: La ruta del proyecto desde donde se está ejecutando el script.
* `ORGANIZATION`: El nombre de la organización.
* `GENERATE_FILE`: Si se debe generar un archivo exportado (valores: true o false).
* `RXD_DEBUG`: Activa o desactiva el modo debug (valores: true o false).

### Funciones del Makefile

1. `run-secure`

Descifra y procesa archivos de entorno, luego ejecuta main.py.

```
make run-secure
```

2. `encrypt`

Cifra un archivo `.env`.

```
make encrypt env_file=path/to/.env
```

3. `decrypt`

Descifra un archivo específico.

```
make decrypt filename=filename
```


### Ejemplo de Configuración del Makefile

```
# Makefile

.SHELLFLAGS := -ec
.PHONY: run-secure encrypt decrypt

# Parámetros para el script de desencriptación
PROJECT_PATH := $(shell pwd)
ORGANIZATION := jalo
GENERATE_FILE := false
RXD_DEBUG := false

# Tarea principal
all: run-secure

# Exporta RXD_DEBUG y ejecuta el script de desencriptación y luego main.py
run-secure:
	@export RXD_DEBUG=$(RXD_DEBUG); \
	if [ "$(GENERATE_FILE)" = true ]; then \
	    generate_flag="--generate-file"; \
	else \
	    generate_flag=""; \
	fi; \
	exported_vars=$$(rxd_cli process $(PROJECT_PATH) $(ORGANIZATION) $$generate_flag); \
	for var in $$exported_vars; do export $$var; done; \
	bash -c "set -o allexport; python3 src/main.py"

# Encripta un archivo .env
encrypt:
	@export RXD_DEBUG=$(RXD_DEBUG); \
	rxd_cli encrypt $(env_file) --organization $(ORGANIZATION)

# Desencripta un archivo específico
decrypt:
	@export RXD_DEBUG=$(RXD_DEBUG); \
	rxd_cli decrypt $(PROJECT_PATH) $(filename) --organization $(ORGANIZATION)
```


### Ejecución del Makefile

Ejecuta los comandos del Makefile según sea necesario:

```
# Para desencriptar y procesar archivos de entorno, y luego ejecutar main.py
make run-secure

# Para encriptar un archivo .env
make encrypt env_file=path/to/.env

# Para desencriptar un archivo específico
make decrypt filename=filename
```

