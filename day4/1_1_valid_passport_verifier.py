
class Passport(object):
    byr = None #(Birth Year)
    iyr = None #(Issue Year)
    eyr = None #(Expiration Year)
    hgt = None #(Height)
    hcl = None #(Hair Color)
    ecl = None #(Eye Color)
    pid = None #(Passport ID)
    cid = None #(Country ID)
    raw_data = None


    def is_valid(self):

        if not self.byr:
            print("INVALID byr missing data")
            return False

        if not self.pid:
            print("INVALID pid missing data")
            return False

        if not self.ecl:
            print("INVALID ecl missing data")
            return False

        if not self.hcl:
            print("INVALID hcl missing data")
            return False

        if not self.hgt:
            print("INVALID hgt missing data")
            return False

        if not self.eyr:
            print("INVALID eyr missing data")
            return False

        if not self.iyr:
            print("INVALID iyr missing data")
            return False

        return True


    def initilize_from_data(self, data):
        self.raw_data = data
        for tokens in data:
            if 'byr:' in tokens:
                self.byr = True
            if 'iyr:' in tokens:
                self.iyr = True
            if 'eyr:' in tokens:
                self.eyr = True
            if 'hgt:' in tokens:
                self.hgt = True
            if 'hcl:' in tokens:
                self.hcl = True
            if 'ecl:' in tokens:
                self.ecl = True
            if 'pid:' in tokens:
                self.pid = True
            if 'cid:' in tokens:
                self.cid = True


def validate_passports(passport_data):
    valid_passport_count = 0
    #print("Passport full data={}".format(passport_data))
    passport_tokens = []
    for data in passport_data:
        if data:
            passport_tokens.append(data)
        else:
            passport = Passport()
            passport.initilize_from_data(passport_tokens)
            if passport.is_valid():
                valid_passport_count += 1
            else:
                print(f"Raw data={passport.raw_data}")
            passport_tokens.clear()

    #check for last entry if we never got one last newline
    passport = Passport()
    passport.initilize_from_data(passport_tokens)
    if passport.is_valid():
        valid_passport_count += 1
    else:
        print(f"Raw data={passport.raw_data}")

    return valid_passport_count

import time
start_time = time.monotonic()
#Acutally test with input data
my_file = open("example_data.txt", "r")
passport_data = [x.strip() for x in my_file.readlines()]
valid_passports_count = validate_passports(passport_data)
end_time = time.monotonic() - start_time

print("Valid Example passport count={}".format(valid_passports_count))
print("Example Time={}".format(end_time))

start_time = time.monotonic()
#Acutally test with input data
my_file = open("input.txt", "r")
passport_data = [x.strip() for x in my_file.readlines()]
valid_passports_count = validate_passports(passport_data)
end_time = time.monotonic() - start_time

print(f"Valid passport count={valid_passports_count}")
print(f"Time={end_time}")