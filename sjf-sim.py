def scheduler(jobs):

    while jobs:
        shortest_len = min(jobs.values())
        shortest_jobs = [
            name for name, steps in jobs.items() if steps == shortest_len]
        shortest = sorted(shortest_jobs)[0]  # tie-break alphabetically

        print(f"-> Task {shortest} finished")
        jobs.pop(shortest)

    print("All tasks finished!")


while True:
    userinput = input(
        "Please enter the process names (separated by whitespace):\n").split()
    steps_number = input(
        "Now enter the number of steps in the same order of your processes (separated by whitespace):\n").split()
    try:
        steps_number_int = list(map(int, steps_number))
        if len(userinput) != len(steps_number_int):
            print("Every process needs a number of steps!")
            continue
        all_processes = {}

        for pname, steps_num in zip(userinput, steps_number_int):
            all_processes[pname] = steps_num

    except ValueError:
        print("Please enter only Integers!")
        continue

    scheduler(all_processes)
    break
