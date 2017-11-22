import math

dinosaur_details = {}
dinosaur_speed = {}
g = 9.8

with open('dataset1.csv') as dinosaur_data:
	for nr, line in enumerate(dinosaur_data):
		if nr > 0:
			dinosaur_name = line.split(',')[0]
			dinosaur_leg_length = line.split(',')[1]
			dinosaur_details[dinosaur_name] = [dinosaur_leg_length,]

with open('dataset2.csv') as dinosaur_file:
	for c, line in enumerate(dinosaur_file):
		if c > 0:
			dinosaur_data = line.strip().split(',')
			dinosaur_name = dinosaur_data[0]
			dinosaur_stride = float(dinosaur_data[1])
			dinosaur_stance = dinosaur_data[2]
			if dinosaur_stance == 'bipedal':
				try:
					dinosaur_leg_length = float(dinosaur_details[dinosaur_name][0])
					dinosaur_speed[dinosaur_name] = ((dinosaur_stride / dinosaur_leg_length) - 1) * math.sqrt(
						dinosaur_leg_length * g)
				except KeyError as err:
					pass

for n, details in enumerate(sorted(dinosaur_speed.items(), key=lambda x: x[1], reverse=True)):
	dinosaur_name = details[0]
	dinosaur_speed = details[1]
	print("{0}) {1}'s speed is {2:.2g} m/s".format(n + 1, dinosaur_name, dinosaur_speed))
