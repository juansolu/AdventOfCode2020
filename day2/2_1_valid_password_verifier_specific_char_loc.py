
class PassWordPolicy(object):
    char_found_index = 0
    char_not_index = 0
    required_char = None
    password_to_evaluate = None

    def is_password_valid(self):
        if not self.required_char:
            #if no required char is setup always fail password
            print("No char found!")
            return False

        char_found_once_where_expected = False
        if self.password_to_evaluate[self.char_found_index] == self.required_char:
            char_found_once_where_expected = True

        if self.password_to_evaluate[self.char_not_index] == self.required_char:
            # if there was already a character found we should not find a required char here.
            if char_found_once_where_expected:
                char_found_once_where_expected = False
            else:
                # There is a required char at this location and it was not found in previous location
                char_found_once_where_expected = True

        return char_found_once_where_expected


def password_policy_builder(entry):
    char_count_index = 0
    char_req_index = 1
    password_index = 2

    password_tokens = entry.split(' ')
    char_reqs = password_tokens[char_count_index].split('-')
    password_policy = PassWordPolicy()

    # subtract 1 to treat char location as zero index
    password_policy.char_found_index = int(char_reqs[0]) - 1
    password_policy.char_not_index = int(char_reqs[1]) - 1

    #only care about first char
    password_policy.required_char = password_tokens[char_req_index][0]

    password_policy.password_to_evaluate = password_tokens[password_index]

    return password_policy

def get_password_policy_result(entries):
    valid_password = 0

    for entry in entries:
        entry = password_policy_builder(entry)
        if entry.is_password_valid():
            valid_password += 1

    return valid_password

data = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc', '3-5 f: fgfff']
valid_password_count = get_password_policy_result(data)
print("Found password valid count={}".format(valid_password_count))

import time
start_time = time.monotonic()
#Acutally test with input data
my_file = open("input.txt", "r")
entries = [x.strip() for x in my_file.readlines()]
valid_password_count = get_password_policy_result(entries)
end_time = time.monotonic() - start_time

print("Found password valid count={}".format(valid_password_count))
print("Time={}".format(end_time))


