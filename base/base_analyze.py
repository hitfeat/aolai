import yaml


def analyze_data(file_name, case_key):
    with open("./data/%s" % file_name) as f:
        data = yaml.load(f,  Loader=yaml.FullLoader)
        temp_data = data[case_key]
        data_list = list()
        for item in temp_data.values():
            data_list.append(item)
        return data_list
