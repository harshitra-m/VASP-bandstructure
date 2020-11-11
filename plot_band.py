import numpy as np
from matplotlib import pyplot as plt

efermi = 6.1669 


## EXTRACTING BAND DATA
data = np.char.split(np.loadtxt("./EIGENVAL", delimiter = "\n", dtype=np.str))

# Defining the empty arrays - define as needed
band1 = []; band2 = []; band3= []; band4 = []; band5 = []; band6 = []; band7 = []; band8 = [];
vals = [band1, band2, band3, band4, band5, band6, band7, band8]


# Parsing the data and filling in eigenvalues 
for j in range(0, len(vals)):
	for i in range(8+j, len(data), 10):
			vals[j].append(float(data[i][1]) - efermi)



## GENERATING K-POINT PATH
kpoints = np.char.split(np.loadtxt("./KPOINTS", delimiter="\n", dtype=np.str))

fullpath = np.array([''.join([kpoints[0][3], kpoints[0][4]])])
path_labels = (np.char.split(fullpath, '-'))[0]

path_points = np.array([0.0])
xs = np.array([0.0])


# Calculating x values corresponding to the bands
for i in range(4,len(kpoints), 2):
	point1 = (float(kpoints[i][2]) - float(kpoints[i + 1][2]))**2
	point2 = (float(kpoints[i][1]) - float(kpoints[i + 1][1]))**2
	point3 = (float(kpoints[i][0]) - float(kpoints[i + 1][0]))**2

	length = np.sqrt(point1 + point2 + point3)
	new_points = np.linspace(float(xs[-1]), float(xs[-1]) + float(length), num=int(kpoints[1][0]))

	xs = np.append(xs, new_points)
	path_points = np.append(path_points, xs[-1])


new_xs = np.delete(xs,0)


# Plotting 
fig, ax = plt.subplots()

for ii in range(0, len(path_points)):
	plt.axvline(x=float(path_points[ii]), linestyle = 'dotted', color='k')


ax.set(xlabel='k-point path', ylabel='Energy (eV)',
       title='Bandstructure of Diamond phase FCC Si (VASP)')
ax.set_xticks(path_points)
ax.set_xticklabels(path_labels)

plt.axhline(y=0, linestyle='solid', color='grey')

plt.plot(new_xs, band1)
plt.plot(new_xs, band2)
plt.plot(new_xs, band3)
plt.plot(new_xs, band4)
plt.plot(new_xs, band5)
plt.plot(new_xs, band6)
plt.plot(new_xs, band7)
plt.plot(new_xs, band8)

# Saving figure
plt.savefig('bands.pdf')



