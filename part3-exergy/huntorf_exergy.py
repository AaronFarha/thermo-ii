"""
Huntorf compressed air energy storage exergy analysis. 
Given: 
- cavern of pressurized air
- V = 300000 m^3
- P1 = 55 bar
- T1 = 50 C = 323 K

- P0 = 1 bar
- T0 = 300 K

Find:
total exergy of the air

Assumptions:
- KE = PE = 0
- Air is ideal gas
- closed system
"""
import numpy as np

# data input
Vtot = 300000       # [m^3]
P1 = 55             # [bar]
P0 = 1              # [bar]
T1 = 50 + 273.15    # [C -> K]
T0 = 300            # [K]

# first calculate the total mass of air in the cavern
R = 287             # [J/kg-K]
bar_to_pa = 100000  # conversion from bar to pascal
P1 = P1 * bar_to_pa
P0 = P0 * bar_to_pa

mtot = (P1 * Vtot) / (R * T1)
print("\n================= Total Mass =================")
print(f"M = {mtot:0.3f} [kg]")

# Calculate the internal energy change compared to dead state
u1 = 232.02         # [kJ/kg], from tables
u0 = 214.07         # [kJ/kg], from tables
dU = mtot * (u1 - u0)
print("\n================= Internal Energy Difference =================")
print(f"dU = {dU:0.3f} [kJ/kg]")

# Calculate the change in entropy compared to dead state
s_1_0 = 1.782       # [kJ/kg-K], from tables
s_0_0 = 1.702       # [kJ/kg-K], from tables

R_kJ = R / 1000
dS = mtot * (s_1_0 - s_0_0 - R_kJ * np.log(P1/P0))
print("\n================= Entropy Difference =================")
print(f"dS = {dS:0.3f} [kJ/K]")

# Calculate the change in flow work compared to dead state
V0 = (mtot * R * 300) / P0
dW = (P0 / 1000) * (Vtot - V0)

print("\n================= Volume at Dead State =================")
print(f"V0 = {V0:0.3f} [m^3]")

print("\n================= Available Work =================")
print(f"dW = {dW:0.3f} [kJ/kg]")

# Calculate total exergy (availability)
E = dU + dW - T0 * dS

print("\n================= Total Exergy =================")
print(f"E = {E:0.3f} [kJ]")