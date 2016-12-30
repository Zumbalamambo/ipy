import CoolProp.CoolProp as CP
fluid = 'Water'

d = CP.PropsSI('D','P', 1e5, 'T', 273.15, fluid)

print d
