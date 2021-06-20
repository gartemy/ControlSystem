from transliterate import translit

def word_change(document_name):
    document_name = document_name.replace(' ', '')
    document_name = document_name.replace('_', '')
    document_name = document_name.replace("(", "")
    document_name = document_name.replace(")", "")
    document_name = translit(document_name, language_code = 'ru', reversed=True)
    document_name = document_name.replace("'", "")
    return document_name