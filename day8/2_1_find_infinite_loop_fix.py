import time

def is_potential_bad_command(command):
    return bool(command in ["nop", "jmp"])

def flip_command_if_prudent(cmd):
    if cmd[0] == "nop" and cmd[1] != 0:
        return "jmp " + cmd[1]
    elif cmd[0] == "jmp":
        return "nop " + cmd[1]
    else:
        return cmd[0] + " " + cmd[1]

def perform_operation(cmd, offset, curr_action_index, accumulator):
    if cmd == "nop":
        return curr_action_index + 1, accumulator
    elif cmd == "acc":
        accumulator += int(offset)
        return curr_action_index + 1, accumulator
    elif cmd == "jmp" and int(offset) != 0:
        return curr_action_index + int(offset), accumulator

    #when in doubt go to next command to avoid infinite loops in one index
    return curr_action_index + 1, accumulator

def run_program_until_completion_or_duplicate(entries, action_index, accumulator):
    visited_instructions = []
    run = True

    while run:
        action_index = action_index % len(entries) #ensure we don't go over the available command entries
        if action_index == 0 and accumulator != 0:
            return accumulator

        command = entries[action_index].split(" ")
        next_operation_index, accumulator = perform_operation(command[0], command[1], action_index, accumulator)

        if next_operation_index == action_index or next_operation_index in visited_instructions:
            return -1
        else:
            visited_instructions.append(next_operation_index)
            action_index = next_operation_index


def fix_program(entries):
    for index, entry in enumerate(entries):
        command = entry.split(" ")
        if is_potential_bad_command(command[0]):
            altered_program = entries.copy()
            altered_program[index] = flip_command_if_prudent(command)
            accumulator = run_program_until_completion_or_duplicate(altered_program, 0, 0)
            if accumulator != -1:
                return accumulator
        else:
            continue

    return -1 #unable to find correct cmd to fix

start_time = time.monotonic()
my_file = open("input.txt", "r")
entries = [x.strip() for x in my_file.readlines()]

accumulator = fix_program(entries)
end_time = time.monotonic() - start_time

print(f"Found answer count={accumulator}")
print(f"Time to execute={end_time}")