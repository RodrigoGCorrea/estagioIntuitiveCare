from parse import *
from tabula import read_pdf
from pdfrw import PdfReader, PdfWriter
import os


def main():
    # Cortei o pdf para conter somente a parte em que queremos tirar os dados para facilitar o processamento
    file = "../Componente Organizacional.pdf"

    pages = PdfReader(file).pages
    crop = (78, 86)

    croppedFile = "../Componente Organizacional Cortado.pdf"
    outdata = PdfWriter(croppedFile)
    for pagenum in range(*crop):
        outdata.addpage(pages[pagenum-1])
    outdata.write()

    # passei o pdf no tabula para gerar as tabelas dentro do python
    tables = read_pdf(croppedFile, pages="all")

    # os quadros 30 e 32 são parecidos, facilitando o processamento
    df30 = ParseDFSimple(tables[0])
    df32 = ParseDFSimple(tables[-1])

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

    df31middle = ParseDFMiddle(tables[2], rowNames)
    print(df31middle)


main()