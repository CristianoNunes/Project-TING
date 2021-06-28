def exists_word(word, instance):
    ocurrences = []
    for index in range(len(instance._data)):
        text_lines = instance._data[index]['linhas_do_arquivo']
        line_ocurrences = []
        for index2 in range(len(text_lines)):
            if word in text_lines[index2]:
                line_ocurrences.append({"linha": index2 + 1})
        content = {
                    "palavra": word,
                    "arquivo": instance._data[index]['nome_do_arquivo'],
                    "ocorrencias": line_ocurrences
                }
        if len(line_ocurrences) > 0:
            ocurrences.append(content)

    return ocurrences


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
