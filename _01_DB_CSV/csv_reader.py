import csv

def get_csv_data(filename):
    data_from_csv = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data_from_csv.append(row)

    return data_from_csv

def write_csv_in_file(filename, data):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("Данные записаны!")
    return True


if __name__ == '__main__':
    print(get_csv_data(r'files\data.csv'))
    data_to_write = [
        ['Name', 'Age', 'City'],
        ['Alice', '30', 'New York'],
        ['Bob', '25', 'Los Angeles'],
        ['Charlie', '35', 'Chicago']
    ]
    print(write_csv_in_file(r'files\output_data.csv', data_to_write))