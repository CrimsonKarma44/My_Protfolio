import json, csv, time

def save_to_json(dic):
    dic['Time'] = time.time()
    with open('storage/database.json', 'r') as file_in:
        content = json.load(file_in)
        content[dic['Name']] = dic
        with open('database.json', 'w') as file_out:
            json.dump(content, file_out)

def save_to_csv(dic):
    dic['time'] = time.time()
    # with open('database.csv', 'a', newline='') as file_in:
    #     writer = csv.writer(file_in, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     writer.writerow([dic['Name'], dic['Email'], dic['Subject'],dic['Message'], dic['time]])

    # using dict
    with open('storage/database.csv', 'a', newline='') as file_in:
        field = ['Name', 'Email', 'Subject', 'Message', 'time']
        writer = csv.DictWriter(file_in, fieldnames=field)
        writer.writerow(dic)
