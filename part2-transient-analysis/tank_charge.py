"""
Steam at a pressure of 15 bar and a temperature of 320 C is contained in a large vessel.
A turbine and initially evacuated tank of 0.6 m^3 are connected with a valve. When 
emergency power is needed, the valve is opened until pressure reaches 15 bar. The final
temperature in the tank is 400 C.   
(Moran and Shapiro, Example 4.12)

Given: 
- Tank with V = 0.6 m^3, initially evacuated
- Steam at 15 bar, 320 C enters

Find:
determine the amount of work generated

Assumptions:
- neglect KE, PE
- steady state, steady flow
- control volume is tank and turbine
- Q = 0 (adiabatic tank)
- entering state is constant
- initial and final states of the mass within the tank are equilibrium states
- mass stored within the turbine and interconnecting pipes is negligible

"""

from CoolProp.CoolProp import PropsSI

# data input
V = 0.6   # [m^3]
T1 = 320  # [C]
T2 = 400  # [C]
P = 15    # [bar]

R = 'Water'

bar_to_pa = 100000 # conversion from bar to pascal

# ================= Solution to problem =================
print("\n================= Solution to problem =================")
# calculate the initial and final internal energy of the system
u1 = PropsSI('U', 'T', T1 + 273.15, 'P', P * bar_to_pa, R)
u2 = PropsSI('U', 'T', T2 + 273.15, 'P', P * bar_to_pa, R)

# calculate the exit state enthalpy
hi = PropsSI('H', 'T', T1 + 273.15, 'P', P * bar_to_pa, R)

# calculate the specific volumes at each state
v1 = 1 / PropsSI('D', 'T', T1 + 273.15, 'P', P * bar_to_pa, R)
v2 = 1 / PropsSI('D', 'T', T2 + 273.15, 'P', P * bar_to_pa, R)

# determine the initial and final mass in the system
m1 = 0
m2 = V / v2

# first law transient energy balance and integrating
Wcv = hi * (m2 - m1) - (m2 * u2 - m1 * u1)

print(f"Wcv = {Wcv:0.2f} [J]")