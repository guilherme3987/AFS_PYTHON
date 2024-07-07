
import Pyro4  # Importa a biblioteca Pyro4 para execução de métodos remotos

def main():
    try:
        # Solicitar ao usuário que insira a URI do servidor
        uri = input("Digite a URI do servidor Pyro4: ").strip()
        file_server = Pyro4.Proxy(uri)  # Cria um proxy para o servidor de arquivos remoto

        while True:
            # Solicita ao usuário um comando e converte para minúsculas
            command = input("Digite o comando (create, read, list, mkdir, ls, createfile, readfile, lsdir, exit): ").strip().lower()

            if command == "create":
                # Comando para criar um arquivo
                filename = input("Digite o nome do arquivo: ").strip()
                content = input("Digite o conteúdo do arquivo: ").strip()
                print(file_server.create_file(filename, content))  # Chama o método remoto para criar o arquivo

            elif command == "read":
                # Comando para ler um arquivo
                filename = input("Digite o nome do arquivo: ").strip()
                print(file_server.read_file(filename))  # Chama o método remoto para ler o arquivo

            elif command == "list":
                # Comando para listar arquivos no diretório base
                print(file_server.list_files())  # Chama o método remoto para listar os arquivos

            elif command == "mkdir":
                # Comando para criar um diretório
                dirname = input("Digite o nome do diretório: ").strip()
                print(file_server.create_directory(dirname))  # Chama o método remoto para criar o diretório

            elif command == "ls":
                # Comando para listar diretórios no diretório base
                print(file_server.list_directories())  # Chama o método remoto para listar os diretórios

            elif command == "createfile":
                # Comando para criar um arquivo dentro de um diretório específico
                dirname = input("Digite o nome do diretório: ").strip()
                filename = input("Digite o nome do arquivo: ").strip()
                content = input("Digite o conteúdo do arquivo: ").strip()
                print(file_server.create_file_in_directory(dirname, filename, content))  # Chama o método remoto para criar o arquivo no diretório

            elif command == "readfile":
                # Comando para ler um arquivo dentro de um diretório específico
                dirname = input("Digite o nome do diretório: ").strip()
                filename = input("Digite o nome do arquivo: ").strip()
                print(file_server.read_file_in_directory(dirname, filename))  # Chama o método remoto para ler o arquivo no diretório

            elif command == "lsdir":
                # Comando para listar o conteúdo de um diretório específico
                dirname = input("Digite o nome do diretório: ").strip()
                print(file_server.list_directory_contents(dirname))  # Chama o método remoto para listar o conteúdo do diretório

            elif command == "exit":
                # Comando para sair do loop
                break

            else:
                # Comando desconhecido
                print("Comando desconhecido.")

    except Pyro4.errors.CommunicationError as e:
        # Tratamento de erro de comunicação com o servidor Pyro4
        print(f"Erro de comunicação: {e}")

    except Pyro4.errors.NamingError as e:
        # Tratamento de erro de nomeação com o servidor Pyro4
        print(f"Erro de nomeação: {e}")

    except Exception as e:
        # Tratamento de qualquer outro erro
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()  # Chama a função principal