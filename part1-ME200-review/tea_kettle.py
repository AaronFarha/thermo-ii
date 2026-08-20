"""
Heating water at constant pressure. 
Given: 
- open container with 0.001 m^3 water (1 liter)
- water is initially at 15 C
- P1 = 1 atm = 101.325 kPa

Find:
a. total energy to heat water to boiling point
b. how long to heat the water with 1.5 kW tea kettle to boiling point
c. how long until water fully vapor

Assumptions:
- neglect heat loss to surroundings
- W = Q
- KE = PE = 0
- P = 1 atm at sea level
"""
from CoolProp.CoolProp import PropsSI

# data input
Vtot = 0.001        # [m^3]
P = 101.325         # [kPa]
T1 = 15 + 273.15    # [C]
T2 = 100 + 273.15   # [C]
Q = 1.5             # [kW]
R = 'Water'

rho1 = PropsSI('D', 'P', P * 1000, 'T', T1, R) # [kg/m^3]
m = Vtot * rho1

cp = PropsSI('C', 'P', P * 1000, 'T', T1, R) / 1000 # [kJ/kg-K]

# ================= Solution to part a. =================
print("\n================= Solution to part a. =================")
dU = m * cp * (T2 - T1)
print(f"dU = {dU:0.4f} [kJ]")

# ================= Solution to part b. =================
print("\n================= Solution to part b. =================")
dt = dU / Q
print(f"dt = {dt:0.1f} [s]")
print(f"dt = {dt/60:0.1f} [min]")

# ================= Solution to part c. =================
print("\n================= Solution to part c. =================")
h2 = PropsSI('H', 'P', P * 1000, 'Q', 0, R) / 1000 # [kJ/kg]
h3 = PropsSI('H', 'P', P * 1000, 'Q', 1, R) / 1000 # [kJ/kg]

dE = m * (h3 - h2) # [kJ]
dt = dE / Q

print(f"dE = {dE:0.4f} [kJ]")
print(f"dt = {dt:0.1f} [s]")
print(f"dt = {dt/60:0.1f} [min]")