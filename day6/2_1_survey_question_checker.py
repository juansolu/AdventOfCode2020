

def verify_survey_responses(survey_data):
    yes_survey_count = 0
    survey_group_answers = None
    group_count = 0
    for data in survey_data:
        if data:
            survey_single_person_answers = set(list(data))
            # Important to check for None explicitely as empty Set would be Falsey
            if survey_group_answers is not None:
                survey_group_answers = set.intersection(survey_group_answers, survey_single_person_answers)
            else:
                survey_group_answers = survey_single_person_answers
        else:
            group_count += 1
            #print(f"Display hash data={survey_group_answers}")
            yes_survey_count += len(survey_group_answers)
            print(f"group_count={group_count} with answers={yes_survey_count}")
            survey_group_answers = None

    # count the last iteration in the loop
    #print(f"Display hash data={survey_group_answers}")
    yes_survey_count += len(survey_group_answers)

    return yes_survey_count

import time
start_time = time.monotonic()
#Acutally test with input data
my_file = open("input.txt", "r")
survey_questions = [x.strip() for x in my_file.readlines()]

yes_answers_count = verify_survey_responses(survey_questions)

end_time = time.monotonic() - start_time

print(f"Found answer count={yes_answers_count}")
print(f"Time to execute={end_time}")
