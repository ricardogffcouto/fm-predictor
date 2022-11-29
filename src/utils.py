from datetime import datetime

def apply_mean_attribute_list(df, new_attr, attr_list):
    df[new_attr] = sum([df[attr] for attr in attr_list]) / (len(attr_list) * 20)

def approximate_age_2020(d1):
    try:
        d1 = datetime.strptime(d1, "%Y-%m-%d").year
        d2 = datetime.strptime("2019-12-31", "%Y-%m-%d").year
        return abs(d2 - d1)
    except:
        return None

def name_to_id(name):
    return "-".join(map(lambda x: x.lower(), name.split(' ')))

def name_char_replacer(name):
    name_fix_list = [('â€š', '‚'), ('â€ž', '„'), ('â€¦', '…'), ('â€¡', '‡'), ('â€°', '‰'), ('â€¹', '‹'), ('â€˜', '‘'), ('â€™', '’'), ('â€œ', '“'), ('â€¢', '•'), ('â€“', '–'), ('â€”', '—'), ('â„¢', '™'), ('â€º', '›'), ('â‚¬', '€'), ('Ã‚', 'a'), ('Æ’', 'ƒ'), ('Ãƒ', 'a'), ('Ã„', 'a'), ('Ã…', 'a'), ('â€', '†'), ('Ã†', 'Æ'), ('Ã‡', 'ç'), ('Ë†', 'ˆ'), ('Ãˆ', 'e'), ('Ã‰', 'e'), ('ÃŠ', 'e'), ('Ã‹', 'e'), ('Å’', 'Œ'), ('ÃŒ', 'i'), ('Å½', 'z'), ('ÃŽ', 'i'), ('Ã‘', 'n'), ('Ã’', 'o'), ('Ã“', 'o'), ('â€', '”'), ('Ã”', 'o'), ('Ã•', 'o'), ('Ã–', 'o'), ('Ã—', '×'), ('Ëœ', '˜'), ('Ã˜', 'o'), ('Ã™', 'u'), ('Å¡', 'š'), ('Ãš', 'u'), ('Ã›', 'u'), ('Å“', 'œ'), ('Ãœ', 'u'), ('Å¾', 'ž'), ('Ãž', 'Þ'), ('Å¸', 'y'), ('ÃŸ', 'ß'), ('Â¡', 'i'), ('Ã¡', 'a'), ('Â¢', '¢'), ('Ã¢', 'a'), ('Â£', '£'), ('Ã£', 'a'), ('Â¤', '¤'),('Ã¤', 'a'), ('Â¥', '¥'), ('Ã¥', 'a'), ('Â¦', '¦'), ('Ã¦', 'æ'), ('Â§', '§'), ('Ã§', 'ç'), ('Â¨', '¨'), ('Ã¨', 'e'), ('Â©', '©'), ('Ã©', 'e'), ('Âª', 'ª'), ('Ãª', 'e'), ('Â«', '«'), ('Ã«', 'e'), ('Â¬', '¬'), ('Ã¬', 'i'), ('Â®', '®'), ('Ã®', 'i'), ('Â¯', '¯'), ('Ã¯', 'i'), ('Â°', '°'), ('Ã°', 'o'), ('Â±', '±'), ('Ã±', 'n'), ('Â²', '²'), ('Ã²', 'o'), ('Â³', '³'), ('Ã³', 'o'), ('Â´', '´'), ('Ã´', 'o'), ('Âµ', 'µ'), ('Ãµ', 'o'), ('Â¶', '¶'), ('Ã¶', 'o'), ('Â·', '·'), ('Ã·', '÷'), ('Â¸', '¸'), ('Ã¸', 'o'), ('Â¹', '¹'), ('Ã¹', 'u'), ('Âº', 'º'), ('Ãº', 'u'), ('Â»', '»'), ('Ã»', 'u'), ('Â¼', '¼'), ('Ã¼', 'u'), ('Â½', '½'), ('Ã½', 'y'), ('Â¾', '¾'), ('Ã¾', 'þ'), ('Â¿', '¿'), ('Ã¿', 'y'), ('Ã€', 'a'), ('Ã', 'e'), ('Ã', 'a'), ('Å', 's'), ('Ã', 'i'), ('Ã', 'i'), ('Ã', 'Ð'), ('Ã', 'y'), ('Ã', 'a'), ('Ã­', 'i'), ('Ã£', 'a')]

    for fix in name_fix_list:
        name = name.replace(fix[0], fix[1])
    return name

def same_sort(list1, list2, reverse=False):
    list1, list2 = (list(t) for t in zip(*sorted(zip(list1, list2), reverse=reverse)))
    return list1, list2