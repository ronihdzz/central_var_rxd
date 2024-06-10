# Central Var RXD


# Environment Variables Management CLI

## Descripción

Este proyecto proporciona una interfaz de línea de comandos (CLI) para gestionar archivos `.env` mediante cifrado y descifrado utilizando GPG. El CLI permite cifrar archivos `.env`, descifrar archivos específicos y procesar variables de entorno para diferentes entornos (desarrollo, producción, staging).

## Requisitos Previos

1. **Python 3.6+**: Asegúrate de tener Python 3.6 o una versión posterior instalada.
2. **GPG**: Instala GPG en tu sistema.
3. **Click**: Instala la biblioteca Click para crear el CLI.

## Instalación de Dependencias

### Instalación de Python y Click

Instala Python 3 y Click utilizando pip:

```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip
pip3 install click
```

## Menú

- [Instalación y Configuración](docs/installer.md)
- [Uso del CLI](docs/cli.md)
- [Uso del Makefile](docs/makefile.md)


### [Instalación y Configuración](docs/installer.md)

Incluye instrucciones detalladas sobre cómo configurar el entorno, definir variables de entorno y configurar el script como binario.

### [Uso del CLI](docs/cli.md)

Proporciona detalles sobre cómo utilizar las funciones del CLI para cifrar, descifrar y procesar archivos `.env`.

### [Uso del Makefile](docs/makefile.md)

Explica cómo utilizar el Makefile para ejecutar las funciones del CLI y gestionar las variables de entorno de manera eficiente.



Funcione al CLI de Hello from 'Central Var RXD'