# 📦 Extrator de Anexo1 de Arquivos ZIP (Python)

Este projeto em Python, para o meu estagio, automatiza a extração do Anexo1 de vários arquivos .zip, renomeando o arquivo extraído com o nome do zip de origem (sem .zip) e gerando um novo zip com esse mesmo nome.

O objetivo é evitar trabalho manual ao lidar com muitos arquivos compactados.

--------------------------------------------------

🎯 O que o script faz

Para cada arquivo .zip dentro da pasta zips, o script:

- Abre o arquivo .zip
- Procura arquivos que contenham "Anexo1" no nome
- Extrai somente o Anexo1
- Renomeia o arquivo extraído com o nome do zip original
- Mantém a extensão original do arquivo (ex: .csv)
- Salva o arquivo renomeado na pasta anexo1_separado
- Cria um novo .zip com o mesmo nome base
- Salva o novo zip na pasta anexo1_zip

--------------------------------------------------

📁 Estrutura de pastas esperada

extrair_anexo/
├── zips/
│   ├── 20260119_AC-PRIME-v5.zip
│   └── outro_arquivo.zip
├── anexo1_separado/
│   └── 20260119_AC-PRIME-v5.csv
├── anexo1_zip/
│   └── 20260119_AC-PRIME-v5.zip
└── extrair_anexo1.py

--------------------------------------------------

▶️ Como executar

1) Pré-requisitos

- Python 3.8 ou superior
- Windows, Linux ou macOS

Verifique se o Python está instalado:

python --version

--------------------------------------------------

2) Clone o repositório

git clone https://github.com/seu-usuario/extrair-anexo1.git
cd extrair-anexo1

--------------------------------------------------

3) Adicione os arquivos ZIP

Coloque todos os arquivos .zip dentro da pasta:

zips/

Não é necessário renomear os arquivos manualmente.

--------------------------------------------------

4) Execute o script

python extrair_anexo1.py

--------------------------------------------------

✅ Resultado

- Pasta anexo1_separado: arquivos Anexo1 extraídos e renomeados (ex: .csv)
- Pasta anexo1_zip: novos arquivos .zip criados automaticamente

Se algum zip não contiver um Anexo1, o script apenas informa no terminal.

--------------------------------------------------

🧠 Lógica utilizada

- os.listdir(): lista arquivos de uma pasta
- zipfile.ZipFile(): leitura e criação de arquivos .zip
- namelist(): lista arquivos dentro do zip
- os.path.splitext(): separa nome e extensão
- tempfile.TemporaryDirectory(): cria diretório temporário
- shutil.move(): move e renomeia arquivos

--------------------------------------------------

⚠️ Observações

- A busca por Anexo1 não diferencia letras maiúsculas e minúsculas
- O script evita sobrescrever arquivos com o mesmo nome
- Suporta múltiplos arquivos Anexo1 no mesmo zip
- Anexo1 meramente ilustrativo



