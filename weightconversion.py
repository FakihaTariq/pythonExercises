weight = input('Weight: ')
weight_type = input('(L)bs or (K)g: ')
conv_weight = 0
if weight_type == 'L' or weight_type == 'l':
    conv_weight = float(weight)*.45
else:
    conv_weight = float(weight)/.45
print(f'You are {conv_weight} pounds')
