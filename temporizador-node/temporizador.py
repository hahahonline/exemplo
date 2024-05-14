import time

def temporizador(segundos):
    print(f'Temporizador iniciado para {segundos} segundos.')
    time.sleep(segundos)
    print('Tempo esgotado!')

# tempo em segundos
tempo_em_segundos = 5
temporizador(tempo_em_segundos)
