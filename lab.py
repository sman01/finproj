import csv
from csv import writer
from csv import reader


default_text = 'Some Text'
senti=[]
i=0


# Open the input_file in read mode and output_file in write mode
with open('Scraped_Car_Review_suzuki.csv', 'r') as read_obj, \
        open('output_1.csv', 'w', newline='') as write_obj:
    # Create a csv.reader object from the input file object
    csv_reader = reader(read_obj)
    
    for row in csv_reader:
        try:
            a = row[6]
        except IndexError:
            a = 'null'
        if a=='Rating':
            senti.append("Sentiment")
        elif a!=None and a!='null':
            if float(a)>3.5:
                senti.append("good")
            elif float(a)<3.6:
                senti.append("bad")
        
        else:
            senti.append("NA")
    # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        row.append(senti[i])
        csv_writer.writerow(row)
        i+=1
    print(i)
    

        
    print("done")
