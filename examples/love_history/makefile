.SHELLFLAGS := -ec
.PHONY: run-secure encrypt decrypt init hello

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
	rxd_cli encrypt $(file) --organization $(ORGANIZATION)

# Desencripta un archivo específico
decrypt:
	@export RXD_DEBUG=$(RXD_DEBUG); \
	rxd_cli decrypt $(PROJECT_PATH) $(file) --organization $(ORGANIZATION)

# Inicializa la estructura de directorios para una nueva organización
init:
	@rxd_cli init $(ORGANIZATION)

# Ejecuta el comando hello para verificar la instalación
hello:
	@rxd_cli hello