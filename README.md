# Fuel Calculator App

Fuel Calculator App es una aplicación de escritorio desarrollada en Python con Tkinter que permite calcular el volumen estimado de gasoil a partir de una medida ingresada en pulgadas.

## 🚀 Características

- Interfaz gráfica intuitiva basada en Tkinter
- Cálculo de volumen estimado de gasoil basado en datos JSON
- Empaquetado en un ejecutable `.exe` para fácil distribución

## 📦 Instalación

Para ejecutar el proyecto en un entorno de desarrollo, sigue estos pasos:

### 1️⃣ Clonar el repositorio

```sh
 git clone <URL_DEL_REPOSITORIO>
 cd Fuel-Calculator-App
```

### 2️⃣ Crear un entorno virtual (opcional, pero recomendado)

```sh
python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate     # En Windows
```

### 3️⃣ Instalar dependencias

Ejecuta el siguiente comando para instalar las dependencias necesarias:

```sh
pip install -r requirements.txt
```

## ▶️ Uso

Para ejecutar la aplicación en modo desarrollo, usa:

```sh
python fuel_calculator.py
```

## 🔧 Compilación a `.exe`

Para generar un ejecutable en Windows, utiliza el siguiente comando:

```sh
pyinstaller --onedir --noconsole --icon=fuel_calculator_ico.ico --add-data="fuel_calculator_ico.ico;." --upx-dir="E:\upx" --clean --noconfirm fuel_calculator.py
```

Esto generará el archivo `fuel_calculator.exe` junto a `_internal` en la carpeta `dist/`.

## 📜 Dependencias

La aplicación usa las siguientes librerías:

```
altgraph==0.17.4
numpy==2.2.2
packaging==24.2
pandas==2.2.3
pefile==2023.2.7
pyinstaller==6.12.0
pyinstaller-hooks-contrib==2025.1
python-dateutil==2.9.0.post0
pytz==2025.1
pywin32-ctypes==0.2.3
six==1.17.0
tk==0.1.0
tzdata==2025.1
```

## 📄 Licencia

Este proyecto está bajo la licencia propia, y no se permite su distribución.

---

📌 _Si encuentras algún problema, por favor abre un issue o contribuye con un PR._ 🚀
