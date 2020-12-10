

def verify_survey_responses(survey_data):
    yes_survey_count = 0
    survey_group_answers = []
    for data in survey_data:
        if data:
            survey_group_answers.extend(list(data))
        else:
            print(f"Display hash data={survey_group_answers}")
            yes_survey_count += len(set(survey_group_answers))
            survey_group_answers.clear()

    # count the last iteration in the loop
    yes_survey_count += len(set(survey_group_answers))

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