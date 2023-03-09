import SL
import functions
import sys


if __name__ == "__main__":
    args = sys.argv[1:]

    # 解析参数
    while args:
        arg = args.pop(0)
        if arg == '-m' or arg == '--method':
            function.DCParams['method'] = args.pop(0)
        elif arg == '-p' or '--path':
            function.DCParams['path'] = args.pop(0)


    DCTask = {
            'params':functions.DCParams.copy(),
            'function':functions.downloadContent
            
