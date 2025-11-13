
def load_data(data_path):
    with open(data_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data
