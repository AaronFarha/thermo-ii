"""
Tank contains water as a two-phase liquid-vapor mixture at 260 C and quality of 0.7. 
Saturated water is slowly withdrawn through a pressure regulating valve and energy is 
transferred in to maintain constant pressure until tank is filled with saturated vapor. 
(Moran and Shapiro, Example 4.11)

Given: 
- Tank with V = 0.85 m^3
- SLVM mixture at 260 C, quality of 0.7

Find:
determine the amount of heat transfer added in

Assumptions:
- neglect KE, PE
- steady state, steady flow
- control volume is tank
- W = 0 (rigid tank)
- exit state is constant
- initial and final states of the mass within the tank are equilibrium states

"""

from CoolProp.CoolProp import PropsSI

# data input
V = 0.85 # [m^3]
T = 260  # [C]

R = 'Water'

# ================= Solution to problem =================
print("\n================= Solution to problem =================")
x1 = 0.7 # initial quality is given
x2 = 1   # final quality is saturated vapor

# calculate the initial and final internal energy of the system
u1 = PropsSI('U', 'T', T + 273.15, 'Q', x1, R)
u2 = PropsSI('U', 'T', T + 273.15, 'Q', x2, R)

# calculate the exit state enthalpy
he = PropsSI('H', 'T', T + 273.15, 'Q', x2, R)

# calculate the specific volumes at each state
v1 = 1 / PropsSI('D', 'T', T + 273.15, 'Q', x1, R)
v2 = 1 / PropsSI('D', 'T', T + 273.15, 'Q', x2, R)

# determine the initial and final mass in the system
m1 = V / v1
m2 = V / v2

# first law transient energy balance and integrating
Qcv = (m2 * u2 - m1 * u1) - he * (m2 - m1)

print(f"Qcv = {Qcv:0.2f} [J]")