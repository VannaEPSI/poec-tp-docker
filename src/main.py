import sys
from calc import apply_percent

price = float(sys.argv[1])
percent = float(sys.argv[2])

tva_included_price = apply_percent(price, percent)
print (tva_included_price)



