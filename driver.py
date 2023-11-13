import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, URL, exc

from vnstock import *
from datetime import datetime, timedelta, tzinfo

import logging
import time
import os

def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Log to console
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Also log to a file
    file_handler = logging.FileHandler("cpy-errors.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

def create_connection(url_object, attempts=3, delay=2):
    attempt = 1
    logger = create_logger()
    while attempt < attempts + 1:
        try:
            return create_engine(url_object)
        except exc.SQLAlchemyError as err:
            if (attempts is attempt):

                logger.info("Failed to connect, exiting without a connection: %s", err)
                return None
            
            logger.info(
                "Connection failed: %s. Retrying (%d/%d)...",
                err,
                attempt,
                attempts-1,
            )
            time.sleep(delay ** attempt)
            attempt += 1
    return None

def insertion():
    url_object =  URL.create(
        'mysql+mysqldb',
        username='thien',
        password='thien',
        host='127.0.0.1',
        database='thien'
    )
    
    engine = create_connection(url_object, attempts=3)
    
    stock_list = ['TCB', 'HPG', 'SSI', 'VIC', 'VHM']
    
    for stock in stock_list:
        last_row = pd.read_sql(f'SELECT * FROM {stock} ORDER BY time DESC LIMIT 1', engine)
        df = stock_historical_data(symbol=stock, start_date=str(datetime.today()-timedelta(days=3))[:10], end_date=str(datetime.today())[:10], resolution='1', type='stock')
        
        if last_row['time'].size > 0:
            df['time'] = df['time'].apply(lambda x: x.replace(tzinfo=None))
            last_row = last_row.iloc[0].to_list()
            latest_idx = df.loc[df['time'] == last_row[0]].index
            latest_idx = pd.to_numeric(latest_idx)
            new_rows = df.iloc[latest_idx[0]+1:]
            
            new_rows.to_sql(stock, con=engine, if_exists='append', method='multi',index=False)
        else:
            df.to_sql(stock, con=engine, if_exists='append', method='multi',index=False)


if __name__ == '__main__':
    insertion()
