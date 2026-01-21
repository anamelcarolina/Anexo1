import zipfile
import os
import tempfile
import shutil

PASTA_ZIPS = "zips"
PASTA_ANEXO1 = "anexo1_separado"
PASTA_ZIP_ANEXO1 = "anexo1_zip"

os.makedirs(PASTA_ANEXO1, exist_ok=True)
os.makedirs(PASTA_ZIP_ANEXO1, exist_ok=True)

for nome_zip in os.listdir(PASTA_ZIPS):
    if not nome_zip.lower().endswith(".zip"):
        continue

    caminho_zip = os.path.join(PASTA_ZIPS, nome_zip)

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
                nome_arquivo = os.path.basename(anexo1)

                with tempfile.TemporaryDirectory() as temp_dir:
                    zip_ref.extract(anexo1, temp_dir)

                    caminho_temp = os.path.join(temp_dir, anexo1)
                    caminho_final = os.path.join(PASTA_ANEXO1, nome_arquivo)

                    contador = 1
                    nome_base, ext = os.path.splitext(nome_arquivo)
                    while os.path.exists(caminho_final):
                        caminho_final = os.path.join(
                            PASTA_ANEXO1,
                            f"{nome_base}_{contador}{ext}"
                        )
                        contador += 1

                    shutil.move(caminho_temp, caminho_final)

                    nome_zip_anexo1 = f"{os.path.splitext(os.path.basename(caminho_final))[0]}.zip"
                    caminho_zip_anexo1 = os.path.join(PASTA_ZIP_ANEXO1, nome_zip_anexo1)

                    with zipfile.ZipFile(caminho_zip_anexo1, 'w', zipfile.ZIP_DEFLATED) as novo_zip:
                        novo_zip.write(
                            caminho_final,
                            arcname=os.path.basename(caminho_final)
                        )

                print(f"✅ Anexo1 separado e zip criado: {nome_zip_anexo1}")

    except zipfile.BadZipFile:
        print(f"❌ Zip inválido: {nome_zip}")
