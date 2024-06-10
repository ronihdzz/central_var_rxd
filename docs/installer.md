
## Instalación de Dependencias

### Instalación de Python y Click

Instala Python 3 y Click utilizando pip:

```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip
pip3 install click
```

### Instalación de GPG
En sistemas basados en Debian/Ubuntu, puedes instalar GPG con:

```
sudo apt-get install -y gnupg
```

## Configuración

### Configuración del Entorno

Debes definir una variable de entorno RXD_LOCAL_ENV_PATH que apunte al directorio base donde se almacenarán los archivos .env cifrados. Esta variable se debe definir en tu archivo de perfil, por ejemplo, .bashrc o .zshrc.

1. Editar el archivo `~/.bashrc`:

    ```
    nano ~/.bashrc
    ```

2. Agregar la variable de entorno al final del archivo:

    ```
    export RXD_LOCAL_ENV_PATH='~/.rxd'
    ```


3. Guardar y cerrar el archivo.


4. Aplicar los cambios:

    ```
    source ~/.bashrc
    ```


5. Para confirmar que la variable de entorno se ha configurado correctamente, puedes ejecutar:

    ```
    echo $RXD_LOCAL_ENV_PATH
    ```


### Configuración del Script como Binario

1. Crea el Directorio `~/bin/` si no Existe:

    ```
    mkdir -p ~/bin
    ```

2. Asegúrate de que `~/bin` esté en tu PATH:

    Edita ~/.bashrc o ~/.zshrc y añade:

    ```
    export PATH="$HOME/bin:$PATH"
    ```

    Luego aplica los cambios:

    ```
    source ~/.bashrc
    ```

3. Crea el Script rxd_cli en `~/bin/`:

    ```
    nano ~/bin/rxd_cli
    ```

    Añade el siguiente contenido:

    ```
    #!/bin/bash
    python ~/.rxd/cli.py
    ```


4. Haz el Script Ejecutable:

    ```
    chmod 700 ~/bin/rxd_cli
    ```


5. Copia el script cli.py al directorio ~/.rxd/ y hazlo ejecutable:

    ```
    chmod 700 ~/.rxd/cli.py
    ```


6.  Verificación de la Instalación

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