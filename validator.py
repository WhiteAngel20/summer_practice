from from_csv_to_json import CSV_JSON
from uuid import UUID

global_data = []
CELL_FAULT = "--------------------cell fault -->\tcolname: {} row: {} [{}]"

def is_valid_uuid(uuid_to_test, version=4):
    """
    Check if uuid_to_test is a valid UUID.

     Parameters
    ----------
    uuid_to_test : str
    version : {1, 2, 3, 4}

     Returns
    -------
    `True` if uuid_to_test is a valid UUID, otherwise `False`.

     Examples
    --------
    >>> is_valid_uuid('c9bf9e57-1685-4c89-bafb-ff5af830be8a')
    True
    >>> is_valid_uuid('c9bf9e58')
    False
    """

    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test

def checking_ID():
    ID = 0
    for i in range(1, len(global_data) - 1):
        if is_valid_uuid(global_data[i][ID]):
            pass
        else:
            print("error uuid".upper())
            print('string is not uuid4 format')
            print(CELL_FAULT.format(global_data[0][ID], i+2, global_data[i][ID]))
            print()


def checking_model():
    MODEL = 1
    for i in range(1, len(global_data) - 1):
        if 'BMW' in global_data[i][MODEL].upper():
            print("error include BMW".upper())
            print("this model cannot be sold")
            print(CELL_FAULT.format(global_data[0][MODEL], i+2, global_data[i][MODEL]))
            print()


def checking_price():
    BOUGHT, SOLD = 2, 4
    for i in range(1, len(global_data) - 1):
        global_data[i][BOUGHT], global_data[i][SOLD] = int(global_data[i][BOUGHT]), int(global_data[i][SOLD])

        if global_data[i][BOUGHT] <= 0 or global_data[i][SOLD] <= 0:
            print("error price".upper())
            print("price to cars must be positive")
            print(CELL_FAULT.format(global_data[0][BOUGHT], i + 2, global_data[i][SOLD]))
            print()

        if global_data[i][BOUGHT] > global_data[i][SOLD]:
            print("error selling".upper())
            print("sold price less than purchase")
            print(CELL_FAULT.format(global_data[0][BOUGHT], i + 2, global_data[i][SOLD]))
            print()

def checking_volume():
    VOLUME = 3
    for i in range(1, len(global_data) - 1):
        global_data[i][VOLUME] = int(global_data[i][VOLUME])

        if global_data[i][VOLUME] <= 0 or global_data[i][VOLUME] == 1900:
            print("error volume".upper())
            print("unvailable volume")
            print(CELL_FAULT.format(global_data[0][VOLUME], i + 2, global_data[i][VOLUME]))
            print()

def checking_mileage():
    MILEAGE = 5
    for i in range(1, len(global_data) - 1):
        global_data[i][MILEAGE] = int(global_data[i][MILEAGE])

        if global_data[i][MILEAGE] <= 0 or global_data[i][MILEAGE] >= 250000:
            print("error mileage".upper())
            print("car with mileage more 250000, not sold")
            print(CELL_FAULT.format(global_data[0][MILEAGE], i + 2, global_data[i][MILEAGE]))
            print()


def c():
    fl = CSV_JSON('cars.csv')
    fl.start()

    global global_data
    global_data = fl.data_global        #return[[],[], ..., []]

    checking_ID()
    checking_model()
    checking_price()
    checking_volume()
    checking_mileage()

c()



























