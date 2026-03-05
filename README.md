## TutorAI – Instalación y ejecución

Este proyecto se compone de tres servicios:

- **frontend**: Next.js con Mantine y `socket.io-client` (puerto **3000**)
- **backend**: Django con Django Ninja (puerto **8000**)
- **streaming**: Node.js con Express y Socket.io (puerto **4000**)

---

### Requisitos previos

- **Node.js** (v18+ recomendado) y **npm** o **yarn**
- **Python 3.10+** y **pip**
- (Opcional pero recomendado) `virtualenv` o `python -m venv`

---

### Estructura del proyecto

- `frontend/`
- `api/`
- `streaming/`

---

### 1. Backend (Django + Django Ninja) – puerto 8000

#### 1.1 Crear y activar entorno virtual

```bash
cd api

# Crear entorno virtual
python -m venv .venv
```

Activar el entorno virtual:

- En **Linux/macOS**:

```bash
source .venv/bin/activate
```

- En **Windows (PowerShell)**:

```bash
.\.venv\Scripts\Activate.ps1
```

- En **Windows (CMD)**:

```bash
.\.venv\Scripts\activate.bat
```

#### 1.2 Instalar dependencias


Ejecuta:

```bash
pip install -r requirements.txt
```

Verifica que `django-cors-headers` esté incluido en el archivo `api/requirements.txt`, ya que es necesario para permitir CORS hacia el frontend.

#### 1.3 Migraciones y ejecución del servidor

```bash
python manage.py migrate
python manage.py runserver
```

El backend quedará escuchando en `http://localhost:8000` por defecto.

#### 1.4 Configuración de CORS en Django

- En `api/api/settings.py`, asegúrate de que `'corsheaders'` esté incluido en la lista `INSTALLED_APPS`.
- Verifica que `'corsheaders.middleware.CorsMiddleware'` esté en la lista `MIDDLEWARE` **por encima** de `'django.middleware.common.CommonMiddleware'`.
- Al final del archivo `settings.py`, define:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
```

> Nota: si el frontend no puede recibir datos del backend, verifica que `django-cors-headers` esté instalado (incluido en `api/requirements.txt`) y correctamente configurado en `api/api/settings.py`.

---

### 2. Frontend (Next.js + Mantine + socket.io-client) – puerto 3000

En una nueva terminal (dejando el backend corriendo):

```bash
cd frontend

# Instalar dependencias (elige una)
npm install
# o
yarn install
```

Para ejecutar el servidor de desarrollo:

```bash
npm run dev
# o
yarn dev
```

El frontend quedará disponible en `http://localhost:3000`.

---

### 3. Servicio de streaming (Node.js + Express + Socket.io) – puerto 4000

En otra terminal:

```bash
cd streaming

# Instalar dependencias
npm install
# o
yarn install
```

Para ejecutar el servidor (ajusta si tu script usa otro comando):

```bash
npm run dev
# o, si el proyecto está configurado así
npm start
```

El servicio de streaming quedará escuchando en `http://localhost:4000`.

---

### Resumen de puertos

- **Frontend (Next.js)**: `http://localhost:3000`
- **Backend (Django + Django Ninja)**: `http://localhost:8000`
- **Streaming (Node + Express + Socket.io)**: `http://localhost:4000`

