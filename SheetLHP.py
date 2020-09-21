from datetime import date
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

import time

def update_google_sheet(name):
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("/home/manhhung060299/CoTAI/face_recognition/FaceRecLHP/ConnectGgSheet/Sheetlhp.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("LHP").sheet1  # Open the spreadhseet
    cellr = sheet.find(name)
    school_day = str(date.today())
    cellc = sheet.find(school_day)
    R = cellr.row
    C = cellc.col

    if sheet.cell(R,C).value == '':
        # print("***")
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        sheet.update_cell(R,C,current_time)
    else:
        print("Đã điểm danh rồi")
