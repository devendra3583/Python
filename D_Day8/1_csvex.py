import csv
 

def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    '''   
    with open(path, "ab") as csv_file:
        
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
    '''
    csv_file=open(path,'wb')
    writer = csv.writer(csv_file)

    for i in data:
        writer.writerow(i)
        
    
    csv_file.close()
            
    

if __name__ == "__main__":
    
    data = [['Dev','Arya','Jhansi'],['Himanshu','Kishor','Agra']]
    path = "out123.csv"
    
    csv_writer(data, path)
    print 'Added sucessfully'
