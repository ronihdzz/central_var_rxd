# CLI Usage

## 🌐 Language | Idioma
**[English](../eng/cli.md)** | **[Español](../esp/cli.md)**

---

The cli.py script provides the following functions:

1. Encrypt a `.env` file
2. Decrypt a specific file
3. Process standard environment files
4. Verify correct CLI installation
5. Initialize a directory structure

## CLI Functions

### **1) Encrypt a .env file**
Encrypts a `.env` file and stores it in the corresponding path within `RXD_LOCAL_ENV_PATH`.

```
rxd_cli encrypt path/to/.env --organization jalo
```

* `path/to/.env`: Path to the `.env` file to encrypt.
* `--organization`: Organization name (default is default_org).

### **2) Decrypt a specific file**

Decrypts a specific file and stores it in the current working directory.

```
rxd_cli decrypt path/to/project filename --organization jalo
```

* `path/to/project`: Path to the project from where the script is being executed.
* `filename`: Name of the file to decrypt (can be development, production, staging or any specific file).
* `--organization`: Organization name (default is default_org).

### **3) Process standard environment files**

Decrypts and processes standard environment files (development, production, staging).

```
rxd_cli process /path/to/project jalo --generate-file
```

* `/path/to/project`: Path to the project from where the script is being executed.
* `jalo`: Organization name.
* `--generate-file`: If specified, generates a .env.exported file with the processed environment variables.

### **4) Installation Verification**

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

### **5) Directory Structure Initialization**

To initialize the directory structure for a new organization, you can use the following command:

```bash
rxd_cli init <organization>
```

Replace <organization> with your organization name. This will create the necessary directory structure in the path specified by the RXD_LOCAL_ENV_PATH environment variable.

For example:

```
rxd_cli init google
```

Will create the necessary directories for the google organization.

```
~/.rxd/
    ├── .google/
    │   ├── .envs
    │   |    ├── .
    │   |    ├── .
``` 