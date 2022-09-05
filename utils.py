FOOTEDNESS_MAPPING = {
    'Either': 1,
    'Left': 0.5,
    'Right': 0.5,
    'Right Only': 0,
    'Left Only': 0
}

POSITION_MAPPING = {
    'AM (R)': 'A',
    'ST (C)': 'A', 
    'AM (L)': 'A',
    'M (C)': 'M',
    'D (C)': 'D',
    'M (R)': 'M',
    'DM': 'M',
    'AM (C)': 'A',
    'M (L)': 'M',
    'D (R)': 'D',
    'D (L)': 'D',
    'WB (R)': 'D',
    'WB (L)': 'D',
}

NAME_FIX_LIST = [('â€š', '‚'), ('â€ž', '„'), ('â€¦', '…'), ('â€¡', '‡'), ('â€°', '‰'), ('â€¹', '‹'), ('â€˜', '‘'), ('â€™', '’'), ('â€œ', '“'), ('â€¢', '•'), ('â€“', '–'), ('â€”', '—'), ('â„¢', '™'), ('â€º', '›'), ('â‚¬', '€'), ('Ã‚', 'a'), ('Æ’', 'ƒ'), ('Ãƒ', 'a'), ('Ã„', 'a'), ('Ã…', 'a'), ('â€', '†'), ('Ã†', 'Æ'), ('Ã‡', 'ç'), ('Ë†', 'ˆ'), ('Ãˆ', 'e'), ('Ã‰', 'e'), ('ÃŠ', 'e'), ('Ã‹', 'e'), ('Å’', 'Œ'), ('ÃŒ', 'i'), ('Å½', 'z'), ('ÃŽ', 'i'), ('Ã‘', 'n'), ('Ã’', 'o'), ('Ã“', 'o'), ('â€', '”'), ('Ã”', 'o'), ('Ã•', 'o'), ('Ã–', 'o'), ('Ã—', '×'), ('Ëœ', '˜'), ('Ã˜', 'o'), ('Ã™', 'u'), ('Å¡', 'š'), ('Ãš', 'u'), ('Ã›', 'u'), ('Å“', 'œ'), ('Ãœ', 'u'), ('Å¾', 'ž'), ('Ãž', 'Þ'), ('Å¸', 'y'), ('ÃŸ', 'ß'), ('Â¡', 'i'), ('Ã¡', 'a'), ('Â¢', '¢'), ('Ã¢', 'a'), ('Â£', '£'), ('Ã£', 'a'), ('Â¤', '¤'),('Ã¤', 'a'), ('Â¥', '¥'), ('Ã¥', 'a'), ('Â¦', '¦'), ('Ã¦', 'æ'), ('Â§', '§'), ('Ã§', 'ç'), ('Â¨', '¨'), ('Ã¨', 'e'), ('Â©', '©'), ('Ã©', 'e'), ('Âª', 'ª'), ('Ãª', 'e'), ('Â«', '«'), ('Ã«', 'e'), ('Â¬', '¬'), ('Ã¬', 'i'), ('Â®', '®'), ('Ã®', 'i'), ('Â¯', '¯'), ('Ã¯', 'i'), ('Â°', '°'), ('Ã°', 'o'), ('Â±', '±'), ('Ã±', 'n'), ('Â²', '²'), ('Ã²', 'o'), ('Â³', '³'), ('Ã³', 'o'), ('Â´', '´'), ('Ã´', 'o'), ('Âµ', 'µ'), ('Ãµ', 'o'), ('Â¶', '¶'), ('Ã¶', 'o'), ('Â·', '·'), ('Ã·', '÷'), ('Â¸', '¸'), ('Ã¸', 'o'), ('Â¹', '¹'), ('Ã¹', 'u'), ('Âº', 'º'), ('Ãº', 'u'), ('Â»', '»'), ('Ã»', 'u'), ('Â¼', '¼'), ('Ã¼', 'u'), ('Â½', '½'), ('Ã½', 'y'), ('Â¾', '¾'), ('Ã¾', 'þ'), ('Â¿', '¿'), ('Ã¿', 'y'), ('Ã€', 'a'), ('Ã', 'e'), ('Ã', 'a'), ('Å', 's'), ('Ã', 'i'), ('Ã', 'i'), ('Ã', 'Ð'), ('Ã', 'y'), ('Ã', 'a'), ('Ã­', 'i'), ('Ã£', 'a')]

GK_ATTR = ['Thr', 'TRO', 'Ref', 'Pun', '1v1', 'Han', 'Ecc', 'Com', 'Cmd', 'Aer', 'Kic']

player_attr = ['Wor', 'Vis', 'Thr', 'Tec', 'Tea', 'Tck', 'Str', 'Sta', 'TRO', 'Ref', 'Pun', 'Pos', 'Pen', 'Pas', 'Pac', '1v1', 'OtB', 'Nat', 'Mar', 'L Th', 'Lon', 'Ldr', 'Kic', 'Jum', 'Hea', 'Han', 'Fre', 'Fla', 'Fir', 'Fin', 'Ecc', 'Dri', 'Det', 'Dec', 'Cro', 'Cor', 'Cnt', 'Cmp', 'Com', 'Cmd', 'Bra', 'Bal', 'Ant', 'Agi', 'Agg', 'Aer', 'Acc']

PLAYER_ATTR = list(set(player_attr) - set(GK_ATTR))

def apply_mean_attribute_list(df, new_attr, attr_list):
    df[new_attr] = sum([df[attr] for attr in attr_list]) / len(attr_list)

from datetime import datetime

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
    for fix in NAME_FIX_LIST:
        name = name.replace(fix[0], fix[1])
    return name

def same_sort(list1, list2, reverse=False):
    list1, list2 = (list(t) for t in zip(*sorted(zip(list1, list2), reverse=reverse)))
    return list1, list2