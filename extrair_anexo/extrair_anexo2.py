## essa biblioteca serve para abrir, ler, extrair e criar arquivos. No caso do projeto, ele abriu os zips, listou os arquivos dentro do zip, extraiu o Anexo1 umriou um novo zip
import zipfile 
import os 
import tempfile
import shutil

PASTA_ZIPS = "zips"
PASTA_ANEXO1 = "anexo1_separado"
PASTA_ZIP_ANEXO1 = "anexo1_zip"

os.makedirs(PASTA_ANEXO1, exist_ok=True) 
os.makedirs(PASTA_ZIP_ANEXO1, exist_ok=True)

for nome_zip in os.listdir(PASTA_ZIPS): #pega cada arquivo zip
    if not nome_zip.lower().endswith(".zip"): #se não terminar com .zip, pula
        continue

    caminho_zip = os.path.join(PASTA_ZIPS, nome_zip)

    nome_zip_sem_extensao, _ = os.path.splitext(nome_zip) # nome do zip SEM .zip (vai virar nome do Anexo1). Separa nome e extensão

    try:
        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            arquivos_anexo1 = [
                f for f in zip_ref.namelist()
                if "anexo1" in f.lower()
            ]

            if not arquivos_anexo1:
                print(f"⚠️ Anexo1 não encontrado em {nome_zip}")
                continue

            for anexo1 in arquivos_anexo1:
                nome_original = os.path.basename(anexo1)
                _, extensao = os.path.splitext(nome_original)

                with tempfile.TemporaryDirectory() as temp_dir:
                    zip_ref.extract(anexo1, temp_dir)

                    caminho_temp = os.path.join(temp_dir, anexo1)

                    # Anexo1 recebe o nome do ZIP (sem .zip) os.pathjoin() cria caminhos de arquivos, nesse caso, ele esta levando o nome_sem_zip (nome do zip sem zip)
                    #  para a pasta anexo1_separado (PASTA_ANEXO1) e colocando sua extensão real do Anexo1 (.csv)
                    caminho_final = os.path.join( #caminho final
                        PASTA_ANEXO1,
                        f"{nome_zip_sem_extensao}{extensao}"
                    )

                    # evita sobrescrever
                    contador = 1 #Esse numero vai ser usado para criar nomes diferentes se já existir um arquivo com o mesmo nome
                    while os.path.exists(caminho_final): #ele verifica se já existe um arquivo com esse caminho
                        caminho_final = os.path.join(
                            PASTA_ANEXO1,
                            f"{nome_zip_sem_extensao}_{contador}{extensao}" 
                        ) 
                        contador += 1

                    shutil.move(caminho_temp, caminho_final)

                    # cria zip com o mesmo nome base
                    caminho_zip_anexo1 = os.path.join(
                        PASTA_ZIP_ANEXO1,
                        f"{os.path.splitext(os.path.basename(caminho_final))[0]}.zip" #os.path.splitext separa o nome em duas partes 
                    )

                    with zipfile.ZipFile(caminho_zip_anexo1, 'w', zipfile.ZIP_DEFLATED) as novo_zip:
                        novo_zip.write(
                            caminho_final,
                            arcname=os.path.basename(caminho_final)
                        )

                print(f"✅ Anexo1 renomeado para '{nome_zip_sem_extensao}{extensao}' e zip criado")

    except zipfile.BadZipFile:
        print(f"❌ Zip inválido: {nome_zip}")
