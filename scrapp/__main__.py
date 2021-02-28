import logging
from scrap_titi import scrapp_VR
from sqlconnectors import Mototravel_conn
from bs4 import BeautifulSoup
import requests
import itertools


logging.basicConfig(level=logging.DEBUG,
                    filename="LOG_scrapp.log",
                    filemode="a", #append ou W pour écraser
                    format='%(asctime)s : %(levelname)s : %(message)s')

def main():
    logging.info("\n\n-------------------init __main__.py------------------------ \n")

    try:
        Myconn = Mototravel_conn()
        logging.info("create_db conn success")
    except:
        logging.warning("Failure create_db conn")

    try:
        Myconn.create_tables()
        logging.info("create_tables conn success")
    except:
        logging.warning("Failure create_tables conn")

    try:
        data = scrapp_VR()
        data.find_title()
        data.find_dates()
        data.find_destinations_levels()
        data.create_dict()
        Myconn.insert_tables(data.list_dict)
        logging.info("insert_tables conn success")
    
    except:
        logging.warning("Failure insert_tables conn")


if __name__=='__main__':
    main()
