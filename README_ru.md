# <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Logo" width="52" height="30" /> Репозиторий Python-скриптов <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Logo" width="52" height="30" />

![В разработке](https://img.shields.io/badge/Статус-В%20разработке-yellow)

## 🌐 
[![Португальский](https://img.shields.io/badge/Português-green)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README.md)
[![Испанский](https://img.shields.io/badge/Español-yellow)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_es.md)
[![Английский](https://img.shields.io/badge/English-blue)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_en.md)
[![Русский](https://img.shields.io/badge/Russian-lightgrey)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ru.md)
[![Китайский](https://img.shields.io/badge/Chinese-red)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ch.md)
[![Арабский](https://img.shields.io/badge/Arabic-orange)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ar.md)

<details>
<summary> 
  <h2>
    О репозитории
  </h2>
</summary>

Этот репозиторий содержит Python-скрипты, находящиеся в разработке. В настоящее время он включает в себя скрипт, который использует Selenium WebDriver для взаимодействия с веб-страницами.

</details>

<details>
<summary><h2>Требования</h2></summary>

Перед запуском скрипта вам необходимо установить некоторые предварительные требования:

- Python 3.x
- Pip (менеджер пакетов Python)
- [Google Chrome](https://www.google.com/chrome/) (или другой браузер, совместимый с Selenium WebDriver)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (если вы не используете `webdriver_manager`)

</details>

<details>
<summary><h2>Настройка окружения</h2></summary>

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/usuario/repo.git
   cd repo
   ```

2. **Создайте файл `.env` в корневой директории проекта** с указанием пути к бинарному файлу браузера:

   ```env
   CHROME_BINARY_LOCATION=/путь/к/вашему/chrome
   ```

   **Примечание:** Убедитесь, что вы заменили `/путь/к/вашему/chrome` на фактический путь к бинарному файлу браузера на вашем компьютере.

3. **Установите зависимости проекта:**

   ```bash
   pip install -r requirements.txt
   ```

---

Если вам нужны дополнительные изменения или добавления, дайте знать!
   Вы можете создать этот файл с помощью следующей команды:

   ```bash
   pip freeze > requirements.txt
   ```

</details>

<details>
<summary><h2>Запуск скрипта</h2></summary>

1. **Запустите Python-скрипт:**

   ```bash
   python3 /путь/к/вашему/script/vagas.py
   ```

   Убедитесь, что вы настроили путь к скрипту в соответствии с вашими потребностями.

</details>

<details>
<summary><h2>Другие проекты</h2></summary>

-  [Заказы ресторана](https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ru.md)
-  [Алгоритмы](https://github.com/SamuelRocha91/Algorithms/blob/main/README_ru.md)
-  [Trybe is not Google](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ru.md)

</details>