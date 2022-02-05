# V tomto úkolu budeš opět vytvářet histogram. Tentokrát se ale nebude vykreslovat zleva doprava,
# ale zespodu nahoru. Funkce vert_histogram(), která vytvoří histogram, by opět měla brát sequence čísel,
# na jehož základě se bude histogram tvořit.

# Výsledek by měl vypadat nějak takto:

# [[' 10|', '  ', '  ', '  ', '**', '  ', '  ', '  '],
#  ['  9|', '  ', '  ', '  ', '**', '  ', '  ', '  '],
#  ['  8|', '  ', '  ', '  ', '**', '  ', '  ', '  '],
#  ['  7|', '  ', '  ', '**', '**', '  ', '  ', '  '],
#  ['  6|', '  ', '  ', '**', '**', '**', '  ', '  '],
#  ['  5|', '  ', '**', '**', '**', '**', '  ', '  '],
#  ['  4|', '**', '**', '**', '**', '**', '  ', '  '],
#  ['  3|', '**', '**', '**', '**', '**', '**', '  '],
#  ['  2|', '**', '**', '**', '**', '**', '**', '**'],
#  ['  1|', '**', '**', '**', '**', '**', '**', '**'],
#  ['   ________________________________']]

from pprint import pprint


def vert_histogram(sequence):
    hist = []
    curr_row_num = max(sequence)

    while curr_row_num > 0:
        one_row = create_row(sequence, curr_row_num)
        hist.append(one_row)
        curr_row_num -= 1
    return hist


def create_row(sequence, curr_row_num):
    row = [curr_row_num]
    number_of_it = curr_row_num
    for number in sequence:
        if number >= number_of_it:
            row.append('|')
        else:
            row.append(' ')
    return row


pprint(vert_histogram([4, 5, 7, 10, 6, 3, 2]))


#################### reseni ze cviceni #######################################################

# def vert_histogram(data, col_width=2):
#     LABEL_WIDTH = len(str(max(data))) + 1
#     DATASET_SIZE = len(data)
#     hist = []
#     current_row_num = max(data)
#     while current_row_num > 0:
#         row = generate_row(current_row_num, col_width, data, LABEL_WIDTH, DATASET_SIZE)
#         hist.append(row)
#         current_row_num -= 1
#     hist.append(make_baseline(col_width, LABEL_WIDTH, DATASET_SIZE))
#     return hist
#
#
# def generate_row(current_row_num, col_width, data, LABEL_WIDTH, DATASET_SIZE):
#     label = '{: >{w}}|'.format(current_row_num, w=LABEL_WIDTH)
#     row = [label] + [' ' * col_width] * DATASET_SIZE
#     for i in range(DATASET_SIZE):
#         if data[i] >= current_row_num:
#             row[i + 1] = '*' * col_width
#     return row
#
#
# def make_baseline(col_width, LABEL_WIDTH, DATASET_SIZE):
#     label_offset = [' '] * LABEL_WIDTH + [' ']
#     line = ['_' * (col_width + 2)] * DATASET_SIZE + ["_"] * 2
#     return [''.join(label_offset + line)]
#
#
# def print_histogram(hist):
#     # print()
#     for line in hist:
#         print('  '.join(line))
#
#
# hist = vert_histogram([4, 5, 7, 9, 6, 3, 2], 4)
# print_histogram(hist)
