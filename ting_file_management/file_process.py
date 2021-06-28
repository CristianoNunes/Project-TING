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
    if instance.__len__() < 1:
        sys.stdout.write("Não há elementos\n")
    else:
        file = instance.dequeue()['nome_do_arquivo']
        sys.stdout.write(f"Arquivo {file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        sys.stdout.write(str(file))
    except IndexError:
        sys.stderr.write("Posição inválida")
