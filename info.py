import os
import os.path
import time
import sys

def pegar_info(arquivo):
    print(f"Nome: {arquivo}")
    print(f"Tamanho: {os.path.getsize(arquivo)}")
    print(f"Criado: {time.ctime(os.path.getctime(arquivo))}")
    print(f"Modificado: {time.ctime(os.path.getmtime(arquivo))}")
    print(f"Acessado: {time.ctime(os.path.getatime(arquivo))}")

if len(sys.argv) != 2:
    print("Usagem: info.py [arquivo]")
else:
    nome = sys.argv[1]
    pegar_info(nome)
