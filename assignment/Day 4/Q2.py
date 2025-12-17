
km_to_m = lambda distance: distance * 1000
m_to_cm = lambda distance: distance * 100
cm_to_mm = lambda distance: distance * 10
ft_to_in = lambda distance: distance * 12
in_to_cm = lambda distance: distance * 2.54
km_to_ft = lambda distance: distance * 3280.84  

def distance_converter(distance, conversion_type, conversion_func):
    result = conversion_func(distance)
    from_unit, to_unit = conversion_type.split(' to ')
    print(f"{distance} {from_unit} is {result} {to_unit}")

distance_km = float(input("Enter distance in kilometers: "))

distance_converter(distance_km, "km to m", km_to_m)
distance_m = km_to_m(distance_km)
distance_converter(distance_m, "m to cm", m_to_cm)
distance_cm = m_to_cm(distance_m)
distance_converter(distance_cm, "cm to mm", cm_to_mm)
distance_ft = km_to_ft(distance_km)
distance_converter(distance_ft, "ft to in", ft_to_in)
distance_in = ft_to_in(distance_ft)
distance_converter(distance_in, "in to cm", in_to_cm)
