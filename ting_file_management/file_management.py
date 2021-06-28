import sys


def txt_importer(path_file):
    if ".txt" not in path_file:
        sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file) as file:
            content = file.read().split("\n")
            return content
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
