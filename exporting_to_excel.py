import openpyxl
import pandas as pd

def excel_maker():
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Films"
    sheet["A1"] = "Title"
    sheet["B1"] = "Orig. title"
    sheet["C1"] = "Year"
    sheet["D1"] = "Rate"
    sheet["E1"] = "Fav"
    sheet["F1"] = "Date added"
    workbook.save(filename="movie_list.xlsx")

def excel_saver(movies):
    wb = openpyxl.load_workbook('movie_list.xlsx')
    sheet = wb.active
    sheet.append(movies)
    wb.save(filename="movie_list.xlsx")


def excel_saver1(movies):
    df = pd.DataFrame(data = movies)

    df.to_excel('movie_list1.xlsx', index=False)