import re
import jieba


def cut(string):
    return ' '.join(jieba.cut(string))


def token(string):
    string = re.findall('[\d|\w]+', string)
    return ' '.join(string)


def deal(string):
    string = token(string)
    return cut(string)


if __name__ == '__main__':
    string = '大家好, 我在学习NLP'
    print(deal(string))