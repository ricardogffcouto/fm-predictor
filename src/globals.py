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

GK_ATTR = ['Thr', 'TRO', 'Ref', 'Pun', '1v1', 'Han', 'Ecc', 'Com', 'Cmd', 'Aer', 'Kic']

OUTFIELDER_ATTR = ['Wor', 'Vis', 'Thr', 'Tec', 'Tea', 'Tck', 'Str', 'Sta', 'TRO', 'Ref', 'Pun', 'Pos', 'Pen', 'Pas', 'Pac', '1v1', 'OtB', 'Nat', 'Mar', 'L Th', 'Lon', 'Ldr', 'Kic', 'Jum', 'Hea', 'Han', 'Fre', 'Fla', 'Fir', 'Fin', 'Ecc', 'Dri', 'Det', 'Dec', 'Cro', 'Cor', 'Cnt', 'Cmp', 'Com', 'Cmd', 'Bra', 'Bal', 'Ant', 'Agi', 'Agg', 'Aer', 'Acc']

PLAYER_ATTR = list(set(OUTFIELDER_ATTR) - set(GK_ATTR))