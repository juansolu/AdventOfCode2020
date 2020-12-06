
class PassWordPolicy(object):
    min_char_count = 0
    max_char_count = 0
    required_char = None
    password_to_evaluate = None

    def is_password_valid(self):
        if not self.required_char:
            #if no required char is setup always fail password
            return False

        required_char_count = self.password_to_evaluate.count(self.required_char)
        if  required_char_count >= self.min_char_count and required_char_count <= self.max_char_count:
            return True

        return False


def password_policy_builder(entry):
    char_count_index = 0
    char_req_index = 1
    password_index = 2

    password_tokens = entry.split(' ')
    char_reqs = password_tokens[char_count_index].split('-')
    password_policy = PassWordPolicy()
    password_policy.min_char_count = int(char_reqs[0])
    password_policy.max_char_count = int(char_reqs[1])

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

data = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
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


