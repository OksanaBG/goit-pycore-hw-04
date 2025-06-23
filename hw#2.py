def get_cats_info(path):
    cats_info = []

    try:
        with open(path, mode='r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cats_info.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                else: 
                    
                    return None
                   
    except FileNotFoundError:
        print(f"Thre is no file by this path:'{path}'.")
    except Exception as error:
        print(f"The file is damaged: {error}")

    return cats_info


path_to = str(input("Please enter the path to file:>>>"))
if path_to == '':
    print("The path is empty")
else:        
    try:
        cats = get_cats_info(path_to)
        if cats is None:
            print("Inforamtion is incorrect")
        else:
            print("Cats info:", cats)
    except:
        print("Something wrong")