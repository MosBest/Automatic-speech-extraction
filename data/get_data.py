import pymysql
import os
import data.urils as urils


# 从数据库中得到新闻语料库
def get_news_from_sql(host, user, password, database, port):

    db = pymysql.connect(host, user, password, database, port)

    cursor = db.cursor()
    with open('news-sentences-xut.txt', 'a') as f:
        sql = """select content from sqlResult_1558435 """
        try:
            cursor.execute(sql)
        except:
            print("Error")
            return

        news = cursor.fetchall()

        for j in range(len(news)):
            data = news[j][0]
            text = urils.deal(data)
            f.write(text + '\n')

    cursor.close()
    db.close()


# 从wiki中得到语料库

def get_data(path):
    dir_name = os.listdir(path)
    STRING = []
    for name in dir_name:
        print("name", name)
        one_path = os.path.join(path, name)
        all_ = os.listdir(one_path)
        for file in all_:
            print("file", file)
            data = open(os.path.join(one_path, file))
            yield data.readlines()


def get_word_from_wiki(path):
    data = get_data(path)

    with open('news-sentences-xut.txt', 'a') as f:
        while True:
            try:
                b = next(data)
                text = [urils.deal(string) for string in b if string!='\n']
                for n in text:
                    f.write(n + '\n')
            except:
                break


def get_news_from_netdist(netdist_path):
    pass

if __name__ == '__main__':

    host = "******"
    user = "**"
    password = "**"
    database = "**"
    port = 0
    try:
        get_news_from_sql(host, user, password, database, port)
    except:
        netdist_path = './'
        get_news_from_netdist(netdist_path)

    # wiki_path = '/home/zhaodao/下载/text/'
    wiki_path = './text/'
    get_word_from_wiki(wiki_path)
