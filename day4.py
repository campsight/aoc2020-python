from aoc_help import *

lines = read_file('data/input-day4.txt')

passports = []
passport_nb = 0
passports.append({})

for line in lines:
    if line:
        entries = line.split(" ")
        for e in entries:
            (field, value) = e.split(":")
            passports[passport_nb][field] = value
    else:
        passport_nb += 1
        passports.append({})

# part 1

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
nb_valids = 0

for pp in passports:
    nb_valids += (required_fields.issubset(pp.keys()))

print(nb_valids)


# part 2
VALID_ECL = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def check_year(ymin, ymax, val):
    if (not len(val) == 4) or not (ymin <= int(val) <= ymax):
        return False
    return True


def check_height(hgt):
    if hgt[-2:] == "cm":
        return 150 <= int(hgt[0:(len(hgt)-2)]) <= 193
    if hgt[-2:] == "in":
        return 59 <= int(hgt[0:(len(hgt) - 2)]) <= 76
    return False


def isalphanum_lower(c):
    if 48 <= ord(c) <= 57:
        return True
    if 97 <= ord(c) <= 122:
        return True
    return False


def check_hair(hcl):
    if not (hcl[0] == "#"):
        return False
    return len([x for x in hcl if isalphanum_lower(x)]) == 6


def check_valid(passport):
    if not check_year(1920, 2002, passport['byr']):
        return False
    if not check_year(2010, 2020, passport['iyr']):
        return False
    if not check_year(2020, 2030, passport['eyr']):
        return False
    if not check_height(passport['hgt']):
        return False
    if not check_hair(passport['hcl']):
        return False
    if passport['ecl'] not in VALID_ECL:
        return False
    if (len(passport['pid']) != 9) or (not passport['pid'].isdigit()):
        return False
    return True


nb_valids = 0

for pp in passports:
    if required_fields.issubset(pp.keys()):
        nb_valids += check_valid(pp)

print(nb_valids)
