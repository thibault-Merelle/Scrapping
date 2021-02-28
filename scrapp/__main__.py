import logging
from scrapp import scrapp_VR
from sqlconnectors import mototravel_conn


logging.basicConfig(level=logging.DEBUG,
                    filename="LOG_scrapp.log",
                    filemode="a", #append ou W pour écraser
                    format='%(asctime)s : %(levelname)s : %(message)s')

def main():
    logging.info("init __main__.py")

    try:
        MyVR = scrapp_VR()
        MyVR.find_title()
        logging.info("request title success")
    
    except:
        logging.warning("Failure title request")


    try:
        MyVR = scrapp_VR()
        MyVR.find_dates()
        logging.info("request dates success")
    
    except:
        logging.warning("Failure dates request")

    try:
        MyVR = scrapp_VR()
        MyVR.explorefind_destinations_levels()
        logging.info("request destinations_levels success")
    
    except:
        logging.warning("Failure destinations_levels request")



    try:
        MyDB = mototravel_conn()
        MyDB.create_tables()
        logging.info("create_tables success")
    
    except:
        logging.warning("Failure create_tables")


    try:
        MyDB = mototravel_conn()
        MyDB.insert_tables()
        logging.info("insert_tables success")
    
    except:
        logging.warning("Failure insert_tables")




if __name__=='__main__':
    main()