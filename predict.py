import  csv
import  sys
import  os.path

value = []

with open("indexes.csv", 'r') as csv_file :
    try :
        dict_val = csv.reader(csv_file, delimiter = ",")
        for row in dict_val :
            value.append(row)
    except :
        sys.exit("Error: File {:} cannot be read".format(csv_file))

check = False
while check == False :
    mileage = input("Enter mileage: ")
    try :
        number_mileage = float(mileage) - 0
        if (number_mileage >= 0) :
            check = True
        else :
            print ("Error: negative mileage? Try again.")
    except :
        print ("Error: not a number, try again.")

print (float(value[0][0]) + (float(value[0][1]) * number_mileage))