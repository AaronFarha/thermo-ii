"""
Heating ammonia at constant pressure. (Moran and Shapiro, Example 3.1)
Given: 
- vertical piston-cylinder with 0.45 kg of ammonia
- ammonia initially at saturated vapor, placed on hot plate
- heating occurs and ammonia expands at constant pressure until 25 C
- P = 1.37 bar

Find:
a. volume occupied by the ammonia at each end state, in m^3
b. the work for the process
c. show initial and final states on Tv and Pv diagrams (do yourself)

Assumptions:
- closed system
- process occurs at constant pressure
- states 1 and 2 are equilibrium states
- piston is the only work mode
"""

from CoolProp.CoolProp import PropsSI

# Data inputs
P = 1.37    # [bar]
x1 = 1      # [-]
T2 = 25     # [C]
m = 0.045    # [kg]

bar_to_pa = 100000 # conversion from bar to pascal

R = 'ammonia' # easy to store the name of the fluid as a variable

# ================= Solution to part a. =================
print("\n================= Solution to part a. =================")
# State 1 starts at saturated vapor. State 2 is in super heated vapor
# Note! CoolProp doesn't have an explicit calculation for specific volume
v1 = 1 / PropsSI('D', 'P', P * bar_to_pa, 'Q', x1, R)
v2 = 1 / PropsSI('D', 'P', P * bar_to_pa, 'T', T2 + 273.15, R)

V1 = m * v1
V2 = m * v2

print(f"V1 = {V1:0.4f} [m^3]")
print(f"V2 = {V2:0.4f} [m^3]")

# ================= Solution to part a. =================
print("\n================= Solution to part a. =================")
# Work is simply evaluated as the integral of pdV = p(V2 - V1)
P = P * bar_to_pa
W = P * (V2 - V1)

print(f"W = {W:0.2f} [J]")