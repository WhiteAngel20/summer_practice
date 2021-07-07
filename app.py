from from_csv_to_json import CSV_JSON

def app_run():
    filename = 'Sample-Spreadsheet-100-rows.csv'
    c = CSV_JSON(filename)
    c.start()


app_run()



