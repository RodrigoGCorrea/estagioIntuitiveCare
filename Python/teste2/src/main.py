# encoding: utf-8
from parse import *
from tabula import read_pdf
from pdfrw import PdfReader, PdfWriter
from pandas import to_numeric, concat
from zipfile import ZipFile, ZIP_DEFLATED
import os


def main():
    # Cortei o pdf para conter somente a parte em que queremos tirar os dados para facilitar o processamento
    file = "../Componente Organizacional.pdf"
    listFiles = ["Quadro 30", "Quadro 31", "Quadro 32"]
    dfList = ["", "", ""]

    pages = PdfReader(file).pages
    crop = (79, 86)

    croppedFile = "../Componente Organizacional Cortado.pdf"
    outdata = PdfWriter(croppedFile)
    for pagenum in range(*crop):
        outdata.addpage(pages[pagenum-1])
    outdata.write()

    # passei o pdf no tabula para gerar as tabelas dentro do python
    tables = read_pdf(croppedFile, pages="all")
    print("PDF foi cortado")

    # organizei o começo do quadro 31
    df31 = tables[1]
    rowNames = list(df31.iloc[0])
    df31.rename(
        columns={
            'Unnamed: 0':rowNames[0],
            "Tabela de Categoria do Padrão TISS" : rowNames[1]
        }, 
        inplace=True 
    )
    df31 = df31.drop([0])

    # arrumei o quadro 31, que veio cortado devido a estar em mais páginas
    for i in range(2, len(tables)-1):
        df31middle = ParseDFMiddle(tables[i], rowNames)
        df31 = concat([df31, df31middle], ignore_index=True)
    
    df31[df31.columns[0]] = to_numeric(df31[df31.columns[0]])
    dfList[1] = df31.sort_values(df31.columns[0])
    print(listFiles[1] + " construído")

    # os quadros 30 e 32 são parecidos, facilitando o processamento
    dfList[0] = ParseDFSimple(tables[0])
    print(listFiles[0]+" construído")
    dfList[2] = ParseDFSimple(tables[-1])
    print(listFiles[2] + " construído")

    # guardei os arquivos CSV
    for i in range(3):
        dfList[i].to_csv(listFiles[i] + ".csv", index=False, encoding='utf-8')
    print("CSVs construídos")

    # colocando os arquivos em um zip
    with ZipFile('Teste_Intuitive_Care_Rodrigo_Correa.zip', 'w') as zipF:
        for file in listFiles:
            zipF.write(file+".csv", compress_type=ZIP_DEFLATED)
            os.remove(file + ".csv")
    print("Zip construido em "+os.getcwd())
    
main()