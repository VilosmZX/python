#################
# Author: Joshua#
# Python: 3.9.2 #
# Module:       #
# - Requests    #
# - numpy       #
# - pandas      #
# - matlotlib   #
#################

import numpy as np 
import pandas as pd 

class data:
  
  def get_csv(){
    df = pd.read_csv('yourdataset.csv') # Example: /root/mydataset/name.csv.
    print(df)
  }
  
if __name__ == '__main__':
  data.get_csv()