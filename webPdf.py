from bs4 import BeautifulSoup
import subprocess
import os
from PyPDF2 import PdfReader

# Suponha que você tenha o conteúdo HTML em uma string chamada html_content
html_content = """
    <!DOCTYPE html>
        <html>
        <head>
            <title>Título da Página</title>
        </head>
        <body>
            <p>Conteúdo da página 1</p>
            <br style="page-break-after: always;">
            <p>Conteúdo da página 2222e2w3</p>
        </body>
        </html>
"""

# Crie um objeto BeautifulSoup para analisar o HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Salve o conteúdo HTML em um arquivo temporário
html_file = 'temp.html'
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))

# Converta o HTML para PDF usando wkhtmltopdf
pdf_file = 'pdfile.pdf'
wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf'
cmd_line = f'"{wkhtmltopdf_path}" "{html_file}" "{pdf_file}"'
subprocess.run(cmd_line, shell=True)

# Verifique se o arquivo PDF foi gerado corretamente
if os.path.exists(pdf_file):
    # Obtenha o número de páginas do PDF
    with open(pdf_file, 'rb') as f:
        reader = PdfReader(f)
        num_pages = len(reader.pages)
        print(f'O total de folhas A4 necessárias para imprimir o conteúdo é: {num_pages}')
else:
    print("Erro: Arquivo PDF não encontrado.")
