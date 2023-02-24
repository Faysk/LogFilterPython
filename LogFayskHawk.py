import os
import time

# Define o caminho do diretório de log em log_path
log_path = r"\\Name-Server\log"

# Entra em um loop que continuará enquanto o servidor Name-Server estiver disponível
while os.system(f"ping -n 1 Name-Server >nul 2>&1") == 0:
    # Conta o número de arquivos de log para cada nível (INFO, ERROR, WARNING)
    info_count = len([filename for filename in os.listdir(log_path) if filename.endswith('.log') and ': INFO' in open(os.path.join(log_path, filename)).read()])
    error_count = len([filename for filename in os.listdir(log_path) if filename.endswith('.log') and ': ERROR' in open(os.path.join(log_path, filename)).read()])
    warning_count = len([filename for filename in os.listdir(log_path) if filename.endswith('.log') and ': WARNING' in open(os.path.join(log_path, filename)).read()])

    # Conta o número total de linhas em todos os arquivos de log
    total_count = sum([int(open(os.path.join(log_path, filename)).read().count('\n')) for filename in os.listdir(log_path) if filename.endswith('.log')])

    # Cria uma string contendo as informações de contagem de logs, incluindo a contagem total de linhas
    log_info = f"Quantidade de informativos: {info_count}\nQuantidade de erros: {error_count}\nQuantidade de avisos: {warning_count}\nQuantidade total: {total_count}"

    # Exibe as informações de contagem de logs, incluindo a contagem total de linhas
    print(log_info)
    print()

    # Exibe as últimas 20 linhas dos arquivos de log
    print("20 últimas linhas de log:")
    for filename in os.listdir(log_path):
        if filename.endswith('.log'):
            with open(os.path.join(log_path, filename), 'r') as f:
                print(f"\n{filename}")
                print('\n'.join(list(f)[-20:]))

    # Aguarda 60 segundos antes de limpar o console e começar o loop novamente
    time.sleep(60)
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa o console, dependendo do sistema operacional
