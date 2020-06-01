from csv import reader,DictReader,writer,DictWriter

# with open('file.csv','r') as f:
#     csv_reader=reader(f)
#     # iterator
#     # print(csv_reader)
#     next(csv_reader)
#     for row in csv_reader:
#         print(row)

# with open('file.csv','r') as f:
#     csv_reader=DictReader(f,delimiter='|')
#     for row in csv_reader:
#         # print(row)
#         print(row['email'])


# writer,DictWriter
with open('file1.csv','w') as f:
    csv_writer=writer(f)
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['isha','india'])
    # csv_writer.writerow(['me','india'])
    csv_writer.writerows([['name','country'],['isha','india'],['me','india']])

with open('final.csv','w',newline='') as f:
    csv_writer=DictWriter(f,fieldnames=['firstname','lastname','age'])
    csv_writer.writeheader()
    # csv_writer.writerow({
    # 'firstname':'isha',
    # 'lastname':'gupta',
    # 'age':20
    # })
    csv_writer.writerows([
    {
    'firstname':'isha',
    'lastname':'gupta',
    'age':20
    },
    {
    'firstname':'isha',
    'lastname':'gupta',
    'age':20
    },
    {
    'firstname':'isha',
    'lastname':'gupta',
    'age':20
    }
    ])


with open('final.csv','r') as rf:
    with open('file2.csv','w') as wf:
        csv_reader=DictReader(rf)
        csv_writer=DictWriter(wf,fieldnames=['firstname','lastname','age'])
        csv_writer.writeheader()
        for row in csv_reader:
            f,l,a=row['firstname'],row['lastname'],row['age']
            csv_writer.writerow({
            'firstname':f,
            'lastname':l,
            'age':a
            })
