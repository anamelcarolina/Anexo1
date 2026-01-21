import shutil
import os

PASTA_ZIPS = r"C:\Users\ana.andrade\Desktop\extrair_anexo\zips\20260119_AC-PRIME-v5.zip"
PASTA_ZIPS_2 = r"C:\Users\ana.andrade\Desktop\extrair_anexo\zips"
PASTA_ANEXO1 = "anexo1_separado"
PASTA_ZIP_ANEXO1 = "anexo1_zip"


# Quero listar todos os arquivos dentro da pasta_zips_2

todos_arquivos_diretorio = os.listdir(PASTA_ZIPS_2)



for arquivo in todos_arquivos_diretorio:
    n1, ex1 = os.path.splitext(arquivo)

    print(n1)
    print(ex1)












#file_path = PASTA_ZIPS
# Divide o caminho do arquivo e a extensão
#nome_arquivo, extensao_arquivo = os.path.splitext(file_path)

#print("\n" + "*" * 30)
#print("root: " + root)
#print("ext: " + ext)

# Cria um novo nome de arquivo com a nova extensão
#new_path = root + ".csv"
#print("Variável criada final: " + new_path) # /home/usuario/dados/analise.csv
