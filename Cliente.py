import Pyro4

def main():
    try:
        # Solicitar ao usuário que insira a URI do servidor
        uri = input("Digite a URI do servidor Pyro4: ").strip()
        file_server = Pyro4.Proxy(uri)

        while True:
            command = input("Digite o comando (create, read, list, mkdir, ls, createfile, readfile, lsdir, exit): ").strip().lower()
            if command == "create":
                filename = input("Digite o nome do arquivo: ").strip()
                content = input("Digite o conteúdo do arquivo: ").strip()
                print(file_server.create_file(filename, content))
            elif command == "read":
                filename = input("Digite o nome do arquivo: ").strip()
                print(file_server.read_file(filename))
            elif command == "list":
                print(file_server.list_files())
            elif command == "mkdir":
                dirname = input("Digite o nome do diretório: ").strip()
                print(file_server.create_directory(dirname))
            elif command == "ls":
                print(file_server.list_directories())
            elif command == "createfile":
                dirname = input("Digite o nome do diretório: ").strip()
                filename = input("Digite o nome do arquivo: ").strip()
                content = input("Digite o conteúdo do arquivo: ").strip()
                print(file_server.create_file_in_directory(dirname, filename, content))
            elif command == "readfile":
                dirname = input("Digite o nome do diretório: ").strip()
                filename = input("Digite o nome do arquivo: ").strip()
                print(file_server.read_file_in_directory(dirname, filename))
            elif command == "lsdir":
                dirname = input("Digite o nome do diretório: ").strip()
                print(file_server.list_directory_contents(dirname))
            elif command == "exit":
                break
            else:
                print("Comando desconhecido.")

    except Pyro4.errors.CommunicationError as e:
        print(f"Erro de comunicação: {e}")

    except Pyro4.errors.NamingError as e:
        print(f"Erro de nomeação: {e}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
