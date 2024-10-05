# <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Logo" width="52" height="30" /> Python Scripts Repository <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Logo" width="52" height="30" />

![In Development](https://img.shields.io/badge/Status-In%20Development-yellow)

## 🌐 
[![Portuguese](https://img.shields.io/badge/Portuguese-green)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README.md)
[![Spanish](https://img.shields.io/badge/Spanish-yellow)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_es.md)
[![English](https://img.shields.io/badge/English-blue)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_en.md)
[![Russian](https://img.shields.io/badge/Russian-lightgrey)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ru.md)
[![Chinese](https://img.shields.io/badge/Chinese-red)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ch.md)
[![Arabic](https://img.shields.io/badge/Arabic-orange)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ar.md)

<details>
<summary> 
  <h2>
    About the Repository
  </h2>
</summary>

This repository contains Python scripts in development. Currently, it includes a script that uses Selenium WebDriver to interact with web pages.

</details>

<details>
<summary><h2>Requirements</h2></summary>

Before running the script, you need to have some prerequisites installed:

- Python 3.x
- Pip (Python package manager)
- [Google Chrome](https://www.google.com/chrome/) (or another browser compatible with Selenium WebDriver)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (if you are not using `webdriver_manager`)

</details>

<details>
<summary><h2>Environment Setup</h2></summary>

1. **Clone the repository:**

   ```bash
   git clone https://github.com/usuario/repo.git
   cd repo
   ```

2. **Create a `.env` file in the root of the project** with the browser binary location:

   ```env
   CHROME_BINARY_LOCATION=/path/to/your/chrome
   ```

   **Note:** Make sure to replace `/path/to/your/chrome` with the actual path to the browser binary on your machine.

3. **Install the project dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should contain the following libraries:

   ```
   selenium
   webdriver-manager
   python-dotenv
   ```

   You can create this file with the following command:

   ```bash
   pip freeze > requirements.txt
   ```

</details>

<details>
<summary><h2>Running the Script</h2></summary>

1. **Run the Python script:**

   ```bash
   python3 /path/to/your/script/vagas.py
   ```

   Make sure to adjust the script path as necessary.

</details>

<details>
<summary><h2>Other Projects</h2></summary>

-  [Restaurant Orders](https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_en.md)
-  [Algorithms](https://github.com/SamuelRocha91/Algorithms/blob/main/README_en.md)
-  [Trybe is not Google](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_en.md)

</details>
