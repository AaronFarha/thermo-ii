"""
R-410a is used in an vapor injection heat pump cycle with intermediate flash tank. Cold and hot reservoirs are at -15 C and 20 C respectively.
Given: 
- vapor compression cycle with R-410a
- hot and cold reservoirs specified

Find:
a. compressor power, in kW
b. refrigeration capacity, in kW and in tons
c. coefficient of performance
d. Carnot COP
e. energy balance on the system

Assumptions:
- Each component is a CV at steady state
- all processes of working fluid internally reversible, except expansion valve
- compressor and expansion valve operate adiabatically
- KE = PE = 0
- sat. vapor enters compressor, sat. liq. exits condenser
"""

import numpy as np
from CoolProp.CoolProp import PropsSI

# Input Data
R = 'R410a'

Th = 20 # [C]
Tc = -15 # [C]

Tcond = Th + 10 + 273 # [K], assume Tevap = Th + 10 C
Tevap = Tc - 10 + 273  # [K], assume Tcond = Tc - 10 C

Tsh = 5 # [K]
Tsc = 5 # [K]

# Pressures
Pevap = PropsSI('P', 'T', Tevap, 'Q', 1, R)
Pcond = PropsSI('P', 'T', Tcond, 'Q', 1, R)
Pint = np.sqrt(Pevap * Pcond)

print("Pcond: ", Pcond / 1000)
print("Pevap: ", Pevap / 1000)
print("Pint: ", Pint / 1000)

# State 1
P1 = Pevap
h1 = PropsSI('H', 'T', Tevap + Tsh, 'P', P1, R)
s1 = PropsSI('S', 'T', Tevap + Tsh, 'P', P1, R)

# State 2
P2 = Pcond
