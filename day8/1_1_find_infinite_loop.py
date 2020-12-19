import time

def perform_operation(action, curr_action_index, accumulator):
    command = action.split(" ")

    if command[0] == "nop":
        return curr_action_index + 1, accumulator
    elif command[0] == "acc":
        accumulator += int(command[1])
        return curr_action_index + 1, accumulator
    elif command[0] == "jmp":
        return curr_action_index + int(command[1]), accumulator

    return curr_action_index, accumulator

def run_program_until_duplicate_step(entries):
    action_index = 0
    accumulator = 0
    visited_instructions = []
    run = True

    while run:
        action_index = action_index % len(entries) #ensure we don't go over the available command entries
        #print(f"Action index={action_index + 1}")
        next_operation_index, accumulator = perform_operation(entries[action_index], action_index, accumulator)

        if next_operation_index == action_index or next_operation_index in visited_instructions:
            return accumulator
        else:
            visited_instructions.append(next_operation_index)
            action_index = next_operation_index


start_time = time.monotonic()
my_file = open("input.txt", "r")
entries = [x.strip() for x in my_file.readlines()]

accumulator = run_program_until_duplicate_step(entries)
end_time = time.monotonic() - start_time

print(f"Found answer count={accumulator}")
print(f"Time to execute={end_time}")