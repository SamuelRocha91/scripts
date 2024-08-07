from dotenv import load_dotenv
import os

# Importa o módulo `webdriver` do pacote `selenium`,
#  que fornece classes para controlar navegadores.
from selenium import webdriver

# Importa a classe `Service` do módulo `chrome.service`
# para gerenciar o serviço do `chromedriver`.
from selenium.webdriver.chrome.service import Service

# Importa a classe `ChromeDriverManager` do pacote `webdriver_manager.chrome`
#  para gerenciar a instalação do `chromedriver`.
from webdriver_manager.chrome import ChromeDriverManager

# Carrega as variáveis de ambiente do arquivo `.env`.
load_dotenv()

# Obtém o caminho do executável do navegador Chrome
chrome_binary_location = os.getenv('CHROME_BINARY_LOCATION')

# Cria uma instância de `ChromeOptions`
# para definir opções específicas para o navegador Chrome.
options = webdriver.ChromeOptions()

# Define o local do executável do navegador Chrome.
#  Certifique-se de que este caminho está correto.
options.binary_location = chrome_binary_location

# Cria uma instância da classe `Service`,
#  que gerencia o serviço do `chromedriver`.
# `ChromeDriverManager().install()` baixa e instala o `chromedriver`
# adequado para a versão do Chrome.
service = Service(ChromeDriverManager().install())

# Cria uma instância do `webdriver.Chrome` usando o serviço
# e as opções configuradas.
driver = webdriver.Chrome(service=service, options=options)

# Abre a página da web especificada (neste caso, Google) no navegador.
driver.get('https://www.google.com')

# Imprime o título da página atual no console. O título é o texto que aparece
#  na aba do navegador.
print(driver.title)

# Fecha o navegador e encerra a sessão do WebDriver.
driver.quit()
