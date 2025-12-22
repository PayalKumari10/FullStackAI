import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.49999999999

print(f"Ideal temperature {ideal_temp}")
print(f"Current temperature {current_temp}")
print(f"Temperature difference {ideal_temp - current_temp}")
print(sys.float_info)