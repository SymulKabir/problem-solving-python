def find_duplicates(ids):
    duplicate_ids = []
    for index, id in enumerate(ids):
        remaining_ids = ids[index + 1:]
        for sub_id in remaining_ids:
            if sub_id == id:
                duplicate_ids.append(sub_id)
    return duplicate_ids


def find_duplicates_2(ids):
    duplicate_ids = []
    list_length = len(ids)
    
    for i in range(list_length):
        for sub_i in range(i + 1, list_length):
            if ids[sub_i] == ids[i]:
                if not ids[sub_i] in duplicate_ids:
                    duplicate_ids.append(ids[sub_i])
                
    print(f"duplicates: {duplicate_ids}")
    return duplicate_ids
        


ids = [12, 12, 42, 7, 22, 43, 42, 22, 12]


find_duplicates_2(ids)