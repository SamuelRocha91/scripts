# <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Logo" width="52" height="30" /> Repositório de Scripts Python <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Logo" width="52" height="30" />

![Em desenvolvimento](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

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
    Sobre o Repositório
  </h2>
</summary>

Este repositório contém scripts Python em desenvolvimento. Atualmente, o repositório inclui um script que utiliza o Selenium WebDriver para interagir com páginas da web. 

</details>

<details>
<summary><h2>Requisitos</h2></summary>

Antes de rodar o script, você precisa ter alguns pré-requisitos instalados:

- Python 3.x
- Pip (gerenciador de pacotes do Python)
- [Google Chrome](https://www.google.com/chrome/) (ou outro navegador compatível com o Selenium WebDriver)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (se você não utilizar `webdriver_manager`)

</details>

<details>
<summary><h2>Configuração do Ambiente</h2></summary>

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/usuario/repo.git
   cd repo
   ```

2. **Crie um arquivo `.env` na raiz do projeto** com a localização do binário do navegador:

   ```env
   CHROME_BINARY_LOCATION=/caminho/para/seu/chrome
   ```

   **Nota:** Certifique-se de substituir `/caminho/para/seu/chrome` pelo caminho real do binário do navegador em sua máquina.

3. **Instale as dependências do projeto:**

   ```bash
   pip install -r requirements.txt
   ```

   O arquivo `requirements.txt` deve conter as seguintes bibliotecas:

   ```
   selenium
   webdriver-manager
   python-dotenv
   ```

   Você pode criar esse arquivo com o seguinte comando:

   ```bash
   pip freeze > requirements.txt
   ```

</details>

<details>
<summary><h2>Rodando o Script</h2></summary>

1. **Execute o script Python:**

   ```bash
   python3 /caminho/para/seu/script/vagas.py
   ```

   Certifique-se de ajustar o caminho do script conforme necessário.

</details>
<details>
<summary><h2>Outros projetos</h2></summary>

-  [Restaurant Orders](https://github.com/SamuelRocha91/restaurantOrders)
-  [Algorithms](https://github.com/SamuelRocha91/Algorithms)
-  [Trybe is not google](https://github.com/SamuelRocha91/trybeIsNotGoogle)

</details>