# You will be supplied with two data files in CSV format. The first file contains
# statistics about various dinosaurs. The second file contains additional data.
#
# Given the following formula,
#
# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
# Where g = 9.8 m/s^2 (gravitational constant)
#
# Write a program to read in the data files from disk, it must then print the names
# of only the bipedal dinosaurs from fastest to slowest. Do not print any other information.
#
# $ cat dataset1.csv
# NAME,LEG_LENGTH,DIET
# Hadrosaurus,1.2,herbivore
# Struthiomimus,0.92,omnivore
# Velociraptor,1.0,carnivore
# Triceratops,0.87,herbivore
# Euoplocephalus,1.6,herbivore
# Stegosaurus,1.40,herbivore
# Tyrannosaurus Rex,2.5,carnivore
# ..
# ..
# ..
# $ cat dataset2.csv
# NAME,STRIDE_LENGTH,STANCE
# Euoplocephalus,1.87,quadrupedal
# Stegosaurus,1.90,quadrupedal
# Tyrannosaurus Rex,5.76,bipedal
# Hadrosaurus,1.4,bipedal
# Deinonychus,1.21,bipedal
# Struthiomimus,1.34,bipedal
# Velociraptor,2.72,bipedal
# ..
# ..
# ..

dinosaur_details = {}
dinosaur_speed = {}
g = flot(9.8)


def sqrt(leg_lenght, g)


with open('dataset1.csv') as dinosaur_data:
	for line in dinosaur_data:
		dinosaur_name = line.split(',')[0]
		dinosaur_leg_length = line.split(',')[1]
		dinosaur_details(dinosaur_name) = (dinosaur_leg_length,)

with open('dataset2.cvs') as dinosaur_file:
	for line in dinosaur_file:
		dinosaur_data = line.split(',')
		dinosaur_name = disosaur_data[0]
		disnosaur_stance = dinosaur_data[2]
		dinosaur_stride = dinosaur_data[1]
		if disnosaur_stance == 'bipedal':
			leg_lenght = dinosaur_details[dinosaur_name][0]
			try:
				float(dinosaur_stride)
				float(leg_lenght)
			except:
				ValueError as e:
			speed = ((dinosaur_stride / leg_lenght) - 1) * sqrt(leg_lenght, g)
			dinosaur_speed(speed) = [dinosaur_name]
for dinosaur in dinosaur_speed.sorted(reverse=True):
	print(dinosaur[dinosaur_name])

