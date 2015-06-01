def main():
    fname = 'score.txt'
    count = 0
    classAvg = 0
    with open(fname) as f:
        content = f.readlines()
    f.close()
    for info in content:
        indInfo = info.split()
        indAvg = (int(indInfo[2]) + int(indInfo[3])) / 2
        classAvg += indAvg
        indInfo.append(str(indAvg))
        content[count] = indInfo
        count += 1
    for info in content:
        info.append(str(float(info[4]) - classAvg/len(content)))
    print (content[0])
    f = open('result.txt', 'w')
    f.write('first name\tlast name\tmidterm\t\tfinal\t\taverage\t\tdeviation\n')
    for info in content:
        for abc in info:
            f.write(abc)
            f.write('\t\t')
        f.write('\n')
    f.write("\nclass average: ")
    f.write(str(classAvg/len(content)))
    f.write("\n")
    f.close()
        
if __name__ == '__main__':
    main()

