from datetime import datetime
from pandas import DataFrame
import pandas_datareader.data as web

def get_acorns_stocks_dat(stock_of_interest, start_time, now_time):
    ## get a dataframe for an ACORNS stock of interest w ##
    f_dat = web.DataReader(stock_of_interest, 'google', start_time, now_time)
    return f_dat

if __name__ == '__main__':
    
    now_time = datetime.now()
    
        #Historical data
    start_time = datetime(now_time.year - 20, now_time.month , now_time.day)
    
    
         #ACORNS Portfolio 
    
    acorns_stocks = ['VNQ','SHY','VEA','VWO','LQD','VB','VOO']
    
    for i, stock in enumerate(acorns_stocks):
            stock_df = get_acorns_stock_dat(stock, start_time, now_time)
            stock_df['Name'] = stock
            if i == 0:
                big_df = stock_df
            else:
                big_df = big_df.append(stock_df)
big_df.to_csv('Todaysstock.csv')
