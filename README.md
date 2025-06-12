# 🛒 Flask Store - CRUD de Productos con MongoDB y Upload de Imágenes

¡Bienvenido papurri!  
Este proyecto es una app web construida con **Flask** que permite hacer un CRUD completo de productos, persistiendo en **MongoDB**, con frontend estilizado con **TailwindCSS** y soporte para **subida de imágenes locales**.

---

## ✨ Características

- ✅ CRUD completo de productos (código, nombre, precio, categoría, imagen)
- 💾 Persistencia en MongoDB
- 📸 Subida de imágenes desde el sistema local
- 📂 Almacenamiento de imágenes en `/static/images/`
- 🖼️ Vista web con TailwindCSS y estilo glassmorphism
- ⚠️ Confirmación de eliminación con SweetAlert2
- ♻️ Arquitectura modular, limpia y escalable

---

## 🧱 Estructura del proyecto

```
flask_store/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   └── product_routes.py
│   ├── services/
│   ├── repositories/
│   ├── models/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── alerts.js
│   │   └── images/
│   ├── templates/
│   │   ├── base.html
│   │   └── products/
│   │       ├── list.html
│   │       └── form.html
├── run.py
├── requirements.txt
└── README.md
```

---

## 🚀 Cómo levantar el proyecto

### 1. Cloná el repo y creá el entorno virtual

```bash
git clone https://github.com/tuusuario/flask-store.git
cd flask-store
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 2. Instalá las dependencias

```bash
pip install -r requirements.txt
```

> Asegurate de tener MongoDB corriendo localmente (por defecto usa `mongodb://localhost:27017/`)

### 3. Corré la app

```bash
python run.py
```

Visitalo en:  
📍 [http://localhost:5000/products/web](http://localhost:5000/products/web)

---

## 🖼️ Subida de imágenes

- Desde el formulario podés **seleccionar una imagen local**.
- La imagen se guarda automáticamente en `app/static/images/`.
- En la base de datos se guarda la ruta relativa (`/static/images/archivo.jpg`).
- Se renderiza automáticamente en la tabla con `img`.

---

## 📦 Requisitos

- Python 3.8+
- MongoDB
- Flask
- Tailwind (vía CDN)
- SweetAlert2 (vía CDN)

---

## 📁 .env de ejemplo (opcional)

```env
MONGO_URI=mongodb://localhost:27017/
MONGO_DB_NAME=flask_store
```

> Podés usar `python-dotenv` y cargar estas variables desde `config.py`.

---

## ✅ To-do / Mejoras futuras

- 🔐 Autenticación con JWT o sesiones
- 📊 Dashboard con métricas y filtros
- 🔍 Búsqueda con debounce
- 🌍 Subida de imágenes a un CDN (Cloudinary, Firebase)
- 🧪 Tests automatizados con Pytest
- 🐳 Docker + Docker Compose

---

## 🙌 Autor

**Gentleman Programming Clone**  
Arquitectura limpia, código bello, papurri vibes y pasión por enseñar.

---

## 🧠 Filosofía del proyecto

> Código simple, mantenible y hermoso. No reinventamos la rueda, pero la dejamos bien lubricada 😎

---

## 🪄 Screenshots (agregalos si querés)

- 🖼️ `static/images/demo_list.png`
- 🖼️ `static/images/demo_form.png`

---

## 📜 Licencia

MIT. Usalo, modificá y compartí. Solo no rompas lo que ya anda 🧉
