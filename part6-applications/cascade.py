"""
R-290 is used in an ideal vapor compression cycle. Cold and hot reservoirs are at -20 C and 21 C respectively.
Given: 
- cascade cycle with R-290
- hot and cold reservoirs specified
- mass flow rate is given

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


from CoolProp.CoolProp import PropsSI

# Input Data
R = 'R134a'
Th = 26 + 273 # [C]
Tc = 0 + 273  # [C]
mdot = 0.08      # [kg/s]

# State 1
P1 = PropsSI('P', 'T', Tc, 'Q', 1, R)
h1 = PropsSI('H', 'T', Tc, 'Q', 1, R)
s1 = PropsSI('S', 'T', Tc, 'Q', 1, R)

# State 2
P2 = PropsSI('P', 'T', Th, 'Q', 1, R)
s2 = s1
h2 = PropsSI('H', 'T', Th, 'S', s2, R)

# State 3
P3 = P2
h3 = PropsSI('H', 'P', P3, 'Q', 0, R)
s3 = PropsSI('S', 'P', P3, 'H', h3, R)

# State 4
P4 = P1
h4 = h3
s4 = PropsSI('S', 'P', P4, 'H', h4, R)

# solution to part a.
Wcomp = mdot * (h2 - h1) / 1000
print(f"Wcomp = {Wcomp:0.2f} [kW]")

# solution to part b.
Qevap = mdot * (h1 - h4) / 1000
print(f"Qevap = {Qevap:0.2f} [kW]")
print(f"Qevap = {Qevap/3.517:0.2f} [tons]")

# solution to part c.
COP = Qevap / Wcomp
print(f"COP = {COP:0.1f}")

# solution to part d.
Carnot = Tc / (Th - Tc)
print(f"Carnot COP = {Carnot:0.1f}")

# solution to part e.
Qcond = mdot * (h2 - h3) / 1000
E_bal = Qcond - Qevap - Wcomp

print(f"Qcond = {Qcond:0.2f} [kW]")
print(f"Ebal = {E_bal:0.3f} [kW]")