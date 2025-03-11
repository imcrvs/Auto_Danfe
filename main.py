import os
import sys
import time
import shutil
import base64
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

try:
    import win32com.client
except ImportError:
    win32com = None
    print("O módulo win32com não foi encontrado. Para criar atalhos, instale o pywin32.")

# Caminhos fixos na máquina do usuário
XML_FOLDER = r"C:\XMLs"
PDF_FOLDER = r"C:\Danfes"
API_URL = "https://ws.meudanfe.com/api/v1/get/nfe/xmltodanfepdf/API"

# Pasta de instalação e caminho final do executável
INSTALL_FOLDER = r"C:\Program Files\Auto_Danfe"
INSTALLED_EXE_PATH = os.path.join(INSTALL_FOLDER, "Auto_Danfe.exe")

def read_file_with_retries(file_path, mode="rb", retries=5, delay=1):
    for attempt in range(1, retries + 1):
        try:
            with open(file_path, mode) as f:
                return f.read()
        except PermissionError as e:
            print(f"Tentativa {attempt} de ler {file_path} falhou (arquivo em uso). Aguardando {delay} segundos...")
            time.sleep(delay)
    raise PermissionError(f"Não foi possível acessar o arquivo {file_path} após {retries} tentativas.")

def convert_xml_to_pdf_api(xml_path, pdf_path):
    try:
        xml_data = read_file_with_retries(xml_path, "rb", retries=5, delay=1)
    except PermissionError as e:
        print(e)
        return False

    headers = {"Content-Type": "text/plain"}
    try:
        response = requests.post(API_URL, headers=headers, data=xml_data)
    except Exception as e:
        print(f"Erro ao chamar a API para {xml_path}: {e}")
        return False

    if response.status_code == 200:
        base64_pdf = response.text.strip('data:application/pdf;base64,').strip('"')
        try:
            pdf_data = base64.b64decode(base64_pdf)
        except Exception as e:
            print(f"Erro ao decodificar o PDF de {xml_path}: {e}")
            return False
        with open(pdf_path, "wb") as f:
            f.write(pdf_data)
        print(f"PDF gerado com sucesso: {pdf_path}")
        return True
    else:
        print(f"Falha na API para {xml_path}. Código HTTP: {response.status_code}")
        return False

class XmlEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.lower().endswith(".xml"):
            print(f"Novo XML detectado: {event.src_path}")
            base_name = os.path.splitext(os.path.basename(event.src_path))[0]
            pdf_path = os.path.join(PDF_FOLDER, f"{base_name}.pdf")
            if os.path.exists(pdf_path):
                print(f"PDF para {base_name} já existe. Ignorando.")
                return
            convert_xml_to_pdf_api(event.src_path, pdf_path)

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Pasta criada: {folder_path}")
    else:
        print(f"Pasta já existe: {folder_path}")

def create_shortcut(target, shortcut_path):
    if win32com is None:
        print("Não foi possível criar o atalho, pois o win32com não está instalado.")
        return
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = os.path.dirname(target)
    shortcut.save()
    print(f"Atalho criado: {shortcut_path}")

def setup_environment():
    # Cria as pastas de XMLs e Danfes na raiz do C:
    create_folder(XML_FOLDER)
    create_folder(PDF_FOLDER)
    
    # Cria atalhos para as pastas na área de trabalho
    desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
    xml_shortcut = os.path.join(desktop, "XMLs.lnk")
    danfes_shortcut = os.path.join(desktop, "Danfes.lnk")
    create_shortcut(XML_FOLDER, xml_shortcut)
    create_shortcut(PDF_FOLDER, danfes_shortcut)

def add_to_startup(exe_path):
    # Caminho da pasta de startup do usuário
    startup_folder = os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs\Startup")
    startup_shortcut = os.path.join(startup_folder, "Auto_Danfe.lnk")
    print(f"Tentando criar atalho na pasta startup: {startup_shortcut}")
    create_shortcut(exe_path, startup_shortcut)

def install_program():
    current_exe = os.path.abspath(sys.argv[0])
    if os.path.normcase(current_exe) == os.path.normcase(INSTALLED_EXE_PATH):
        print("Programa já está instalado em:", INSTALLED_EXE_PATH)
        return
    create_folder(INSTALL_FOLDER)
    try:
        shutil.copy(current_exe, INSTALLED_EXE_PATH)
        print(f"Executável copiado para: {INSTALLED_EXE_PATH}")
    except Exception as e:
        print(f"Erro ao copiar o executável para {INSTALL_FOLDER}: {e}")
        return
    add_to_startup(INSTALLED_EXE_PATH)

def main():
    install_program()            # Copia o executável para a pasta de instalação e adiciona o atalho na startup
    setup_environment()          # Cria as pastas (XMLs e Danfes) e os atalhos na área de trabalho
    create_folder(XML_FOLDER)    # Garante que a pasta XMLs exista
    create_folder(PDF_FOLDER)    # Garante que a pasta Danfes exista

    observer = Observer()
    event_handler = XmlEventHandler()
    observer.schedule(event_handler, XML_FOLDER, recursive=False)
    observer.start()
    print(f"Monitorando a pasta: {XML_FOLDER}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Encerrando monitoramento...")
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
