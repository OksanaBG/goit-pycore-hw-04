def total_salary(path):
   
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0

            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        salary = float(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        print(f"Incorrect input in line: {line.strip()}")
                        continue

            if count == 0:
                return (0, 0)

            average = total / count
            return (total, average)

    except FileNotFoundError:
        print("File is not founded.")
        
        return (0, 0)
    except Exception as e:
        print(f"Error: {e}")
        return (0, 0)
    
path_to = str(input("Please enter the path to file:>>>"))
if path_to == '':
    print("The path is empty")
else:        
    try:
        total, average =total_salary(path_to)
        print(f"The Total amount is {total} and average is {average}")


    except:
        print("Something wrong")