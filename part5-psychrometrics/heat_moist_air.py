"""
Moist air enters a duct at 10 C, 80% relative humidity, and volumetric flow of 150 m^3/min.
Mixture heated in duct and exits at 30 C. System all at 1 bar.
(Moran and Shapiro, Example 12.10)
 
Given: 
- T1 = 10 C
- T2 = 30 C
- Vdot = 150 m^3/min
- P = 1 bar
- f1 = 80%

Find:
a) heat transfer added to air
b) relative humidity, f2, at exit

Assumptions:
- KE = PE = 0
- W = 0
- Ideal gas mixture
- Dalton's Law
- Steady state, steady flow
- Open system
"""

from CoolProp.CoolProp import PropsSI
from CoolProp.HumidAirProp import HAPropsSI

# data input
Vdot = 150   # [m^3/min]

T1 = 10  # [C]
T2 = 30  # [C]

P = 1e5    # [bar -> Pa]

f1 = 0.8 # [% RH]

# ================= Solution to part a) =================
print("\n================= Solution to part a) =================")
# to get mass balance, we need the humidity ratios, since no moisture added -> w1 = w2 = w
w = HAPropsSI('HumRat','T',T1 + 273.15,'P',P,'R',f1)
print(f"w = {w:0.2f} [kg-vap / kg-dry air]")

# to get the air flow rate on a mass basis, we need the specific volume of dry air, which is 1 / density
va1 = 1 / PropsSI('D','T',T1 + 273.15,'P',P,'Air')
ma_dot = Vdot / va1 # [kg/min]
print(f"ma_dot = {ma_dot:0.2f} [kg / min]")

# 1st law energy balance --> Q_heat = ma_dot * (h2 - h1)
# to get the mixture enthalpies, we first get the enthalpies of the dry air and water vapor at each state point

# saturated pressure of water vapor at each state
Pg1 = PropsSI('P','T',T1 + 273.15,'Q',1,'Water')
Pg2 = PropsSI('P','T',T2 + 273.15,'Q',1,'Water')

# Pv remains constant since the humidity ratio stays the same
Pv = f1 * Pg1

# dry air enthalpies, need to use air partial pressure!!
ha1 = PropsSI('H','T',T1 + 273.15,'P',P - Pv,'Air') # [J/kg]
ha2 = PropsSI('H','T',T2 + 273.15,'P',P - Pv,'Air') # [J/kg]

# water vapor enthalpies, need to use water vapor partial pressure!!
hv1 = PropsSI('H','T',T1 + 273.15,'P',Pv,'Water') # [J/kg]
hv2 = PropsSI('H','T',T2 + 273.15,'P',Pv,'Water') # [J/kg]

# solving for Q_heat after energy balance
Q_heat = ma_dot * ((ha2 - ha1) + w * (hv2 - hv1)) / 1000 # [kJ/min]
print(f"Q_heat = {Q_heat:0.2f} [kJ / min]")

# ================= Solution to part b) =================
print("\n================= Solution to part b) =================")
# to calculate the relative humidity at the exit we simply need 
# the saturated water vapor pressure at state 2 since Pv is constant in this example
f2 = Pv / Pg2
print(f"f2 = {f2*100:0.2f} [%]")