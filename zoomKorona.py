import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import webbrowser
import time

scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

client = gspread.authorize(creds)

flag = 0

while(1):

    if(flag):
        break

    time.sleep(60)

    # Returns a datetime object containing the local date and time
    dateTimeObj = datetime.now()

    cur_day = dateTimeObj.day
    cur_month = dateTimeObj.month
    cur_hour = dateTimeObj.hour
    cur_min = dateTimeObj.minute

    cur_timeVal = int(str(cur_hour)+str(cur_min))


    sheet = client.open('Zoom-Korona').sheet1
    rows = sheet.row_count

    print("cur_time ", cur_timeVal)


    for i in range(2,rows): #considering first row is the title

        if(sheet.cell(i,1).value==""):
            break

        #print("row: ", i)

        #get time and date
        record_time = sheet.cell(i, 1).value
        record_date = sheet.cell(i, 2).value

        #covert string into datetime
        record_time = datetime.strptime(record_time, '%H:%M:%S')
        record_date = datetime.strptime(record_date, '%d/%m/%Y')

        rec_hour = record_time.hour
        rec_min = record_time.minute

        rec_timeVal = int(str(rec_hour)+str(rec_min))

        if(int(cur_day)<int(record_date.day)):
            continue
        if(int(cur_month)<int(record_date.month)):
            continue

        #print("rec_time ", rec_timeVal)


        if(cur_timeVal>rec_timeVal-5 and cur_timeVal<rec_timeVal+5):
            zoom_url = sheet.cell(i,3).value
            webbrowser.open_new_tab(zoom_url)
            flag = 1
            break   
