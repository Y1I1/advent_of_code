with open('advent_of_code/day_1_input.txt', 'r') as f:
    max_Cal = 0
    temp_Cal = 0
    current_Cal = 0
    for line in f:
        if line == '\n':    
            temp_Cal = current_Cal
            current_Cal = 0
            max_Cal = max_Cal if max_Cal > temp_Cal else temp_Cal
        else:
            current_Cal += int(line)

print(max_Cal)