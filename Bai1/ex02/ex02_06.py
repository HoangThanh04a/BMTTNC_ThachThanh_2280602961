input_str = input("Nhập X,Y: " )
dimensisons = [int(x) for x in input_str.split(',')]
row_Num = dimensisons[0]
col_Num = dimensisons[1]
multilist = [[0 for col in range (col_Num)]for row in range (row_Num)]
for row in range(row_Num):
    for col in range (col_Num):
        multilist[row][col] = row * col
print(multilist)