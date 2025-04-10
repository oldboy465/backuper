import os
import shutil
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Função para organizar a pasta selecionada pelo usuário
def organizar_pasta():
    # Cria uma janela Tkinter invisível para abrir a caixa de diálogo
    Tk().withdraw()

    # Abre a caixa de diálogo para o usuário selecionar a pasta principal
    print("Selecione a pasta principal onde estão os arquivos:")
    pasta_principal = askdirectory(title="Selecione a pasta principal")

    if not pasta_principal:
        print("Nenhuma pasta foi selecionada. Encerrando o programa.")
        return

    # Obtém a data atual no formato dd-mm-yyyy
    data_atual = datetime.now().strftime("%d-%m-%Y")
    nome_pasta_backup = f"backup {data_atual}"

    # Caminho completo para a nova pasta de backup
    backup_path = os.path.join(pasta_principal, nome_pasta_backup)

    # Cria a pasta de backup, se ela ainda não existir
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)
        print(f"Pasta de backup criada: {backup_path}")
    else:
        print(f"A pasta de backup já existe: {backup_path}")

    # Lista todos os itens na pasta principal
    for item in os.listdir(pasta_principal):
        item_path = os.path.join(pasta_principal, item)

        # Verifica se é um arquivo (ignora pastas)
        if os.path.isfile(item_path):
            # Move o arquivo para a pasta de backup
            try:
                shutil.move(item_path, backup_path)
                print(f"Arquivo movido: {item}")
            except Exception as e:
                print(f"Erro ao mover o arquivo {item}: {e}")

    print("Organização concluída!")

# Executa a função
if __name__ == "__main__":
    organizar_pasta()