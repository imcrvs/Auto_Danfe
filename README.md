# Auto_Danfe

Auto_Danfe é uma ferramenta simples, desenvolvida em Python para monitorar automaticamente uma pasta específica em busca de arquivos XML de notas fiscais, convertendo-os para PDF através de uma API e salvando-os em outra pasta. Além disso, o programa realiza automaticamente sua instalação, copiando o executável para "C:\Program Files\Auto_Danfe", criando atalhos das pastas XML e Danfes na área de trabalho e configurando sua execução automática na inicialização do Windows.

-------------------------------------------------------------------------------

FUNCIONALIDADES:

1. Monitoramento Automático:
- Utiliza a biblioteca watchdog para monitorar automaticamente a pasta C:\XMLs.
- Quando um novo arquivo XML é detectado, ele é convertido automaticamente.

2. Conversão Automática de XML para PDF:
- Envia automaticamente o XML para a API configurada em:
  https://ws.meudanfe.com/api/v1/get/nfe/xmltodanfepdf/API
- Salva automaticamente o PDF resultante em: C:\Danfes.

3. Configuração Automática de Ambiente:
- Cria automaticamente as pastas C:\XMLs e C:\Danfes caso elas ainda não existam.
- Cria automaticamente atalhos para ambas as pastas na Área de Trabalho.

3. Instalação Automática no Windows:
- Ao executar pela primeira vez, o programa se copia automaticamente para:
  C:\Program Files\Auto_Danfe\
- Cria automaticamente um atalho para seu executável na pasta inicializar do Windows, garantindo a execução automática em segundo plano ao iniciar o computador.

4. Execução em Segundo Plano:
- O executável é gerado com a opção "--noconsole", permitindo rodar silenciosamente em segundo plano.

--------------------------------------------------------------------------------
PRÉ-REQUISITOS:

- Python versão 3.8 ou superior instalado no computador.
  Download em: https://python.org/downloads/

- Bibliotecas Python necessárias:
  - watchdog
  - requests
  - pywin32

- Instalação das bibliotecas:
  pip install watchdog requests pywin32

- Privilégios Administrativos:
  - A instalação automática requer privilégios administrativos para copiar o executável para "Program Files" e criar atalhos.

--------------------------------------------------------------------------------

INSTALAÇÃO E EMPACOTAMENTO

1. Ambiente de Desenvolvimento:
- Clone o projeto:
  git clone https://github.com/seuusuario/Auto_Danfe.git
  cd Auto_Danfe

- Ambiente virtual (recomendado):
  python -m venv venv
  venv\Scripts\activate

- Instalação das dependências:
  pip install -r requirements.txt
  ou manualmente:
  pip install watchdog requests pywin32

2. Gerar o executável com PyInstaller:
- Instale o PyInstaller:
  pip install pyinstaller

- Comando para gerar executável (sem console):
  pyinstaller --onefile --noconsole main.py
- Executável ficará disponível na pasta "dist".

--------------------------------------------------------------------------------

COMO FUNCIONA:

Ao ser executado pela primeira vez, o programa realiza:

1. Instalação automática:
  - Copia automaticamente o executável para:
    C:\Program Files\Auto_Danfe\
  - Cria automaticamente um atalho para inicialização em:
    %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

2. Configuração automática do ambiente:
  - Cria automaticamente as pastas:
    C:\XMLs e C:\Danfes
  - Cria atalhos automaticamente na Área de Trabalho para:
    C:\XMLs
    C:\Danfes

3. Monitoramento e Conversão:
  - Monitora automaticamente a pasta C:\XMLs.
  - Converte automaticamente XML para PDF na pasta C:\Danfes.

COMO USAR:

1. Executar o programa:
- Execute o Auto_Danfe.exe (após gerado pelo PyInstaller).
- Certifique-se de que o executável foi copiado automaticamente para C:\Program Files\Auto_Danfe\.

2. Coloque arquivos XML:
- Coloque arquivos XML de notas fiscais em C:\XMLs.
- O PDF será gerado automaticamente na pasta C:\Danfes.

3. Verificar atalhos:
- Na Área de Trabalho estarão atalhos rápidos para as pastas C:\XMLs e C:\Danfes.
- O programa iniciará automaticamente com o Windows através do atalho na pasta Startup.

CONTRIBUIÇÃO:

Para sugerir melhorias ou correções, abra uma issue ou envie um pull request no repositório do GitHub.

LICENÇA:

MIT License.

CONTATO: marcos@demarcco.com.br ou contato@demarcco.com.br
