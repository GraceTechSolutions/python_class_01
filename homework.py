# Sum of matrix

# m1 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# m2 = [
#     [6,8,7],
#     [6,1,4],
#     [0,2,7]
# ]

# main_list = []
# for row in range(len(m1)):
#     temp_list = []
#     row1 = m1[row]
#     row2 = m2[row]

#     for col in range(len(row1)):
#         e1 = row1[col]
#         e2 = row2[col]
#         temp_list.append(e1+e2)
    
    # print(temp_list)
#     main_list.append(temp_list)

# print(main_list)


# Display row or column or element of matrix

matrix = [
    [1,2,3],
    [3,4,5],
    [7,8,9]
]

def find_element(matrix, row=None, col=None):
    if row and col:
        # print(f'Accessing element of row {row} and column {col}')
        print(matrix[row-1][col-1])
        return matrix[row-1][col-1]
    elif row:
        # print(f'Accessing element of row {row}')
        print(matrix[row-1])
        return matrix[row-1]
    elif col:
        main = []
        # print(f'Accessing element of column {col}')
        for rows in matrix:
            main.append(rows[col-1])
        
        print(main)
        return(main)
    else:
        print('Please provide an valid input')
        return(False)

find_element(matrix,1)
