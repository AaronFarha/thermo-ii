"""
Steam is working fluid in an ideal Rankine cycle. Sat. vapor enters turbine at 8.0 MPa, sat. liq. exits condenser at 0.008 MPa.
Net power of cycle is 100 MW.
Given: 
- ideal rankine cycle with steam
- boiler and condenser pressures specified
- net power is given

Find:
a. thermal efficiency
b. back work ratio
c. mass flow rate of steam in cycle, kg/h
d. rate of heat transfer in boiler
e. rate of heat transfer in condenser

Assumptions:
- Each component is a CV at steady state
- all processes of working fluid internally reversible
- turbine and pump operate adiabatically
- KE = PE = 0
- sat. vapor enters turbine, sat. liq. exits condenser
"""
from CoolProp.CoolProp import PropsSI

# Input Data
R = 'Water'
T_cool_1 = 15 # [C]
T_cool_2 = 35 # [C]
Wcycle = 100 * 1000 # [kW]

# State 1
P1 = 8.0 * 1000 # [kPa]
h1 = PropsSI('H', 'P', P1 * 1000, 'Q', 1, R) / 1000 # [kJ/kg]
s1 = PropsSI('S', 'P', P1 * 1000, 'Q', 1, R) / 1000 # [kJ/kg-K]

# State 2 
P2 = 0.008 * 1000 # [kPa]
sf2 = PropsSI('S', 'P', P2 * 1000, 'Q', 0, R) / 1000
sg2 = PropsSI('S', 'P', P2 * 1000, 'Q', 1, R) / 1000
hf2 = PropsSI('H', 'P', P2 * 1000, 'Q', 0, R) / 1000
hg2 = PropsSI('H', 'P', P2 * 1000, 'Q', 1, R) / 1000

s2 = s1
x2 = (s2 - sf2) / (sg2 - sf2)
h2 = hf2 + x2*(hg2 - hf2)

# State 3
P3 = P2
h3 = PropsSI('H', 'P', P3 * 1000, 'Q', 0, R) / 1000
s3 = sf2
v3 = 1 / PropsSI('D', 'P', P3 * 1000, 'Q', 0, R)

# State 4
P4 = P1
s4 = s3
h4 = h3 + v3 * (P4 - P3)

# Solution to part a.
wnet = (h1 - h2) - (h4 - h3)
qin = h1 - h4
eta = wnet / qin

print(f"specific work of cycle: {wnet:0.2f} [kJ/kg]")
print(f"specific heat into cycle: {qin:0.2f} [kJ/kg]")
print(f"cycle efficiency: {eta*100:0.2f}%")

# solution to part b.
bwr = (h4 - h3) / (h1 - h2)

print(f"back work ratio: {bwr*100:0.2f}%")

# solution to part c.
mdot = Wcycle / wnet # [kg/s]
print(f"mass flow rate: {mdot:0.2f} [kg/s]")

# solution to part d.
Qin = mdot * qin
print(f"Qin = {Qin / 1000:0.2f} [MW]")

# solution to part e. 
Qout = mdot * (h2 - h3)
print(f"Qout = {Qout / 1000:0.2f} [MW]")