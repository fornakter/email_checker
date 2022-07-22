import csv
import re
from glob import glob


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
    all_emails = read_file()
    regex = re.compile(r'\b[A-Za-z\d._%+-]+@[A-Za-z\d.-]+\.[A-Z|a-z]{2,}\b')
    count_emails = 0
    for line in all_emails:
        if re.fullmatch(regex, line):
            pass
        else:
            count_emails += 1
            print(line)
    print('Number of wrong emails: ', count_emails)


def search_for_string():
    all_emails = read_file()
    string_search = input("Enter a word: ")
    count_emails = 0
    for line in all_emails:
        line = line.strip('\n')
        if re.findall(string_search, line):
            count_emails += 1
            print(line)
    print(count_emails)


def group_emails_by_domain():
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
        print(f'Ilosc domen {group_domains[i][0]}: {len(group_domains[i])}')


def group_by_domain():
    all_emails = read_file()
    regex = re.compile(r'@[A-Za-z\d.-]+\.[A-Z|a-z]{2,}\b')
    #all_emails.sort(regex)
    print(all_emails)


if __name__ == '__main__':
    group_by_domain()
