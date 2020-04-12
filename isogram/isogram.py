def is_isogram(string):
    string_wo_space = string.replace(" ", "")
    string_wo_space = string_wo_space.replace("-", "")
    string_len = len(string_wo_space)
    set_len = len(set(string_wo_space.lower()))
    return string_len == set_len

