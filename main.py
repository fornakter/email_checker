import csv
import re
from glob import glob


def save_to_file(date_to_save, name_of_file):
    count_file = 1

    while True:
        prepear_file = name_of_file + str(count_file) + '.txt'
        try:
            open(prepear_file)
        except:
            print('Utworzono plik: ', prepear_file)
            open(prepear_file, 'w').write(date_to_save)
            break
        else:
            print('Nazwa', prepear_file, 'zajeta')
            count_file += 1


def read_file():
    emails_csv = []
    emails_txt = []
    for path in glob('emails/*.txt'):
        with open(path, 'rt') as f:
            for line in f:
                line = line.strip('\n')
                emails_txt.append(line)
    for path in glob('emails/*.csv'):
        with open(path, 'r') as f:
            f_csv = csv.DictReader(f, delimiter=';')
            for row in f_csv:
                emails_csv.append(row['email'])
    all_emails = emails_txt + emails_csv
    return all_emails


def show_incorrect_emails():
    result = ""
    all_emails = read_file()
    regex = re.compile(r'\b[A-Za-z\d._%+-]+@[A-Za-z\d.-]+\.[A-Z|a-z]{2,}\b')
    count_emails = 0
    for line in all_emails:
        if re.fullmatch(regex, line):
            pass
        else:
            count_emails += 1
            print(line)
            result = result + line + "\n"
    save_to_file(result, "incorrect")
    print('Number of wrong emails: ', count_emails)


def search_for_string():
    result = ""
    all_emails = read_file()
    string_search = input("Enter a word: ")
    count_emails = 0
    for line in all_emails:
        line = line.strip('\n')
        if re.findall(string_search, line):
            count_emails += 1
            print(line)
            result = result + line + '\n'
    save_to_file(result, "string_result")
    print(count_emails)


def group_emails_by_domain():
    result = ""
    all_emails = read_file()
    emails_sorted = []
    domains = []
    regex = re.compile(r'@[A-Za-z\d.-]+\.[A-Z|a-z]{2,}\b')
    for line in all_emails:
        line = line.strip('\n')
        emails_sorted.append(line)
        reg_search = re.search(regex, line)
        if reg_search:
            domains.append(reg_search.group())
    domains.sort()
    group_domains = [[]]
    pattern_domain = domains[0]
    d = 0
    while len(domains) > 0:

        if pattern_domain == domains[0]:
            group_domains[d].append(domains[0])
            domains.remove(pattern_domain)
        else:
            pattern_domain = domains[0]
            d += 1
            group_domains.append([])
    for i in range(len(group_domains)):
        result1 = (f'Ilosc domen {group_domains[i][0]}: {len(group_domains[i])}')
        print(result1)
        result = result + result1 + '\n'
    save_to_file(result, "domains")


def sort_by_domain():
    return print('I sad, its not ready, yet')
    # all_emails = read_file()
    # regex = re.compile(r'@[A-Za-z\d.-]+\.[A-Z|a-z]{2,}\b')
    # # all_emails.sort(regex)
    # print(all_emails)


def number_of_emails():
    all_emails = read_file()
    print('All emails: ', len(all_emails))
    menu()


def read_me():
    print('''
----- Readme ----------------------------------------------------------------

Check Your files with email

Functions:
* Search incorrect emails on files. Ex. test1gmail.com, test2@hotmail
* Find a word in email. Ex. search word 'stone' in emails. 
  Result: find 2 emails: astone@domain.com, stonegrade@doom.com
* Group emails by domain.
  Result:
  Nubmer or @gmail.com: 33
  Number of @domain.com: 21
  number of @hotmail.com: 4
* Sort by domain. Alphabetic sorting by domain (not ready yet)

Files must be on '/emails' folder

Supported files:
  .txt
  .csv

Limit of flies or emails: not found. Checked on 60 files with 12252 emails.
Works correctly and fast.

--------------------------------------------------------------------------------
    ''')


def menu():
    print('''
    1. Show incorret emails
    2. Search for string
    3. Group emails by domain
    4. Sort by domain - not ready, yet
    5. Numer of emails
    6. Readme
    ''')
    chose = input('I chose: ')
    match chose:
        case '1':
            show_incorrect_emails()
        case '2':
            search_for_string()
        case '3':
            group_emails_by_domain()
        case '4':
            sort_by_domain()
        case '5':
            number_of_emails()
        case '6':
            read_me()
        case _:
            print('I dont know what is this')


if __name__ == '__main__':
    menu()
