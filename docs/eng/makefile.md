# Makefile Usage

## 🌐 Language | Idioma
**[English](../eng/makefile.md)** | **[Español](../esp/makefile.md)**

---

The Makefile provides a simple interface to execute CLI functions and manage environment variables.

### Environment Variables

* `PROJECT_PATH`: The path of the project from where the script is being executed.
* `ORGANIZATION`: The organization name.
* `GENERATE_FILE`: Whether to generate an exported file (values: true or false).
* `RXD_DEBUG`: Activates or deactivates debug mode (values: true or false).

### Makefile Functions

1. `run-secure`

Decrypts and processes environment files, then executes main.py.

```
make run-secure
```

2. `encrypt`

Encrypts a `.env` file.

```
make encrypt env_file=path/to/.env
```

3. `decrypt`

Decrypts a specific file.

```
make decrypt filename=filename
```

### Example Makefile Configuration

```
# Makefile

.SHELLFLAGS := -ec
.PHONY: run-secure encrypt decrypt

# Parameters for the decryption script
PROJECT_PATH := $(shell pwd)
ORGANIZATION := jalo
GENERATE_FILE := false
RXD_DEBUG := false

# Main task
all: run-secure

# Export RXD_DEBUG and execute the decryption script and then main.py
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

# Encrypt a .env file
encrypt:
	@export RXD_DEBUG=$(RXD_DEBUG); \
	rxd_cli encrypt $(env_file) --organization $(ORGANIZATION)

# Decrypt a specific file
decrypt:
	@export RXD_DEBUG=$(RXD_DEBUG); \
	rxd_cli decrypt $(PROJECT_PATH) $(filename) --organization $(ORGANIZATION)
```

### Makefile Execution

Execute Makefile commands as needed:

```
# To decrypt and process environment files, then execute main.py
make run-secure

# To encrypt a .env file
make encrypt env_file=path/to/.env

# To decrypt a specific file
make decrypt filename=filename
``` 