# Upload Bypass Tester

Ferramenta simples para testar filtros de upload de arquivos em aplicações web, utilizando múltiplas extensões, nomes aleatórios de arquivos e técnicas comuns de bypass para identificar validações inseguras.

---

## Funcionalidades

- Gera nomes aleatórios para cada upload
- Testa múltiplas extensões:
  - PHP
  - ASP/ASPX
  - JSP
  - CGI/Perl/Python/Ruby
  - HTML/JS
  - Imagens
  - Documentos

- Utiliza técnicas comuns de bypass:
  - Double extension
  - Null byte (`%00`)
  - Uppercase/lowercase bypass
  - Trailing spaces
  - Fake image extension
  - MIME spoofing

- Exibe resultados em tempo real:
  - `[ACEITO]`
  - `[BLOQUEADO]`
  - `[ERRO]`

---

## Requisitos

- Python 3
- Biblioteca `requests`

### Instalação

```bash
pip install requests
```

Uso
Executar normalmente

```python
python3 ubt.py http://URL
```

Exibir apenas uploads aceitos

```python
python3 ubt.py http://URL | grep -v "BLOQUEADO"
```

Exemplo

```python
python3 ubt.py http://target/upload.php
```

Saída
```text
[ACEITO] xkfjre.php.jpg | HTTP 200
[BLOQUEADO] abcdex.php | HTTP 403
[ACEITO] qwerty.phtml | HTTP 201
```

Como funciona

O script:

```text
Gera nomes aleatórios para os arquivos
Cria arquivos temporários automaticamente
Aplica múltiplas combinações de extensões e bypasses
Define MIME types aleatórios
Realiza upload via multipart/form-data
Analisa as respostas HTTP da aplicação
Payloads testados
```

Exemplos de formatos gerados:

```text
random.php
random.php.jpg
random.jpg.php
random.php%00.jpg
random.PHP
random.php...
```

O prefixo random representa nomes gerados aleatoriamente pelo script.
