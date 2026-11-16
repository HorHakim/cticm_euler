import matplotlib.pyplot as plt
import math

# méthode approchée euler
x = [0]
F_euler = [2]

step = 0.001
a, b = 0, 10


number_points = int((b-a) / step)

for index_point in range(1, number_points):
	x.append(x[-1] + step)
	# x.append(x[0] + index_point * step)
	
	next_f_value = F_euler[-1] * (3*step + 1)
	F_euler.append(next_f_value)
######################################################
# on calcule les vraie valeur de f pour les comparer

F_real_values = []

def real_f_function(x):
	return 2 * math.exp(3*x)

for x_value in x:
	real_f_value = real_f_function(x_value)
	F_real_values.append(real_f_value)



######################################################



plt.figure(figsize=(15,6))
plt.title("Exemple de comparaison entre une solution analytique et une approximation d'Euler")
plt.plot(x, F_euler, 'ro', label="Approximation Euler")
plt.plot(x, F_real_values, "b-", label="Solution analytique")
plt.xlabel("Les valeurs de X")
plt.ylabel("Contraintes")
plt.legend()
plt.show()