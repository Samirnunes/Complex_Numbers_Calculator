from complex_number import complex_number as cn

z1 = cn(1,2)
z2 = cn(2,1)

print(f'z1: {z1}')
print(f'z2: {z2}')
cn.print_cis(z1)
cn.print_cis(z2)
print(f'z1_conjugate: {cn.conj(z1)}')
print(f'z2_conjugate: {cn.conj(z2)}')
print(f'z1_module: {cn.mod(z1)}')
print(f'z2_module: {cn.mod(z2)}')
print(f'z1_z2_sum: {cn.csum(z1,z2)}')
print(f'z1_z2_multiplication: {cn.cmult(z1,z2)}')
print(f'z1_z2_division: {cn.cdiv(z1,z2)}')
