# usr/bin/env python

from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np

#Takes two points and returns a list with X steps between the points
def interpolate(point_1, point_2, steps):
	dp = (point_2 - point_1)/(steps)
	interpolate = [point_1 + (step * dp) for step in range(steps)]

	#plt.plot(np.linspace(0,1,len(interpolate)), interpolate)
	#plt.scatter(np.linspace(0,1,len(interpolate)), interpolate)
	#plt.show()
	return interpolate
	
def fit_dataset(beg_res, end_res, data):
	steps = beg_res/end_res
	interpolated = []
	
	for lower_point, higher_point in zip(data[:-1], data[1:]):
		interpolated.extend( interpolate(lower_point, higher_point, steps) )
	interpolated.append(data[-1])
	return interpolated
'''
example_dataset = Dataset('exercise_one_data.nc', mode = 'r')

lats = [float(lon) for lon in np.linspace(0,10,3)]

new_lats = fit_dataset(5, 1, lats)

plt.plot(np.linspace(0,1,len(new_lats)), new_lats)
plt.scatter(np.linspace(0,1,len(new_lats)), new_lats)
plt.show()
'''









































































#Note, 2d datasets are much more complicated
#I would recommend using built in functions to do a 2d dataset, otherwise you have to work with flattening along axis

two_d_lats = [list(np.linspace(i, 10+i, 3)) for i in range(0,10,5)]
for l in two_d_lats:
	plt.scatter(l, l, s = 100, c = 'g')

#SO now we have the second dimension interpolated, what about the first?
first_row = [l[0] for l in two_d_lats]
print first_row
#Now we have a list of the first dimension, first list, start and end point
#Now lets interpolate by it
first_row = fit_dataset(5, 1, first_row)

second_row = [l[1] for l in two_d_lats]
second_row = fit_dataset(5, 1, second_row)

third_row = [l[2] for l in two_d_lats]
third_row = fit_dataset(5, 1, third_row)
#put rows in order
new_dataset = [first_row, second_row, third_row]
#transpose the data
new_dataset = [list(x) for x in zip(*new_dataset)]
#Fill in the second dimension
final_dataset = []
for l in new_dataset:
	final_dataset.append(fit_dataset(5, 1, l))
#But now make this automatic for the number of rows


