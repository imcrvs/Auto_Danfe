Auto_Danfe
Auto_Danfe é uma ferramenta simples, leve e eficaz desenvolvida em Python para monitorar uma pasta específica em busca de arquivos XML de notas fiscais, convertendo-os automaticamente para PDF através de uma API e salvando os PDFs em outra pasta. Além disso, o programa se instala automaticamente, copiando seu executável para "C:\Program Files\Auto_Danfe", criando atalhos para as pastas de XML e Danfes na área de trabalho e configurando sua execução automática na inicialização do Windows.

Funcionalidades
Monitoramento Automático:
Utiliza a biblioteca watchdog para monitorar a pasta C:\XMLs. Quando um novo XML é detectado, ele é processado automaticamente.

Conversão de XML para PDF:
Envia o arquivo XML para a API de conversão (configurada em https://ws.meudanfe.com/api/v1/get/nfe/xmltodanfepdf/API) e salva o PDF resultante na pasta C:\Danfes.

Criação Automática de Pastas e Atalhos:
Se as pastas C:\XMLs e C:\Danfes não existirem, o programa as cria. Além disso, atalhos para estas pastas são criados na área de trabalho do usuário.

Instalação Automática:
Ao ser executado, o programa copia seu próprio executável para C:\Program Files\Auto_Danfe\ e cria um atalho na pasta de inicialização do Windows para garantir que o programa rode em segundo plano sempre que o sistema iniciar.

Execução em Segundo Plano:
O executável é gerado com a opção --noconsole, permitindo sua execução sem a exibição de uma janela de console.

Pré-requisitos
Python 3.8 ou superior:
Certifique-se de ter o Python instalado. Baixe a versão mais recente em python.org/downloads.

Bibliotecas Python:
As seguintes bibliotecas são necessárias:

watchdog
requests
pywin32 (para criação de atalhos no Windows)
Você pode instalá-las utilizando pip:

bash
Copiar
pip install watchdog requests pywin32
Privilégios Administrativos:
Algumas operações (como copiar o executável para "Program Files" e criar atalhos na pasta de startup) podem requerer execução com privilégios de administrador.

Instalação e Empacotamento
1. Configurar o Ambiente de Desenvolvimento
Clone o Repositório:

bash
Copiar
git clone https://github.com/seuusuario/Auto_Danfe.git
cd Auto_Danfe
Crie um Ambiente Virtual (opcional, mas recomendado):

bash
Copiar
python -m venv venv
venv\Scripts\activate  # No Windows
Instale as Dependências:

bash
Copiar
pip install -r requirements.txt
Obs.: Caso não exista um arquivo requirements.txt, instale manualmente:

bash
Copiar
pip install watchdog requests pywin32
2. Gerar o Executável com PyInstaller
Instale o PyInstaller:

bash
Copiar
pip install pyinstaller
Empacote o Projeto: No diretório onde se encontra o arquivo main.py, execute:

bash
Copiar
pyinstaller --onefile --noconsole main.py
O executável gerado estará na pasta dist.

Como Funciona
Ao ser executado, o programa realiza as seguintes operações:

Instalação Automática:

Copia seu próprio executável para C:\Program Files\Auto_Danfe\ (caso ainda não esteja instalado).
Cria um atalho do executável na pasta de startup do Windows (%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup), garantindo a execução automática na inicialização do sistema.
Configuração do Ambiente:

Cria as pastas C:\XMLs e C:\Danfes, se elas ainda não existirem.
Cria atalhos para essas pastas na área de trabalho do usuário.
Monitoramento e Conversão:

Monitora a pasta C:\XMLs utilizando o watchdog.
Ao detectar um novo arquivo XML, o programa envia o arquivo para a API de conversão e salva o PDF resultante em C:\Danfes.
Uso
Após gerar o executável, siga os passos abaixo:

Executar o Programa:

Execute o arquivo gerado (por exemplo, Auto_Danfe.exe).
Se estiver rodando em ambiente de testes, você pode executar o executável diretamente. Para a instalação final, certifique-se de que o programa foi copiado para C:\Program Files\Auto_Danfe\ e que o atalho de startup foi criado.
Colocar Arquivos XML:

Coloque seus arquivos XML de nota fiscal na pasta C:\XMLs.
O programa detectará automaticamente os novos arquivos e gerará os PDFs correspondentes na pasta C:\Danfes.
Verificar Atalhos:

Os atalhos para as pastas C:\XMLs e C:\Danfes estarão na área de trabalho para acesso rápido.
O atalho na pasta de startup garante que o Auto_Danfe seja iniciado automaticamente com o Windows.
Contribuição
Contribuições são bem-vindas! Se você deseja melhorar o projeto ou corrigir algum problema, por favor abra uma issue ou envie um pull request.

Licença
Este projeto é licenciado sob a MIT License.

Contato
Para dúvidas ou sugestões, entre em contato através do seu email.
