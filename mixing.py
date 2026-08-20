import numpy as np
from CoolProp.CoolProp import PropsSI

Tn2 = 260
To2 = 300

Nn2 = 0.4
No2 = 0.1

Pn2 = 200
Po2 = 100

Cvn2 = PropsSI('CVMOLAR', 'T', Tn2, 'P', Pn2 * 1000, 'N2')
Cvo2 = PropsSI('CVMOLAR', 'T', Tn2, 'P', Pn2 * 1000, 'O2')

num = Nn2 * Cvn2 * Tn2 + No2 * Cvo2 * To2
den = Nn2 * Cvn2 + No2 * Cvo2

T2 = num / den
print(f"T2 = {T2:.3f} K")

R = 8.314
Vn2 = (Nn2 * R * Tn2) / Pn2
Vo2 = (No2 * R * To2) / Po2

V = Vn2 + Vo2

P2 = ((Nn2 + No2) * R * T2) / V
print(f"P2 = {P2:.3f} kPa")

Cpn2 = Cvn2 + R
Cpo2 = Cvo2 + R

yn2 = Nn2 / (Nn2 + No2)
yo2 = No2 / (Nn2 + No2)

dSn2 = Nn2 * (Cpn2 * np.log(T2 / Tn2) - R * np.log((yn2 * P2)/Pn2))
dSo2 = No2 * (Cpo2 * np.log(T2 / To2) - R * np.log((yo2 * P2)/Po2))

sigma = dSn2 + dSo2
print(f"sigma = {sigma:.3f} kJ/K")