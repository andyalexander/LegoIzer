import pandas as pd

def string_to_rgb(col_string):
    b1 = int(f'0x{col_string[0:2]}',0)
    b2 = int(f'0x{col_string[2:4]}',0)
    b3 = int(f'0x{col_string[4:]}',0)
    return (b1,b2,b3)

# def write_xml(df, fn):
    # with open(fn, )