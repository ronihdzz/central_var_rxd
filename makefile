.SHELLFLAGS := -ec
.PHONY: run-secure encrypt decrypt init hello

# Parámetros para el script de desencriptación
PROJECT_PATH := $(shell pwd)
ORGANIZATION := google
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
	exported_vars=$$(python3 ~/.rxd/cli.py process $(PROJECT_PATH) $(ORGANIZATION) $$generate_flag); \
	for var in $$exported_vars; do export $$var; done; \
	bash -c "set -o allexport; python3 src/main.py"

# Encripta un archivo .env
encrypt:
	@export RXD_DEBUG=$(RXD_DEBUG); \
	python3 ~/.rxd/cli.py encrypt $(file) --organization $(ORGANIZATION)

# Desencripta un archivo específico
decrypt:
	@export RXD_DEBUG=$(RXD_DEBUG); \
	python3 ~/.rxd/cli.py decrypt $(PROJECT_PATH) $(file) --organization $(ORGANIZATION)

# Inicializa la estructura de directorios para una nueva organización
init:
	@python3 ~/.rxd/cli.py init $(ORGANIZATION)

# Ejecuta el comando hello para verificar la instalación
hello:
	@python3 ~/.rxd/cli.py hello