# Importa o módulo os para manipulação do sistema de arquivos
import os

# Importa a biblioteca Pyro4 para execução de métodos remotos
import Pyro4

# Classe FileServer com seus métodos
@Pyro4.expose
class FileServer:

    # Inicializa o servidor de arquivos com um diretório de armazenamento padrão
    def __init__(self, storage_dir="file_storage"):
        self.base_dir = storage_dir
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    # Método para criar um novo arquivo
    def create_file(self, filename, content):
        filepath = os.path.join(self.base_dir, filename)
        if os.path.exists(filepath):
            return "File already exists."
        with open(filepath, 'w') as f:
            f.write(content)
        return f"File '{filename}' created."

    # Método para ler o conteúdo de um arquivo
    def read_file(self, filename):
        filepath = os.path.join(self.base_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return f.read()
        return "File not found."

    # Método para listar todos os arquivos no diretório base
    def list_files(self):
        return [name for name in os.listdir(self.base_dir) if os.path.isfile(os.path.join(self.base_dir, name))]


    # Método para criar um novo diretório
    def create_directory(self, dirname):
        dirpath = os.path.join(self.base_dir, dirname)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
            return f"Directory '{dirname}' created."
        return f"Directory '{dirname}' already exists."

    # Método para listar todos os diretórios no diretório base
    def list_directories(self):
        return [name for name in os.listdir(self.base_dir) if os.path.isdir(os.path.join(self.base_dir, name))]

    # Método para criar um arquivo dentro de um diretório específico
    def create_file_in_directory(self, dirname, filename, content):
        dirpath = os.path.join(self.base_dir, dirname)
        if not os.path.exists(dirpath):
            return f"Directory '{dirname}' does not exist."
        filepath = os.path.join(dirpath, filename)
        if os.path.exists(filepath):
            return f"File '{filename}' already exists in directory '{dirname}'."
        with open(filepath, 'w') as f:
            f.write(content)
        return f"File '{filename}' created in directory '{dirname}'."

    # Método para ler o conteúdo de um arquivo dentro de um diretório 
    def read_file_in_directory(self, dirname, filename):
        dirpath = os.path.join(self.base_dir, dirname)
        filepath = os.path.join(dirpath, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return f.read()
        return f"File '{filename}' not found in directory '{dirname}'."

    def list_directory_contents(self, dirname):
        dirpath = os.path.join(self.base_dir, dirname)
        if not os.path.exists(dirpath):
            return f"Directory '{dirname}' not found."
        contents = []
        for name in os.listdir(dirpath):
            item_path = os.path.join(dirpath, name)
            if os.path.isfile(item_path):
                contents.append(f"File: {name}")
            elif os.path.isdir(item_path):
                contents.append(f"Directory: {name}")
        return contents

def main():
    # Defina o endereço IP do servidor
    hostname = "26.158.1.41"  # Permite conexões de qualquer endereço IP
    daemon = Pyro4.Daemon(host=hostname)
    uri = daemon.register(FileServer, "example.fileserver")

    print(f"Ready. Object URI = {uri}")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
