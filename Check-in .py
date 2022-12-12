'''The program will compute the percentage of the food's calories that are due to fat,
and will display the input information and the percentage in the form of a complete English sentence.'''
#Pogram name is healthy meal
#Name of your Dish
name=str(input("enter the name of the item: "))
#serving size in gram
serving = int(input("Enter the serving size in gram: "))
#Fat Value of your meal
fat = float(input("Enter the grams of fat in a serving: "))
#carbohydrates vlue of your meal
carb = float(input("Enter the grams of carbohydrates in a serving: "))
#Protein Value 
protein = float(input("Enter the grams of protein in a serving: "))
#As we know 1g Protein = 4kacl
proteinValue = int(protein) * 4
#As we know 1g carbohydrates = 4kacl
carbValue = int(carb) * 4
#As we know 1g Fat = 9kacl
fatValue = int(fat) * 9
#Final calculation
servingValue = int(serving) / int(fatValue) + int(carbValue) + int(proteinValue) * 100
print(name)
print(servingValue)
