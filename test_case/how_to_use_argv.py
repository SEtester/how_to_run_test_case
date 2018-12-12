#encoding:utf8

from sys import argv
print('argv是一个数组：',argv)

'''
sys.argv 命令行参数List，第一个元素是程序本身路径
sys.argv: 实现从程序外部向程序传递参数。
argv 是一个数组
使用命令行 执行脚本文件， 例: python how_to_use_argv.py pre-release 
输出arpv = ['how_to_use_argv.py','pre-release']
python 后面的参数 how_to_use_argv.py 和 pre-release 分别是数组的第一个元素和第二个元素
'''

