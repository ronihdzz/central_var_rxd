# Dependencies Installation

## 🌐 Language | Idioma
**[English](../eng/installer.md)** | **[Español](../esp/installer.md)**

---

### Installing Python and Click

Install Python 3 and Click using pip:

```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip
pip3 install click
```

### Installing GPG
On Debian/Ubuntu-based systems, you can install GPG with:

```
sudo apt-get install -y gnupg
```

## Configuration

### Environment Configuration

You must define an environment variable RXD_LOCAL_ENV_PATH that points to the base directory where encrypted .env files will be stored. This variable should be defined in your profile file, for example, .bashrc or .zshrc.

1. Edit the `~/.bashrc` file:

    ```
    nano ~/.bashrc
    ```

2. Add the environment variable at the end of the file:

    ```
    export RXD_LOCAL_ENV_PATH='~/.rxd'
    ```

3. Save and close the file.

4. Apply the changes:

    ```
    source ~/.bashrc
    ```

5. To confirm that the environment variable has been configured correctly, you can execute:

    ```
    echo $RXD_LOCAL_ENV_PATH
    ```

### Script Configuration as Binary

1. Create the `~/bin/` Directory if it doesn't exist:

    ```
    mkdir -p ~/bin
    ```

2. Make sure `~/bin` is in your PATH:

    Edit ~/.bashrc or ~/.zshrc and add:

    ```
    export PATH="$HOME/bin:$PATH"
    ```

    Then apply the changes:

    ```
    source ~/.bashrc
    ```

3. Create the rxd_cli Script in `~/bin/`:

    ```
    nano ~/bin/rxd_cli
    ```

    Add the following content:

    ```
    #!/bin/bash
    python ~/.rxd/cli.py
    ```

4. Make the Script Executable:

    ```
    chmod 700 ~/bin/rxd_cli
    ```

5. Copy the cli.py script to the ~/.rxd/ directory and make it executable:

    ```
    chmod 700 ~/.rxd/cli.py
    ```

6. Installation Verification

    To verify that the CLI has been installed correctly, you can execute the following command:

    ```bash
    rxd_cli hello
    ```

    You should see a message that says:

    ```
    ######################################
    #                                    #
    #  Hello from 'Central Var RXD' CLI! #
    #                                    #
    ######################################
    ``` 