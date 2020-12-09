import re

class Passport(object):

    _byr = 0 #(Birth Year) - four digits; at least 1920 and at most 2002.
    _iyr = 0 #(Issue Year) - four digits; at least 2010 and at most 2020.
    _eyr = 0 #(Expiration Year) - four digits; at least 2020 and at most 2030.
    _hgt = None #(Height) - a number followed by either cm or in:
        #If cm, the number must be at least 150 and at most 193.
        #If in, the number must be at least 59 and at most 76.
    _hcl = None #(Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    _ecl = None #(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    _pid = None #(Passport ID) - a nine-digit number, including leading zeroes.
    _cid = None #(Country ID) - ignored, missing or not.
    _raw_data = None

    # Set byr if business rules pass
    def set_byr(self, byr):
        if not byr:
            return

        byr = byr.strip()
        try:
            byr_candidate = int(byr)
            #range method goes to one before limit
            if byr_candidate in range(1920, 2003):
                self._byr = byr_candidate
        except ValueError:
            pass

    # Set iyr if business rules pass
    def set_iyr(self, iyr):
        if not iyr:
            return

        iyr = iyr.strip()
        try:
            iyr_candidate = int(iyr)
            #range method goes to one before limit
            if iyr_candidate in range(2010, 2021):
                self._iyr = iyr_candidate
        except ValueError:
            pass

    # Set eyr if business rules pass
    def set_eyr(self, eyr):
        if not eyr:
            return

        eyr = eyr.strip()
        try:
            eyr_candidate = int(eyr)
            #range method goes to one before limit
            if eyr_candidate in range(2020, 2031):
                self._eyr = eyr_candidate
        except ValueError:
            pass

    # set hcl if business rules pass (is hex color)
    def set_hcl(self, hcl):
        if not hcl:
            return

        hcl = hcl.strip()

        #is hex color regex
        match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hcl)
        if match:
            self._hcl = hcl

    # set ecl if business rules pass
    def set_ecl(self, ecl):
        if not ecl:
            return

        ecl = ecl.strip()

        if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            self._ecl = ecl


    # Set hgt if business rules pass
    def set_hgt(self, hgt):
        if not hgt:
            return

        hgt = hgt.strip()
        try:
            if hgt.endswith('cm'):
                range_tuple = (150,194)
                hgt_clean = hgt.replace('cm', '')
            elif hgt.endswith('in'):
                range_tuple = (59,77)
                hgt_clean = hgt.replace('in', '')
            else:
                #no valid measurement type
                return

            hgt_candidate = int(hgt_clean)
            if hgt_candidate in range(range_tuple[0], range_tuple[1]):
                self._hgt = hgt
        except ValueError:
            pass

    # set pid if business rules pass
    def set_pid(self, pid):
        if not pid:
            return

        pid = pid.strip()

        #is 9 digit string
        match = re.search(r'^[0-9]{9}$', pid)
        if match:
            self._pid = pid


    def is_valid(self):

        if not self._byr:
            print("INVALID byr missing data")
            return False

        if not self._pid:
            print("INVALID pid missing data")
            return False

        if not self._ecl:
            print("INVALID ecl missing data")
            return False

        if not self._hcl:
            print("INVALID hcl missing data")
            return False

        if not self._hgt:
            print("INVALID hgt missing data")
            return False

        if not self._eyr:
            print("INVALID eyr missing data")
            return False

        if not self._iyr:
            print("INVALID iyr missing data")
            return False

        return True


    def get_passport_dict_data(self, all_fields_data):
        # atttempted to use regex but too brittle, parse keys explicitely
        tokens = all_fields_data.split(" ")
        passport_tokens = {}
        for token in tokens:
            key_value = token.split(":")
            if key_value[0] == 'eyr':
                passport_tokens['eyr'] = key_value[1]
            elif key_value[0] == 'byr':
                passport_tokens['byr'] = key_value[1]
            elif key_value[0] == 'iyr':
                passport_tokens['iyr'] = key_value[1]
            elif key_value[0] == 'hgt':
                passport_tokens['hgt'] = key_value[1]
            elif key_value[0] == 'hcl':
                passport_tokens['hcl'] = key_value[1]
            elif key_value[0] == 'ecl':
                passport_tokens['ecl'] = key_value[1]
            elif key_value[0] == 'pid':
                passport_tokens['pid'] = key_value[1]
            elif key_value[0] == 'cid':
                passport_tokens['cid'] = key_value[1]

        return passport_tokens


    def initilize_from_data(self, data):

        self.raw_data = " ".join(data)
        field_dict = self.get_passport_dict_data(self.raw_data)
        if 'byr' in field_dict:
            self.set_byr(field_dict['byr'])
        if 'iyr' in field_dict:
            self.set_iyr(field_dict['iyr'])
        if 'eyr' in field_dict:
            self.set_eyr(field_dict['eyr'])
        if 'hgt' in field_dict:
            self.set_hgt(field_dict['hgt'])
        if 'hcl' in field_dict:
            self.set_hcl(field_dict['hcl'])
        if 'ecl' in field_dict:
            self.set_ecl(field_dict['ecl'])
        if 'pid' in field_dict:
            self.set_pid(field_dict['pid'])
        if 'cid' in field_dict:
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
# start_time = time.monotonic()
# my_file = open("example_invalid_passports.txt", "r")
# passport_data = [x.strip() for x in my_file.readlines()]
# valid_passports_count = validate_passports(passport_data)
# end_time = time.monotonic() - start_time

# print("Invalid Example passport count={}".format(valid_passports_count))
# print("Example Time={}".format(end_time))

# start_time = time.monotonic()
# my_file = open("example_valid_passports.txt", "r")
# passport_data = [x.strip() for x in my_file.readlines()]
# valid_passports_count = validate_passports(passport_data)
# end_time = time.monotonic() - start_time

# print("Valid Example passport count={}".format(valid_passports_count))
# print("Example Time={}".format(end_time))

start_time = time.monotonic()
#Acutally test with input data
my_file = open("input.txt", "r")
passport_data = [x.strip() for x in my_file.readlines()]
valid_passports_count = validate_passports(passport_data)
end_time = time.monotonic() - start_time

print(f"Valid passport count={valid_passports_count}")
print(f"Time={end_time}")