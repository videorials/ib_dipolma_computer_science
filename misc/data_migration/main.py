import os

def main():

	# >> -------------------- << delete csv file if one exits
	if os.path.exists("subjects_import.csv"):
		os.remove("subjects_import.csv")

	# >> -------------------- << count records in extract (insertion of linebreaks | line 50)
	num_lines = sum(1 for line in open('subjects_extract.txt'))

	# >> -------------------- << open files
	subjects_extract = open("subjects_extract.txt", "r", encoding="utf-8")
	subjects_import = open("subjects_import.csv", "a")

	# >> -------------------- << add headings to csv file
	subjects_import.write("id;subject_name;syl_code\n")

	# >> ======================================== << process data line by line <<

	line_number = 0
	for line in subjects_extract:
		line_number += 1
		# >> -------------------- << remove end of line character
		subject = line.replace("\n","")

		# >> -------------------- << extract and store syllabus code
		syl_code = ""
		for index in range(len(subject)-1, -1, -1):
			if subject[index].isdigit():
				syl_code = subject[index] + syl_code
				if len(syl_code) == 4:
					break

		# >> -------------------- << trim and repair subject name
		subject = subject[0:index -3]
		if subject[-1] == "-": subject += "1"
		if subject[-1] == "1": subject += ")"
		if subject[-1] == "g": subject += "e"

		# >> -------------------- << replace unrecognised characters (black diamond)
		for index in range(len(subject)):
			if subject[index] == "–":
				subject = (f"{subject[:index-1]} - {subject[index + 2:]}")

		# >> -------------------- << construct (combine) data
		id = f"{subject[:3]}_{syl_code[1:]}"
		data = f"{id};{subject};{syl_code}"

		if line_number < num_lines:
			data += "\n"

		# >> -------------------- << append to data file		
		subjects_import.write(data)

	# >> -------------------- << close files
			
	subjects_import.close()
	subjects_extract.close()

if __name__ == "__main__":
    main()