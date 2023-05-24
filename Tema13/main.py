from datetime import date
from functional import seq


### Exercitiul 1 ###

class Person:
    def __init__(self, first_name: str, last_name: str, date_of_birth: date, email_address: str):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email_address = email_address

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.date_of_birth.isoformat()} {self.email_address}'


# yearsago and num_years from https://stackoverflow.com/a/765990
def yearsago(years, from_date):
    try:
        return from_date.replace(year=from_date.year - years)
    except ValueError:
        # Must be 2/29!
        return from_date.replace(month=2, day=28, year=from_date.year-years)


def num_years(begin, end):
    num_years = int((end - begin).days / 365.2425)
    if begin > yearsago(num_years, end):
        return num_years - 1
    else:
        return num_years


def exercitiul1():
    people = seq(
        Person("John", "Doe", date(1960, 11, 3), "jdoe@example.com"),
        Person("Ellen", "Smith", date(1992, 5, 13), "ellensmith@example.com"),
        Person("Jane", "White", date(1986, 2, 1), "janewhite@example.com"),
        Person("Bill", "Jackson", date(1999, 11, 6), "bjackson@example.com"),
        Person("John", "Smith", date(1975, 7, 14), "johnsmith@example.com"),
        Person("Jack", "Williams", date(2005, 5, 28), "")
    )

    youngest = people.sorted(lambda p: p.date_of_birth, reverse=True).first()
    oldest = people.sorted(lambda p: p.date_of_birth).first()
    print(f'Youngest person is {youngest}')
    print(f'Oldest person is {oldest}')

    underage = people.filter(lambda p: num_years(p.date_of_birth, date.today()) < 18)
    print(f'Underage people {underage}')

    emails = people.map(lambda p: p.email_address)
    print(f'emails {emails}')

    emails = people.map(lambda p: (f'{p.first_name} {p.last_name}', p.email_address)).dict()
    print(f'emails {emails}')

    emails = people.map(lambda p: (p.email_address, p)).dict()
    print(emails)

    grouped = people.group_by(lambda p: p.date_of_birth.month)
    print(f'birthdays each month {grouped}')

    partitioned = people.partition(lambda p: p.date_of_birth.year <= 1980)
    print(f'people born before/after 1980 {partitioned}')

    distinct_fn = people.map(lambda p: p.first_name).distinct()
    print(f'first names: {distinct_fn}')

    average_age = people.map(lambda p: num_years(p.date_of_birth, date.today())).average()
    print(f'average age: {average_age}')

    count = people.filter(lambda p: p.last_name).count(lambda _: True)
    print(f'number of people named Smith: {count}')

    optional = people.filter(lambda p: p.first_name == 'John').last_option()
    match optional:
        case None:
            print('No person named John :(')
        case person:
            print(f'He exists: {person}')

    search_result = people.filter(lambda p: p.first_name == 'Thomas').map(lambda p: p.last_name)
    match search_result:
        case None:
            print('No person named Thomas found :(')
        case person:
            print(f'There he is: {person}')

    missing_emails = people.filter(lambda p: len(p.email_address) == 0)
    print(f'missing emails {missing_emails}')


def exercitiul3():
    lst = seq(1, 21, 75, 39, 7, 2, 35, 3, 31, 7, 8)
    result = lst.filter(lambda x: x >= 5).grouped(2).map(lambda l: l[0] * l[1]).sum()
    print(f'Processed: {lst}')
    print(f'\t=>{result}')


if __name__ == "__main__":
    exercitiul1()
    exercitiul3()
