def writeFile(inFileName, outFileIf):
    inFile = open(inFileName, "rb")

    contents = inFile.read()
    dataLen = len(contents)

    #KybeleのファイルサイズをArrayで格納
    bary = bytearray([])
    for var in range(0, 4):
        bary.append((dataLen >> (8 * var)) & 0X000000FF)

    #ファイルに書き出す
    outFileIf.write(bary)
    outFileIf.write(contents)

    inFile.close()