import sys
from MyException import MyException
from makeUpdataData import writeFile

#引数チェック実装
try:
    args = sys.argv
    updateFile = open("Update.bin", "wb")

    if len(args) >= 2:
        writeFile(args[1], updateFile)
        if len(args) == 3:
            writeFile(args[2], updateFile)
        else:
            bary = bytearray([0,0,0,0])
            updateFile.write(bary)
    else:
        raise MyException()

except MyException:
    print('引数が不足しています。')

except Exception as e:
    print("Normal Exception ", e)