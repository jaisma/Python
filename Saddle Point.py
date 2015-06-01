def saddlePoint(matrix):
    #assume good matrix
    points = []
    saddlePoint = matrix
    for row_idx, row in enumerate(saddlePoint):
        rowMin = min(row)
        temp = []
        for col_idx, col in enumerate(saddlePoint):
            temp.append((col[row.index(rowMin)]))
        colMax = max(temp)
        if (rowMin == colMax):
            points.append((row_idx, row.index(rowMin)))
    return set(points)

def main():
    testinput = [[9,4,3,1,5],[7,8,4,9,6],[3,7,2,6,2],[1,5,3,7,8],[5,2,1,8,9]]
    print(saddlePoint(testinput))
    
if __name__ == '__main__':
    main()
