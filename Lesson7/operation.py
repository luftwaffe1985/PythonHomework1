import csv

def add_contact(data):
    with open('dict.csv', 'a', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for d in data:
            writer.writerow(d)
    print('Контакт успешно добавлен.')

def find_contact(data):
    with open('dict.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for _ in range(1):
                if row['Surname'] == data:
                    print(row['Name'],row['Surname'],row['Phone number'],row['Comment'] )