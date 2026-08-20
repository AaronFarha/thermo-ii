"""
Power cycle operating between two thermal reservoirs. (Moran and Shapiro, Example 5.1)
Given: 
- thermal reservoir operates between Th = 2000 K and Tc = 400 K
- Qh is obtained from Th
- Qc is rejected to Tc

Find:
determine if the cycle operates reversibly, irreversibly, or is impossible for the following scenarios
a. Qh = 1000 kJ, eta = 60%
b. Qh = 1000 kJ, Wcycle = 850 kJ
c. Qh = 1000 kJ, Qc = 200 kJ

"""

# data input
Th = 2000 # [K]
Tc = 400  # [K]

Qh = 1000 # [kJ]

# maximum thermal efficiency
eta_max = (Th - Tc) / Th

# ================= Solution to part a. =================
print("\n================= Solution to part a. =================")
eta = 0.6

if eta < eta_max:
    print("The system operates irreversibly")
elif eta == eta_max:
    print("The system operates reversibly")
elif eta > eta_max:
    print("The system is impossible")
    
# ================= Solution to part b. =================
print("\n================= Solution to part b. =================")
Wcycle = 850  # [kJ]

eta = Wcycle / Qh

if eta < eta_max:
    print("The system operates irreversibly")
elif eta == eta_max:
    print("The system operates reversibly")
elif eta > eta_max:
    print("The system is impossible")
    
# ================= Solution to part c. =================
print("\n================= Solution to part c. =================")
# applying an energy balance
Qc = 200  # [kJ]
Wcycle = Qh - Qc

eta = Wcycle / Qh

if eta < eta_max:
    print("The system operates irreversibly")
elif eta == eta_max:
    print("The system operates reversibly")
elif eta > eta_max:
    print("The system is impossible")