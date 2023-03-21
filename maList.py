#student=["Sam", "Pep", "Andre", "Young", "Marie", "Ruth"]

#print(student[2])

#def element():
#	for n in range(len(student)):
#		print(student[n])

#element()



student=[{
	"Sam": "France",
	"Solo":"Maroc",
	"Andre" : "Guinee",
	"Rose" : "Canada",
	"Namory" :" Chine",
	"Salif": "USA",
	"Dame" : "Senegal",
	"Chantal" : "Cote d'ivoire",
	"Amadou" :"Belgique"
}, {

    'spam': 'eggs',
    'knights': 'lumberjack',
    'bacon': 'sausage'    

},
{'voiture': 'véhicule à quatre roues',
 'vélo': 'véhicule à deux roues',
 'tricycle': 'véhicule à trois roues'}
]
for cle in student:
	for n in cle:
		if n== 'spam':
			print(cle[n])
#or n in students:
#	print(n, students[n], sep=",")
