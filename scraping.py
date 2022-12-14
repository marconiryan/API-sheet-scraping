import gspread
import pandas as pd


def getData(shname: str, worksheetname: str):
    sa = gspread.service_account(filename='.env/keys.json')  # Chaves
    sh = sa.open(shname)

    wks = sh.worksheet(worksheetname)  # Nome da folha da planilha
    dataframe = pd.DataFrame(wks.get_all_records())
    # -----------------------------------------
    data: dict = {}
    contador: int = 0
    for valor in dataframe.values:
        temp: dict = {}
        for index_column in range(len(dataframe.columns)):
            temp[dataframe.columns[index_column]] = valor[index_column]
        data[contador] = temp
        contador += 1

    return data
