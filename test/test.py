import numpy as np
from scipy import special
from scipy import integrate

result = integrate.quad(lambda x: special.jv(0,x), 0, np.Inf)
print result
