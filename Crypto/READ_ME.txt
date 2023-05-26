
HELP MENU: 

| -a    | amount   | input: price start, price end, shares ]   
| -ia   | amount   | input: price start, price end, shares      
| -ic   | cost     | input: price, shares             

RUN -a: 
python Crypto.py -a 1.51 2.36 100

RESULTS:
---------------------------------
total cost: $151.00
---------------------------------
percent: +56.29%
profit: +$85.00
---------------------------------


RUN -ia:
python Crypto.py -ia 1.51 2.36 100     

RESULTS 
---------------------------------
price start: $2.1
price end: $4.0
shares: 100
---------------------------------
total cost: $210.00
---------------------------------
percent: +90.48%
profit: +$190.00
---------------------------------

RUN -ic:
python Crypto.py -ic 1.51 2.36 100

RESULTS 
---------------------------------
price: $2.32
shares: 100
total cost: $232.00
---------------------------------

