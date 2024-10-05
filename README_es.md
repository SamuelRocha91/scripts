# <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Logo" width="52" height="30" /> Repositorio de Scripts de Python <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Logo" width="52" height="30" />

![En desarrollo](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow)

## 🌐 
[![Portugués](https://img.shields.io/badge/Português-green)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README.md)
[![Español](https://img.shields.io/badge/Español-yellow)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_es.md)
[![Inglés](https://img.shields.io/badge/English-blue)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_en.md)
[![Ruso](https://img.shields.io/badge/Russian-lightgrey)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ru.md)
[![Chino](https://img.shields.io/badge/Chinese-red)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ch.md)
[![Árabe](https://img.shields.io/badge/Arabic-orange)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ar.md)

<details>
<summary> 
  <h2>
    Sobre el Repositorio
  </h2>
</summary>

Este repositorio contiene scripts de Python en desarrollo. Actualmente, incluye un script que utiliza Selenium WebDriver para interactuar con páginas web.

</details>

<details>
<summary><h2>Requisitos</h2></summary>

Antes de ejecutar el script, necesitas tener algunos requisitos previos instalados:

- Python 3.x
- Pip (gestor de paquetes de Python)
- [Google Chrome](https://www.google.com/chrome/) (o cualquier otro navegador compatible con Selenium WebDriver)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (si no utilizas `webdriver_manager`)

</details>

<details>
<summary><h2>Configuración del Entorno</h2></summary>

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/usuario/repo.git
   cd repo
   ```

2. **Crea un archivo `.env` en la raíz del proyecto** con la ubicación del binario del navegador:

   ```env
   CHROME_BINARY_LOCATION=/ruta/a/tu/chrome
   ```

   **Nota:** Asegúrate de reemplazar `/ruta/a/tu/chrome` con la ruta real del binario del navegador en tu máquina.

3. **Instala las dependencias del proyecto:**

   ```bash
   pip install -r requirements.txt
   ```

   El archivo `requirements.txt` debe contener las siguientes bibliotecas:

   ```
   selenium
   webdriver-manager
   python-dotenv
   ```

   Puedes crear este archivo con el siguiente comando:

   ```bash
   pip freeze > requirements.txt
   ```

</details>

<details>
<summary><h2>Ejecutando el Script</h2></summary>

1. **Ejecuta el script de Python:**

   ```bash
   python3 /ruta/a/tu/script/vagas.py
   ```

   Asegúrate de ajustar la ruta del script según sea necesario.

</details>

<details>
<summary><h2>Otros Proyectos</h2></summary>

-  [Pedidos de Restaurante](https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_es.md)
-  [Algoritmos](https://github.com/SamuelRocha91/Algorithms/blob/main/README_es.md)
-  [Trybe is not Google](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_es.md)

</details>