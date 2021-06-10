# Função pode ser usada para os quadros 30 e 32 pois são menores e menos complexos
def ParseDFSimple(df):
    newdf = df
    rowNames = df.iloc[0,0].split(" ", 1)
    newdf = df.drop([0])
    newdf[rowNames] = newdf[newdf.columns[0]].str.split(" ", 1, expand=True)
    df = df.drop(df.columns[0], axis=1)
    return newdf

def ParseDFMiddle(df, rowNames):
    newdf = df
    firstLine = list(newdf.columns)
    newdf.loc[-1] = firstLine
    newdf = newdf.rename(
        columns={
            firstLine[0]:rowNames[0],
            firstLine[1]:rowNames[1]
        }
    )
    return newdf
