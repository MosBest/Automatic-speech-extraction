import re
import jieba


def cut(string):
    return ' '.join(jieba.cut(string))


def token(string):
    string = re.findall('[\d|\w|\u3002 |\uff1f |\uff01 |\uff0c |\u3001 |\uff1b |\uff1a |\u201c |\u201d |\u2018 |\u2019 |\uff08 |\uff09 |\u300a |\u300b |\u3008 |\u3009 |\u3010 |\u3011 |\u300e |\u300f |\u300c |\u300d |\ufe43 |\ufe44 |\u3014 |\u3015 |\u2026 |\u2014 |\uff5e |\ufe4f |\uffe5]+', string)
    return ' '.join(string)


def deal(string):
    string = token(string)
    return cut(string)


if __name__ == '__main__':
    string = '大家好， 我在学习NLP'
    print(deal(string))
