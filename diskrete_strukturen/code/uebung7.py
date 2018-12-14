def ggT(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return ggT(b, r)

def backwards(a, b, d):
    for la in range(0, b//d):
        mu, r = divmod(d - la * a, b)
        if r == 0:
            return la, mu



print('ggT(a, b) = d = lambda * a + mu * b')
print('a = q * b + r')
print('ggT(a, b) = ggT(b, r)')
print('0 < lambda < b/d\n')

a = int(input('a = '))
b = int(input('b = '))
d = ggT(a, b)
print('ggT({}, {}) = {}\n'.format(a, b, d))

print('0 < lambda < {}'.format(b//d))
la, mu = backwards(a, b, d)
print('lambda = {}'.format(la))
print('mu = {}'.format(mu))
print('{} = {} * {} + {} * {}'.format(d, la, a, mu, b))
