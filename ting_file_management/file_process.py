from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    contents = txt_importer(path_file)
    out = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(contents),
        "linhas_do_arquivo": contents
    }
    stop = False

    for data in instance._data:
        if(data["nome_do_arquivo"] == path_file):
            stop = True

    if not stop:
        instance.enqueue(out)

    sys.stdout.write(str(out))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
