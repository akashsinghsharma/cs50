def einstein_eqn(m):
    c = 300000000 #m/s
    c2 = pow(c,2)
    e = m*c2
    return e

user_mass = int(input('please enter mass in kg'))
energy = einstein_eqn(user_mass)
print(energy)