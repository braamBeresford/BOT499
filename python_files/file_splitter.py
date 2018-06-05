import sys
import os
import time
wholeFile = False
arr = []
index = -1

def splitFiles(fileName, chops):
	try:
		with open(fileName, "r") as file:
			pass
	except FileNotFoundError as e:
			print("Invalid file name")

	else:
		with open(fileName, "r") as file:
			# Read the header line
			header = file.readline()

			# Read the rest of file
			data = file.readlines()

			temp_header = ""
			temp_data = ""


			total_lines = len(data)
			lines_per_file = int(total_lines/chops) + (total_lines%chops >0)
			# print(os.path.basename(fileName))
			for i in range(chops):
				file_part_path = "./data/split/" + os.path.basename(fileName) + ".part" + str(i+1)

				part_file = open(file_part_path, "w")
				print(file_part_path)

				# part_file.write(header)

				for line in data[i*lines_per_file : i* lines_per_file + lines_per_file]:
					if "Sequence" in line:
						temp = "sequence"
						
					elif ">" not in line:
						temp = line[:-1]
						part_file.write(temp)
					elif ">" in line and temp != "sequence":
						part_file.write('\n')


				part_file.flush()
				part_file.close()





def usage():
	'''Informs how to use the file'''
	print("usage: python3 file_splitter.py file number_of_files")

if len(sys.argv) < 2:
	usage()

else:
	fileName = sys.argv[1]
	try:
		chops = int(sys.argv[2])
	except: 
		usage()

	else:
		splitFiles(fileName, chops)
