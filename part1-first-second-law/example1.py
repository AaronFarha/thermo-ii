"""
Heating water at constant volume. (Moran and Shapiro, Example 3.2)
Given: 
- closed, rigid container with 0.5 m^3 water
- water is at SLVM, with x1 = 0.5
- P1 = 1 bar
- P2 = 1.5 bar

Find:
a. temperature, in C, at states 1 and 2
b. mass of vapor, in kg, at states 1 and 2
c. heating continues, determine pressure, in bar, when container as only saturated vapor
d. create a Tv diagram to indicate all states

Assumptions:
- closed system
- rigid container --> V = constant
- states 1, 2, and 3 are equilibrium states
"""
from CoolProp.CoolProp import PropsSI

# Data inputs
Vtot = 0.5  # [m^3]
P1 = 1      # [bar]
P2 = 1.5    # [bar]
x1 = 0.5    # [-]

bar_to_pa = 100000 # conversion from bar to pascal

R = 'Water' # easy to store the name of the fluid as a variable

# Calculate specific volume at State 1 using P1 and x1
# Note: CoolProp doesn't have a function call for specific volume, but density
v_f1 = 1 / PropsSI('D', 'P', P1 * bar_to_pa, 'Q', 0, R)
v_g1 = 1 / PropsSI('D', 'P', P1 * bar_to_pa, 'Q', 1, R)

v1 = v_f1 + x1 * (v_g1 - v_f1)
print(f"\nv1 = {v1:0.4f} [m^3/kg]")

# since mass and volume are fixed, v2 = v1
v2 = v1

v_f2 = 1 / PropsSI('D', 'P', P2 * bar_to_pa, 'Q', 0, R)
v_g2 = 1 / PropsSI('D', 'P', P2 * bar_to_pa, 'Q', 1, R)

print(f"vg2 = {v_g2:0.4f} [m^3/kg]")

# ================= Solution to part a. =================
print("\n================= Solution to part a. =================")
# Since states 1 and 2 are within SLVM, T1 and T2 correspond to saturation temps
T1 = PropsSI('T', 'P', P1 * bar_to_pa, 'Q', 1, R) - 273.15
T2 = PropsSI('T', 'P', P2 * bar_to_pa, 'Q', 1, R) - 273.15

print(f"T1 = {T1:0.4f} [C]")
print(f"T2 = {T2:0.4f} [C]")

# ================= Solution to part b. =================
print("\n================= Solution to part b. =================")
# First find the total mass in the system
m = Vtot / v1 # [m^3] / [m^3/kg] = [kg]
print(f"M = {m:0.4f} [kg]")

# calculate vapor mass using quality
m_g1 = x1 * m
print(f"m_g1 = {m_g1:0.4f} [kg]")

# calculate vapor quality at state 2
x2 = (v2 - v_f2) / (v_g2 - v_f2)
m_g2 = x2 * m
print(f"m_g2 = {m_g2:0.4f} [kg]")

# ================= Solution to part c. =================
print("\n================= Solution to part c. =================")
# State 3 is on the saturated vapor line, so v_g3 = v1 = v2
P3 = PropsSI('P', 'D', 1/v2, 'Q', 1, R) / bar_to_pa
print(f"P3 = {P3:0.4f} [bar]")