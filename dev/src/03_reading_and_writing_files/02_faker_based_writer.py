from faker import Faker
import csv


def write_sample_file():
    with open('myCSV2.csv', mode='w', newline='', encoding='utf-8') as output:
        faker = Faker()
        writer = csv.writer(output)
        header = ['name', 'age', 'street', 'city', 'state','zip','lng','lat']
        writer.writerow(header)
        for r in range(200):
            writer.writerow([
                faker.name(),
                faker.random_int(min=20, max=80, step=1),
                faker.street_address(),
                faker.city(),
                faker.state(),
                faker.zipcode(),
                faker.longitude(),
                faker.latitude()
            ])


if __name__ == '__main__':
    write_sample_file()


