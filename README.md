# InstructureCodingTest
coding test from Instructure


- Launch the python code:

python dataLoad.py


- enter one or more csv files seperated by space, the program will process file(s) and print all active ones

001.csv 002.csv 003.csv
**************************************************
Receiving and processing CSV files: ['001.csv', '002.csv', '003.csv']
Active Course: Suicide

Active Course: Chemistry
	Active Student: Daniel Kelly

Active Course: Astronautics
	Active Student: Michael Cox
	Active Student: William Allen
	Active Student: Olivia Price

Active Course: Air warfare
	Active Student: Mia Hill

Active Course: Holidays
	Active Student: Alexander Stewart
	Active Student: Daniel Phillips
	Active Student: Aiden Richardson

Active Course: Feelings

Active Course: Canoeing
	Active Student: Chloe Wood
	Active Student: Daniel Bennett

Active Course: French language
	Active Student: Abigail Hughes

Active Course: Judiciary

Active Course: Abortion, law
	Active Student: William Roberts
	Active Student: William Gray

**************************************************


- a batch running

cat csv.txt | python dataLoad.py


