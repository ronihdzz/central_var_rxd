# Central Var RXD

## 🌐 Language | Idioma
**[English](README.md)** | **[Español](README.es.md)**

---

**Secure Environment Variables Management System with GPG Encryption**

---

## 📋 Table of Contents

1. [What is Central Var RXD?](#-what-is-central-var-rxd)
2. [What Problems Does It Solve?](#-what-problems-does-it-solve)
3. [Key Features](#-key-features)
4. [Quick Installation](#-quick-installation)
5. [Basic Usage Guide](#-basic-usage-guide)
6. [System Structure](#️-system-structure)
7. [Technical Components](#-technical-components)
8. [Complete Example: Johnny's Story](#-complete-example-johnnys-story)
9. [Integration in Your Project](#-integration-in-your-project)
10. [Complete Technical Documentation](#-complete-technical-documentation)

---

## 🎯 What is Central Var RXD?

Central Var RXD is a CLI (Command Line Interface) tool designed to manage environment variables in a **secure and centralized** way in software development projects. It uses GPG (GNU Privacy Guard) encryption to protect sensitive information such as passwords, API keys, tokens, and other credentials that should not be exposed in plain text.

---

## 💡 What Problems Does It Solve?

### 1. **Credential Security**
- **Problem**: Environment variables contain sensitive information (passwords, API keys, tokens) that cannot be shared in plain text.
- **Solution**: Automatically encrypts all `.env` files using GPG with AES256 algorithm.

### 2. **Multi-Environment Management**
- **Problem**: Modern projects handle multiple environments (development, staging, production) with different configurations.
- **Solution**: Automatically manages separate files for each environment (`.env.dev.gpg`, `.env.stg.gpg`, `.env.prd.gpg`).

---

## ⭐ Key Features

- 🔐 **AES256 Encryption**: Maximum security with GPG
- 🚀 **Direct Execution**: Variables only in memory, never on disk
- 🎯 **Multi-Environment**: Development, staging, and production
- 👥 **Secure Collaboration**: Share projects without exposing credentials
- 🛡️ **Zero Temporary Files**: No local traces
- 🔑 **Authentication Required**: Passphrase for each operation

---

## ⚡ Quick Installation

```bash
# 1. Check dependencies
python3 --version  # Python 3.6+
gpg --version      # GPG 2.0+

# 2. Install Central Var RXD
# (See complete documentation in docs/eng/installer.md)

# 3. Verify installation
rxd_cli hello
```

> **📖 Complete Installation**: [docs/eng/installer.md](docs/eng/installer.md)

---

## 🚀 Basic Usage Guide

### Step 1: Configure Project
```bash
# Copy makefile to your project
cp ~/.rxd/makefile your-project/
cd your-project/

# Configure organization
sed -i 's/ORGANIZATION := jalo/ORGANIZATION := your-org/' makefile
```

### Step 2: Create Template
```bash
mkdir -p .envs/
cat > .envs/.env.template << EOF
ENVIRONMENT=development
DATABASE_URL=
API_KEY=
SECRET_TOKEN=
EOF
```

### Step 3: Encrypt Variables
```bash
# Create variables file
echo "DATABASE_URL=postgresql://localhost/myapp" > .env.dev
echo "API_KEY=dev-key-123" >> .env.dev

# Encrypt file
make encrypt file=.env.dev

# Remove original
rm .env.dev
```

### Step 4: Run Securely
```bash
make run-secure
```

---

## 🏗️ System Structure

### **Central Directory**
```
~/.rxd/                                 # Base directory of the system
├── cli.py                             # 🔧 SOURCE CODE of the CLI
└── [ORGANIZACIONES]/                  # Folders by organization/project
    ├── jalo/                          # Example: organization "jalo"
    │   └── .envs/
    │       ├── .env.dev.gpg          # Development variables (ENCRYPTED)
    │       ├── .env.stg.gpg          # Staging variables (ENCRYPTED)
    │       └── .env.prd.gpg          # Production variables (ENCRYPTED)
    ├── mi-empresa/                    # Example: organization "mi-empresa"
    │   └── .envs/
    │       ├── .env.dev.gpg
    │       ├── .env.stg.gpg
    │       └── .env.prd.gpg
    └── otro-proyecto/
        └── .envs/
            ├── .env.dev.gpg
            ├── .env.stg.gpg
            └── .env.prd.gpg
```

### **Project Structure**
```
Tu-Proyecto/                           # Any of your projects
├── makefile                          # 📋 COPY - Only change ORGANIZATION
├── src/
│   └── main.py                       # Your application that uses variables
└── .envs/
    └── .env.template                 # 🎯 CONFIGURATION - Define what you need
```

---

## 🔧 Technical Components

### **1. Main CLI (`~/.rxd/cli.py`)**
- **Location**: `~/.rxd/cli.py`
- **Function**: Source code of the CLI that handles encryption/decryption
- **Installed once** and serves for all projects

### **2. Makefile (Copied to each project)**
- **Copied**: To the root of each project
- **Configuration**: Only change `ORGANIZATION := tu-proyecto`
- **Function**: Simplifies execution with commands like `make run-secure`

### **3. Variable Template (`proyecto/.envs/.env.template`)**
- **Location**: In each individual project
- **Function**: Define what variables that project specifically needs
- **Controls**: Default environment and variables to inject

    The `.env.template` is the **configuration file** that tells the CLI:
    1. **What default environment to use?**
    2. **What variables to inject in your code?**

    #### **.env.template Structure:**
    ```bash
    # .envs/.env.template
    ENVIRONMENT=          # ← Cannot be empty
    ```

    #### **Available Values for ENVIRONMENT:**
    - **`development`** → Use `.env.dev.gpg`
    - **`staging`** → Use `.env.stg.gpg`  
    - **`production`** → Use `.env.prd.gpg`

    #### **⚠️ FILE NAMING (CRITICAL)**
    
    **Original Files (before encryption):**
    ```bash
    .env.dev     # ← File for DEVELOPMENT
    .env.prd     # ← File for PRODUCTION  
    .env.stg     # ← File for STAGING
    ```
    
    **Encrypted Files (after encryption):**
    ```bash
    .env.dev.gpg # ← Generated automatically
    .env.prd.gpg # ← Generated automatically
    .env.stg.gpg # ← Generated automatically
    ```
    
    **What if I use other names?**
    ❌ **WILL NOT WORK** - The system looks for exactly these names.

### **Complete Workflow**

1. **Single Installation**: Install the CLI in `~/.rxd/cli.py` (once)
2. **By Project**: Copy `makefile` and create `.env.template`
3. **Encryption**: Variables are encrypted in `~/.rxd/[ORGANIZATION]/.envs/`
4. **Execution**: `make run-secure` decrypts, injects, and executes
5. **Cleanup**: Temporary files are automatically removed

---

## 👨‍💻 Complete Example: Johnny's Story

### **Situation:**
Johnny has a project called **"love_history"** with the structure:
```
love_history/
└── src/
    └── main.py        # Uses AMOR_AGOSTO and AMOR_DICIEMBRE variables
```

His `main.py` contains code that uses sensitive variables:
```python
import os
amor_agosto = os.environ.get("AMOR_AGOSTO")
amor_diciembre = os.environ.get("AMOR_DICIEMBRE")
print(f"In August: {amor_agosto}")
print(f"In December: {amor_diciembre}")
```

### **Johnny's Problem:**
- Has sensitive variables (person names 😅)
- Doesn't want those names to be in plain text on his computer
  because it's very confidential information

### **Solution: Use Central Var RXD**

#### **Step 1: Install the System**
```bash
# Johnny installs the CLI once
# (following docs/eng/installer.md)
rxd_cli hello  # ✅ Verify installation
```

#### **Step 2: Copy and Configure Makefile**
```bash
cd love_history/
# Copy the system's makefile
cp ~/.rxd/makefile .

# Edit ONLY the organization
nano makefile
# Change: ORGANIZATION := jalo
# To:    ORGANIZATION := love_history
```

#### **Step 3: Create the .envs Folder**
```bash
mkdir -p .envs/
```

#### **Step 4: Encrypt Your Environment Variables File**

```bash
# Create file with actual values
cat > .env.prd << EOF
AMOR_AGOSTO=Fran
AMOR_DICIEMBRE=Diego
EOF

# Encrypt the file (here's the magic!)
make encrypt file=.env.prd
# This creates: ~/.rxd/love_history/.envs/.env.prd.gpg

# Remove the original file (for security) 
# ¡So no one fisguees on his computer his love life! 💕
rm .env.prd
```

#### **Step 5: Create the Magic Template (.env.template)**

¡Now comes the important part! Johnny needs to create the file that tells the system:
- **What environment to use?** (development, staging, production)
- **What variables to inject?** (only the ones he really needs)

```bash
cat > .envs/.env.template << EOF
ENVIRONMENT=production
AMOR_AGOSTO=
AMOR_DICIEMBRE=
EOF
```

**What does each line do?**
- `ENVIRONMENT=production` → "Hey system, by default use my `.env.prd.gpg`"
- `AMOR_AGOSTO=` → "I need this variable in my code" (value comes from encrypted file)
- `AMOR_DICIEMBRE=` → "I also need this other variable"

💡 **Johnny's Tip**: The template is like a "shopping list" - only ask for what you really need.

#### **Step 6: ¡The Moment of Truth! 🎭**

Now Johnny can run his project without anyone seeing his love secrets:

```bash
# ¡One command and done!
make run-secure
```

### **🎬 What happens internally when Johnny runs `make run-secure`?**

**¡It's like a spy movie! 🕵️‍♂️**

1. **📋 Reading the Template**: 
   - System: "Let's see... read `.envs/.env.template`"
   - System: "Ah! Johnny wants `ENVIRONMENT=production`, `AMOR_AGOSTO` and `AMOR_DICIEMBRE`"

2. **🔍 Searching for the Treasure**:
   - System: "Since Johnny said production, I look for `~/.rxd/love_history/.envs/.env.prd.gpg`"
   - System: "Found! 💎"

3. **🔓 Secure Decryption** (¡GPG asks for the passphrase!):
   - System: "GPG, decrypt this please..."
   - GPG: "What's your passphrase, Johnny?" 🔑
   - Johnny: *enters his passphrase*
   - GPG: "Done boss, here are your variables"

4. **💉 Direct Injection** (¡No temporary files!):
   - System: "Capturing variables: `AMOR_AGOSTO=Fran AMOR_DICIEMBRE=Diego`"
   - System: "Injecting directly into the execution environment..."
   - System: "Done! Variables are in memory, not in files"

5. **🚀 Project Execution**:
   - System: "Run! `python3 src/main.py`"
   - Johnny's code: "Great! I have my secret variables"

6. **🧹 Automatic Cleanup** (¡No traces!):
   - System: "Process finished, freeing memory..."
   - System: "Variables removed from environment!"

**🔒 Super Cool**: Variables NEVER go to local files! They only exist in memory during execution. 🛡️

### **🔧 How does the `make run-secure` work technically?**

```bash
# 1. Capture variables directly from CLI
exported_vars=$$(rxd_cli process $(PROJECT_PATH) $(ORGANIZATION))

# 2. Inject them into the current environment (¡no files!)
for var in $$exported_vars; do export $$var; done

# 3. Execute the program with those variables already available
bash -c "set -o allexport; python3 src/main.py"
```

**🛡️ Super James Bond Security:**
- ✅ GPG asks for passphrase to decrypt
- ✅ Variables only in memory, never on disk
- ✅ Automatically removed after process ends
- ✅ Zero temporary files in your project

### **Final Result for Johnny:**
```
love_history/                     # Johnny's project
├── makefile                      # ORGANIZATION := love_history
├── src/
│   └── main.py                   # Uses variables
└── .envs/
    └── .env.template             # Defines what variables it needs

~/.rxd/                           # Central system
├── cli.py                        # CLI code
└── love_history/                 # Johnny's organization
    └── .envs/
        └── .env.prd.gpg         # Securely encrypted variables
```

### **🏆 Johnny's Advantages (and his love life):**

- 🔐 **Extreme Security**: AES256 encryption + passphrase + variables only in memory. Even the NSA wouldn't know about Fran and Diego!
- 🚀 **Super Simplicity**: One single `make run-secure`, enter your passphrase and ¡done!
- 👥 **No Shame Collaboration**: Can upload project to GitHub without coworkers seeing his crushes
- 🎭 **Multi-Environment**: Can create `.env.dev.gpg` for "test loves" 😉  
- 🎯 **Total Control**: Only variables from template are injected - no "surprise" variables
- 💾 **Zero Local Files**: Variables NEVER touch Johnny's computer disk
- 🔑 **Authentication Required**: GPG always asks for his personal passphrase

**💖 Johnny can sleep peacefully knowing his secrets are safe** 😴

---

## 🚀 Integration in Your Project

### Step 1: Copy the Makefile
```bash
# Copy the makefile to your project
cp makefile tu-nuevo-proyecto/
cd tu-nuevo-proyecto/

# Edit the organization
sed -i 's/ORGANIZATION := jalo/ORGANIZATION := tu-organizacion/' makefile
```

### Step 2: Create Variable Template
```bash
# Create the structure
mkdir -p .envs/

# Define your required variables
cat > .envs/.env.template << EOF
ENVIRONMENT=development
DATABASE_URL=
API_KEY=
SECRET_TOKEN=
EOF
```

### Step 3: Encrypt Variables by Environment

> **⚠️ IMPORTANT**: Files MUST have specific names to work:
> - **`.env.dev`** → For development (generates `.env.dev.gpg`)
> - **`.env.prd`** → For production (generates `.env.prd.gpg`) 
> - **`.env.stg`** → For staging (generates `.env.stg.gpg`)

```bash
# Create .env files for each environment (EXACT NAMES)
echo "DATABASE_URL=postgresql://localhost/myapp_dev" > .env.dev
echo "API_KEY=dev-api-key-123" >> .env.dev
echo "SECRET_TOKEN=dev-secret-123" >> .env.dev

echo "DATABASE_URL=postgresql://prod-server/myapp" > .env.prd
echo "API_KEY=prod-api-key-xyz" >> .env.prd
echo "SECRET_TOKEN=prod-secret-xyz" >> .env.prd

# Encrypt for each environment
make encrypt file=.env.dev   # → Generates ~/.rxd/tu-org/.envs/.env.dev.gpg
make encrypt file=.env.prd   # → Generates ~/.rxd/tu-org/.envs/.env.prd.gpg

# Remove original files for security
rm .env.dev .env.prd
```

### Step 4: Use in Your Application
```bash
# Run with automatically injected variables
make run-secure

# Or for specific environment
ENVIRONMENT=production make run-secure
```

**¡Your project is integrated!** 🎉

---

## 📖 Complete Technical Documentation

### **Mandatory Reading**

Correct implementation of Central Var RXD requires complete reading of specific documentation. Each document contains critical technical information for system operation.

### **1. [Installation and Configuration](docs/eng/installer.md)** - **CRITICAL**

**Critical Importance:**
- Incorrect dependency installation prevents system operation
- `RXD_LOCAL_ENV_PATH` configuration is crucial for file localization
- `PATH` configuration is necessary for `rxd_cli` execution

**Document Content:**
- Dependency installation: Python3, Click, GPG
- Environment variable configuration: `RXD_LOCAL_ENV_PATH`
- Binary configuration for terminal execution
- Installation verification procedures

### **2. [CLI Usage](docs/eng/cli.md)** - **CRITICAL**

**Critical Importance:**
- Unfamiliar CLI commands prevent system use
- Incorrect syntax of parameters generates execution errors
- Understanding CLI command structure is essential for correct encryption

**Document Content:**
- 5 fundamental commands: `encrypt`, `decrypt`, `process`, `hello`, `init`
- Specific syntax: mandatory and optional parameters
- Example implementations for each command
- Critical parameters: `--organization`, paths, file names

### **3. [Makefile Usage](docs/eng/makefile.md)** - **CRITICAL**

**Critical Importance:**
- Understanding Makefile variables is necessary for customization
- Command knowledge is essential for project execution
- Correct configuration prevents organization errors

**Document Content:**
- 4 critical variables: `PROJECT_PATH`, `ORGANIZATION`, `GENERATE_FILE`, `RXD_DEBUG`
- 3 main commands: `run-secure`, `encrypt`, `decrypt`
- Complete configuration with functional examples
- Specific syntax for each command

### **Recommended Study Methodology**

1. Read each document completely, line by line
2. Execute all example commands provided
3. Verify each step's functionality before continuing
4. Document important parameters for reference
5. Test commands in a secure development environment

### **Success Guarantee**
Complete reading and understanding these three documents guarantees 99% success in Central Var RXD implementation. Omission of this documentation results in equivalent probability of technical issues.

### **Consequences of Omitting Documentation**

**By omitting [Installation and Configuration](docs/eng/installer.md):**
- "Command not found" errors
- "Environment variable not defined" errors
- Unable to localize encrypted files
- Significant time spent resolving issues

**By omitting [CLI Usage](docs/eng/cli.md):**
- Encrypting files in incorrect locations
- Unable to decrypt own files
- Incorrect organization use
- Execution errors with confusing messages

**By omitting [Makefile Usage](docs/eng/makefile.md):**
- Incorrect organization configuration
- `make` command failures
- Unable to execute projects securely
- Incorrect debug variable configuration

---

**Central Var RXD** - *Secure and efficient environment variable management for development teams*