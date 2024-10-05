# <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Logo" width="52" height="30" /> Python脚本库 <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Logo" width="52" height="30" />

![开发中](https://img.shields.io/badge/状态-开发中-yellow)

## 🌐 
[![葡萄牙语](https://img.shields.io/badge/Português-green)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README.md)
[![西班牙语](https://img.shields.io/badge/Español-yellow)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_es.md)
[![英语](https://img.shields.io/badge/English-blue)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_en.md)
[![俄语](https://img.shields.io/badge/Russian-lightgrey)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ru.md)
[![中文](https://img.shields.io/badge/Chinese-red)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ch.md)
[![阿拉伯语](https://img.shields.io/badge/Arabic-orange)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ar.md)

<details>
<summary> 
  <h2>
    关于此库
  </h2>
</summary>

该库包含正在开发的Python脚本。目前，库中包括一个使用Selenium WebDriver与网页交互的脚本。

</details>

<details>
<summary><h2>要求</h2></summary>

在运行脚本之前，您需要安装一些前置条件：

- Python 3.x
- Pip（Python包管理器）
- [Google Chrome](https://www.google.com/chrome/)（或其他兼容Selenium WebDriver的浏览器）
- [ChromeDriver](https://sites.google.com/chromium.org/driver/)（如果您不使用`webdriver_manager`）

</details>

<details>
<summary><h2>环境配置</h2></summary>

1. **克隆库：**

   ```bash
   git clone https://github.com/usuario/repo.git
   cd repo
   ```

2. **在项目根目录创建一个`.env`文件**，其中包含浏览器二进制文件的位置：

   ```env
   CHROME_BINARY_LOCATION=/路径/到/您的/chrome
   ```

   **注意：**确保将`/路径/到/您的/chrome`替换为您计算机上浏览器二进制文件的实际路径。

3. **安装项目依赖：**

   ```bash
   pip install -r requirements.txt
   ```

   `requirements.txt`文件应包含以下库：

   ```
   selenium
   webdriver-manager
   python-dotenv
   ```

   您可以使用以下命令创建此文件：

   ```bash
   pip freeze > requirements.txt
   ```

</details>

<details>
<summary><h2>运行脚本</h2></summary>

1. **运行Python脚本：**

   ```bash
   python3 /路径/到/您的/script/vagas.py
   ```

   确保根据需要调整脚本路径。

</details>

<details>
<summary><h2>其他项目</h2></summary>

-  [餐厅订单](https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ch.md)
-  [算法](https://github.com/SamuelRocha91/Algorithms/blob/main/README_ch.md)
-  [Trybe不是谷歌](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ch.md)

</details>
