import Module.APIEndpoint as aep
from Module.DB import NewDB

if __name__ == '__main__':

    data = NewDB("AC_Routing.db")
    NewDB.create_tables_if_not_exist(data)
    aep.start(data, False)
