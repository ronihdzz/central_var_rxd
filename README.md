# Central Var RXD

**Sistema de Gestión Segura de Variables de Entorno con Cifrado GPG**

---

## 📋 Tabla de Contenidos

1. [¿Qué es Central Var RXD?](#-qué-es-central-var-rxd)
2. [¿Qué Problemas Resuelve?](#-qué-problemas-resuelve)
3. [Características Principales](#-características-principales)
4. [Instalación Rápida](#-instalación-rápida)
5. [Guía de Uso Básico](#-guía-de-uso-básico)
6. [Estructura del Sistema](#️-estructura-del-sistema)
7. [Componentes Técnicos](#-componentes-técnicos)
8. [Ejemplo Completo: La Historia de Juanito](#-ejemplo-completo-la-historia-de-juanito)
9. [Integración en Tu Proyecto](#-integración-en-tu-proyecto)
10. [Documentación Técnica Completa](#-documentación-técnica-completa)

---

## 🎯 ¿Qué es Central Var RXD?

Central Var RXD es una herramienta CLI (Command Line Interface) diseñada para gestionar variables de entorno de manera **segura y centralizada** en proyectos de desarrollo de software. Utiliza cifrado GPG (GNU Privacy Guard) para proteger información sensible como contraseñas, API keys, tokens y otras credenciales que no deben estar expuestas en texto plano.

---

## 💡 ¿Qué Problemas Resuelve?

### 1. **Seguridad de Credenciales**
- **Problema**: Las variables de entorno contienen información sensible (passwords, API keys, tokens) que no pueden ser compartidas en texto plano.
- **Solución**: Cifra automáticamente todos los archivos `.env` usando GPG con algoritmo AES256.

### 2. **Gestión Multi-Ambiente**
- **Problema**: Los proyectos modernos manejan múltiples ambientes (desarrollo, staging, producción) con diferentes configuraciones.
- **Solución**: Maneja automáticamente archivos separados para cada ambiente (`.env.dev.gpg`, `.env.stg.gpg`, `.env.prd.gpg`).

---

## ⭐ Características Principales

- 🔐 **Cifrado AES256**: Máxima seguridad con GPG
- 🚀 **Ejecución Directa**: Variables solo en memoria, nunca en disco
- 🎯 **Multi-Ambiente**: Desarrollo, staging y producción
- 👥 **Colaboración Segura**: Comparte proyectos sin exponer credenciales
- 🛡️ **Zero Archivos Temporales**: Sin rastros locales
- 🔑 **Autenticación Requerida**: Frase secreta para cada operación

---

## ⚡ Instalación Rápida

```bash
# 1. Verificar dependencias
python3 --version  # Python 3.6+
gpg --version      # GPG 2.0+

# 2. Instalar Central Var RXD
# (Ver documentación completa en docs/installer.md)

# 3. Verificar instalación
rxd_cli hello
```

> **📖 Instalación Completa**: [docs/installer.md](docs/installer.md)

---

## 🚀 Guía de Uso Básico

### Paso 1: Configurar Proyecto
```bash
# Copiar makefile a tu proyecto
cp ~/.rxd/makefile tu-proyecto/
cd tu-proyecto/

# Configurar organización
sed -i 's/ORGANIZATION := jalo/ORGANIZATION := tu-org/' makefile
```

### Paso 2: Crear Template
```bash
mkdir -p .envs/
cat > .envs/.env.template << EOF
ENVIRONMENT=development
DATABASE_URL=
API_KEY=
SECRET_TOKEN=
EOF
```

### Paso 3: Cifrar Variables
```bash
# Crear archivo de variables
echo "DATABASE_URL=postgresql://localhost/myapp" > .env.dev
echo "API_KEY=dev-key-123" >> .env.dev

# Cifrar archivo
make encrypt file=.env.dev

# Eliminar original
rm .env.dev
```

### Paso 4: Ejecutar con Seguridad
```bash
make run-secure
```

---

## 🏗️ Estructura del Sistema

### **Directorio Central**
```
~/.rxd/                                 # Directorio base del sistema
├── cli.py                             # 🔧 CÓDIGO FUENTE del CLI
└── [ORGANIZACIONES]/                  # Carpetas por organización/proyecto
    ├── jalo/                          # Ejemplo: organización "jalo"
    │   └── .envs/
    │       ├── .env.dev.gpg          # Variables desarrollo (CIFRADAS)
    │       ├── .env.stg.gpg          # Variables staging (CIFRADAS)
    │       └── .env.prd.gpg          # Variables producción (CIFRADAS)
    ├── mi-empresa/                    # Ejemplo: organización "mi-empresa"
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

### **Estructura del Proyecto**
```
Tu-Proyecto/                           # Cualquier proyecto tuyo
├── makefile                          # 📋 SE COPIA - Solo cambiar ORGANIZATION
├── src/
│   └── main.py                       # Tu aplicación que usa variables
└── .envs/
    └── .env.template                 # 🎯 CONFIGURACIÓN - Define qué necesitas
```

---

## 🔧 Componentes Técnicos

### **1. CLI Principal (`~/.rxd/cli.py`)**
- **Ubicación**: `~/.rxd/cli.py`
- **Función**: Código fuente del CLI que maneja cifrado/descifrado
- **Se instala una vez** y sirve para todos los proyectos

### **2. Makefile (Se copia a cada proyecto)**
- **Se copia**: A la raíz de cada proyecto
- **Configuración**: Solo cambiar `ORGANIZATION := tu-proyecto`
- **Función**: Simplifica la ejecución con comandos como `make run-secure`

### **3. Template de Variables (`proyecto/.envs/.env.template`)**
- **Ubicación**: En cada proyecto individual
- **Función**: Define qué variables necesita ese proyecto específico
- **Controla**: Ambiente por defecto y variables a inyectar

    El `.env.template` es el **archivo de configuración** que le dice al CLI:
    1. **¿Qué ambiente usar por defecto?**
    2. **¿Qué variables inyectar en tu código?**

    #### **Estructura del .env.template:**
    ```bash
    # .envs/.env.template
    ENVIRONMENT=          # ← No puede estar vacio
    ```

    #### **Valores Disponibles para ENVIRONMENT:**
    - **`development`** → Usa archivo `.env.dev.gpg`
    - **`staging`** → Usa archivo `.env.stg.gpg`  
    - **`production`** → Usa archivo `.env.prd.gpg`

    #### **⚠️ NOMENCLATURA DE ARCHIVOS (CRÍTICO)**
    
    **Archivos Originales (antes de cifrar):**
    ```bash
    .env.dev     # ← Archivo para DESARROLLO
    .env.prd     # ← Archivo para PRODUCCIÓN  
    .env.stg     # ← Archivo para STAGING
    ```
    
    **Archivos Cifrados (después de cifrar):**
    ```bash
    .env.dev.gpg # ← Se genera automáticamente
    .env.prd.gpg # ← Se genera automáticamente
    .env.stg.gpg # ← Se genera automáticamente
    ```
    
    **¿Qué pasa si uso otros nombres?**
    ❌ **NO FUNCIONARÁ** - El sistema busca exactamente estos nombres.

### **Flujo de Trabajo Completo**

1. **Instalación Única**: Se instala el CLI en `~/.rxd/cli.py` (una sola vez)
2. **Por Proyecto**: Se copia `makefile` y se crea `.env.template`
3. **Cifrado**: Variables se cifran en `~/.rxd/[ORGANIZATION]/.envs/`
4. **Ejecución**: `make run-secure` descifra, inyecta y ejecuta
5. **Limpieza**: Archivos temporales se eliminan automáticamente

---

## 👨‍💻 Ejemplo Completo: La Historia de Juanito

### **Situación:**
Juanito tiene un proyecto llamado **"love_history"** con la estructura:
```
love_history/
└── src/
    └── main.py        # Usa variables AMOR_AGOSTO y AMOR_DICIEMBRE
```

Su `main.py` contiene código que usa variables sensibles:
```python
import os
amor_agosto = os.environ.get("AMOR_AGOSTO")
amor_diciembre = os.environ.get("AMOR_DICIEMBRE")
print(f"En agosto: {amor_agosto}")
print(f"En diciembre: {amor_diciembre}")
```

### **Problema de Juanito:**
- Tiene variables sensibles (nombres de personas 😅)
- No quiere que esos nombres estén en texto plano en su computadora
  porque es información muy confidencial

### **Solución: Usar Central Var RXD**

#### **Paso 1: Instalar el Sistema**
```bash
# Juanito instala el CLI una sola vez
# (siguiendo docs/installer.md)
rxd_cli hello  # ✅ Verificar instalación
```

#### **Paso 2: Copiar y Configurar Makefile**
```bash
cd love_history/
# Copia el makefile del sistema
cp ~/.rxd/makefile .

# Edita SOLO la organización
nano makefile
# Cambia: ORGANIZATION := jalo
# Por:    ORGANIZATION := love_history
```

#### **Paso 3: Crear la carpeta .envs**
```bash
mkdir -p .envs/
```

#### **Paso 4: Cifrar su archivo de variables de entorno**

```bash
# Crea archivo con valores reales
cat > .env.prd << EOF
AMOR_AGOSTO=Fran
AMOR_DICIEMBRE=Diego
EOF

# Cifra el archivo (¡aquí está la magia!)
make encrypt file=.env.prd
# Esto crea: ~/.rxd/love_history/.envs/.env.prd.gpg

# Elimina el archivo original (por seguridad) 
# ¡Para que nadie fisguee en su computadora los amores de su vida! 💕
rm .env.prd
```

#### **Paso 5: Crear el Template Mágico (.env.template)**

¡Ahora viene la parte importante! Juanito necesita crear el archivo que le dirá al sistema:
- **¿Qué ambiente usar?** (development, staging, production)
- **¿Qué variables inyectar?** (solo las que realmente necesita)

```bash
cat > .envs/.env.template << EOF
ENVIRONMENT=production
AMOR_AGOSTO=
AMOR_DICIEMBRE=
EOF
```

**¿Qué hace cada línea?**
- `ENVIRONMENT=production` → "Oye sistema, por defecto usa mi archivo `.env.prd.gpg`"
- `AMOR_AGOSTO=` → "Necesito esta variable en mi código" (el valor viene del archivo cifrado)
- `AMOR_DICIEMBRE=` → "También necesito esta otra variable"

💡 **Tip de Juanito**: El template es como una "lista de compras" - solo pides lo que realmente necesitas.

#### **Paso 6: ¡El Momento de la Verdad! 🎭**

Ahora Juanito puede ejecutar su proyecto sin que nadie vea sus secretos de amor:

```bash
# ¡Un solo comando y listo!
make run-secure
```

### **🎬 ¿Qué pasa internamente cuando Juanito ejecuta `make run-secure`?**

**¡Es como una película de espías! 🕵️‍♂️**

1. **📋 Lectura del Template**: 
   - Sistema: "A ver... leo `.envs/.env.template`"
   - Sistema: "¡Ah! Juanito quiere `ENVIRONMENT=production`, `AMOR_AGOSTO` y `AMOR_DICIEMBRE`"

2. **🔍 Búsqueda del Tesoro**:
   - Sistema: "Como dice production, busco `~/.rxd/love_history/.envs/.env.prd.gpg`"
   - Sistema: "¡Encontrado! 💎"

3. **🔓 Descifrado Seguro** (¡GPG pide la frase secreta!):
   - Sistema: "GPG, descifra esto por favor..."
   - GPG: "¿Cuál es tu frase secreta, Juanito?" 🔑
   - Juanito: *introduce su frase secreta*
   - GPG: "Listo jefe, aquí tienes las variables"

4. **💉 Inyección Directa** (¡Sin archivos temporales!):
   - Sistema: "Capturando variables: `AMOR_AGOSTO=Fran AMOR_DICIEMBRE=Diego`"
   - Sistema: "Inyectando directamente en el entorno de ejecución..."
   - Sistema: "¡Listo! Las variables están en memoria, no en archivos"

5. **🚀 Ejecución del Proyecto**:
   - Sistema: "¡A correr! `python3 src/main.py`"
   - Código de Juanito: "¡Genial! Ya tengo mis variables secretas"

6. **🧹 Limpieza Automática** (¡Sin rastros!):
   - Sistema: "El proceso terminó, liberando memoria..."
   - Sistema: "¡Variables eliminadas del entorno!"

**🔒 Lo SÚPER genial**: ¡Las variables NUNCA se guardan en archivos locales! Solo existen en memoria durante la ejecución. ¡Máxima seguridad! 🛡️

### **🔧 ¿Cómo funciona técnicamente el `make run-secure`?**

```bash
# 1. Captura las variables directamente del CLI
exported_vars=$$(rxd_cli process $(PROJECT_PATH) $(ORGANIZATION))

# 2. Las inyecta en el entorno actual (¡sin archivos!)
for var in $$exported_vars; do export $$var; done

# 3. Ejecuta el programa con esas variables ya disponibles
bash -c "set -o allexport; python3 src/main.py"
```

**🛡️ Seguridad nivel JAMES BOND**:
- ✅ GPG solicita frase secreta para descifrar
- ✅ Variables solo en memoria, nunca en disco
- ✅ Se eliminan automáticamente al terminar el proceso
- ✅ Zero archivos temporales en tu proyecto

### **Resultado Final para Juanito:**
```
love_history/                     # Proyecto de Juanito
├── makefile                      # ORGANIZATION := love_history
├── src/
│   └── main.py                   # Usa las variables
└── .envs/
    └── .env.template             # Define qué variables necesita

~/.rxd/                           # Sistema central
├── cli.py                        # Código del CLI
└── love_history/                 # Organización de Juanito
    └── .envs/
        └── .env.prd.gpg         # Variables cifradas de forma segura
```

### **🏆 Ventajas para Juanito (y su vida amorosa):**

- 🔐 **Seguridad EXTREMA**: Cifrado AES256 + frase secreta + variables solo en memoria. ¡Ni la NSA sabría de Fran y Diego!
- 🚀 **Super Simplicidad**: Un solo `make run-secure`, introduce tu frase secreta y ¡listo!
- 👥 **Colaboración Sin Vergüenza**: Puede subir el proyecto a GitHub sin que sus compañeros vean sus crushes
- 🎭 **Multi-Ambiente**: Puede crear `.env.dev.gpg` para sus "amores de prueba" 😉  
- 🎯 **Control Total**: Solo las variables del template se inyectan - nada de variables "sorpresa"
- 💾 **Zero Archivos Locales**: Las variables NUNCA tocan el disco de su computadora
- 🔑 **Autenticación Requerida**: GPG siempre pide su frase secreta personal

**💖 Juanito puede dormir tranquilo sabiendo que sus secretos están a salvo** 😴

---

## 🚀 Integración en Tu Proyecto

### Paso 1: Copiar el Makefile
```bash
# Copia el makefile a tu proyecto
cp makefile tu-nuevo-proyecto/
cd tu-nuevo-proyecto/

# Edita la organización
sed -i 's/ORGANIZATION := jalo/ORGANIZATION := tu-organizacion/' makefile
```

### Paso 2: Crear Template de Variables
```bash
# Crea la estructura
mkdir -p .envs/

# Define tus variables requeridas
cat > .envs/.env.template << EOF
ENVIRONMENT=development
DATABASE_URL=
API_KEY=
SECRET_TOKEN=
EOF
```

### Paso 3: Cifrar Variables por Ambiente

> **⚠️ IMPORTANTE**: Los archivos DEBEN tener nombres específicos para funcionar:
> - **`.env.dev`** → Para desarrollo (genera `.env.dev.gpg`)
> - **`.env.prd`** → Para producción (genera `.env.prd.gpg`) 
> - **`.env.stg`** → Para staging (genera `.env.stg.gpg`)

```bash
# Crea archivos .env para cada ambiente (NOMBRES EXACTOS)
echo "DATABASE_URL=postgresql://localhost/myapp_dev" > .env.dev
echo "API_KEY=dev-api-key-123" >> .env.dev
echo "SECRET_TOKEN=dev-secret-123" >> .env.dev

echo "DATABASE_URL=postgresql://prod-server/myapp" > .env.prd
echo "API_KEY=prod-api-key-xyz" >> .env.prd
echo "SECRET_TOKEN=prod-secret-xyz" >> .env.prd

# Cifra para cada ambiente
make encrypt file=.env.dev   # → Genera ~/.rxd/tu-org/.envs/.env.dev.gpg
make encrypt file=.env.prd   # → Genera ~/.rxd/tu-org/.envs/.env.prd.gpg

# Elimina archivos originales por seguridad
rm .env.dev .env.prd
```

### Paso 4: Usar en Tu Aplicación
```bash
# Ejecuta con variables automáticamente inyectadas
make run-secure

# O para ambiente específico
ENVIRONMENT=production make run-secure
```

**¡Tu proyecto ya está integrado!** 🎉

---

## 📖 Documentación Técnica Completa

### **Lectura Obligatoria**

La correcta implementación de Central Var RXD requiere la lectura completa de la documentación específica. Cada documento contiene información técnica crítica para el funcionamiento del sistema.

### **1. [Instalación y Configuración](docs/installer.md)** - **PRIORITARIO**

**Importancia crítica:**
- La instalación incorrecta de dependencias impide el funcionamiento del sistema
- La configuración de `RXD_LOCAL_ENV_PATH` es fundamental para la localización de archivos
- La configuración del PATH es necesaria para la ejecución de `rxd_cli`

**Contenido del documento:**
- Instalación de dependencias: Python3, Click, GPG
- Configuración de variables de entorno: `RXD_LOCAL_ENV_PATH`
- Configuración del binario para ejecución en terminal
- Procedimientos de verificación de instalación

### **2. [Uso del CLI](docs/cli.md)** - **ESENCIAL**

**Importancia crítica:**
- El desconocimiento de los comandos del CLI impide el uso del sistema
- La sintaxis incorrecta de parámetros genera errores de ejecución
- La comprensión de la estructura de comandos es esencial para el cifrado correcto

**Contenido del documento:**
- 5 comandos fundamentales: `encrypt`, `decrypt`, `process`, `hello`, `init`
- Sintaxis específica: parámetros obligatorios y opcionales
- Ejemplos de implementación para cada comando
- Parámetros críticos: `--organization`, rutas, nombres de archivos

### **3. [Uso del Makefile](docs/makefile.md)** - **FUNDAMENTAL**

**Importancia crítica:**
- La comprensión de variables del Makefile es necesaria para la personalización
- El conocimiento de comandos es esencial para la ejecución de proyectos
- La configuración correcta previene errores de organización

**Contenido del documento:**
- 4 variables críticas: `PROJECT_PATH`, `ORGANIZATION`, `GENERATE_FILE`, `RXD_DEBUG`
- 3 comandos principales: `run-secure`, `encrypt`, `decrypt`
- Configuración completa con ejemplos funcionales
- Sintaxis específica para cada comando

### **Metodología de Estudio Recomendada**

1. Leer cada documento completamente, línea por línea
2. Ejecutar todos los comandos de ejemplo proporcionados
3. Verificar el funcionamiento de cada paso antes de continuar
4. Documentar parámetros importantes para referencia
5. Probar comandos en un entorno de desarrollo seguro

### **Garantía de Éxito**
La lectura completa y comprensión de estos tres documentos garantiza el 99% de éxito en la implementación de Central Var RXD. La omisión de esta documentación resulta en una probabilidad equivalente de problemas técnicos.

### **Consecuencias de Omitir la Documentación**

**Por omitir [Instalación y Configuración](docs/installer.md):**
- Errores de "comando no encontrado"
- Errores de "variable de entorno no definida"
- Imposibilidad de localizar archivos cifrados
- Tiempo significativo invertido en resolución de problemas

**Por omitir [Uso del CLI](docs/cli.md):**
- Cifrado de archivos en ubicaciones incorrectas
- Imposibilidad de descifrar archivos propios
- Uso incorrecto de organizaciones
- Errores de ejecución con mensajes confusos

**Por omitir [Uso del Makefile](docs/makefile.md):**
- Configuración incorrecta de organización
- Fallos en comandos `make`
- Imposibilidad de ejecutar proyectos de forma segura
- Configuración incorrecta de variables de debug

---

**Central Var RXD** - *Gestión segura y eficiente de variables de entorno para equipos de desarrollo*