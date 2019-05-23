# Automatic-speech-extraction
新闻人物言论自动提取

## 代码使用
本次项目中的　语法分析　都是使用　哈工大　的　LTP 。而该模型过大，不好传送到github上面，所以这里讲解下载方式。
	
    1. 打开链接　https://github.com/HIT-SCIR/pyltp

    2. 安装pyltp 

	pip install pyltp
    3.下载模型文件
	
  http://ltp.ai/download.html
  点击版本3.4.0 的 "模型" 下方的ltp_data_v3.4.0.zip文件。
    
    解压，然后将文件夹重命名为　model/ 然后放在　该项目文件中　即可。

最后　运行 index.py文件。
```
python index.py
```
然后在浏览器中输入网址 http://localhost:8091/
即可使用了。
## 语料库的获取
本次使用两个数据源，一个是wiki语料库，一个是新闻语料库。
1. wiki语料库	

	1. 
	找到链接 https://dumps.wikimedia.org/zhwiki/20190401/　
    
    找到　zhwiki-20190401-pages-articles.xml.bz
    (或者其他的.xml.bz也可以)　点击下载
    
	2. 
	打开链接 https://github.com/attardi/wikiextractor　然后克隆到本地
    ```
    git clone https://github.com/attardi/wikiextractor.git
    ```
    然后加入目录，运行程序　WikiExtractor.py
    ```
    $ python WikiExtractor.py zhwiki-20190401-pages-articles.xml.bz
    ```
    即可得到一个　text/　的文件夹,这就是我们得到的wiki中文语料库。
    将 text/ 放在和　data/get_data.py　同一个目录下

2. 新闻语料库

	可以从sql中提取，也可以从百度网盘自己下载。
    
    如果要从sql中提取，请在 data/get_data.py 中最小面填写相应的值（    host =     user =    password =　database =   　 port = ）
    
    如果从百度云盘中提取
	
    百度网盘链接为：
    
    将其放在 data/get_data.py　同一个目录下

## 语料库处理
进入 data/ 运行代码　get_data.py　即可。
```shell
$ cd data
$ python get_data.py
```
你会发现在　data/目录下，生成了一个名为 news-sentences-xut.txt的文本文件。

## 生成word2vec
进入　word2vec_model/　中,运行　make_word2vec.py　即可。
```
cd word2vec_model
python make_word2vec.py
```
你会发现在　word2vec_model/　得到了word2vermodel 这个word2vec 模型。

## 生成与"say"相近的词语
进入　similar_said/　中，　运行 get_word_similar_said.py 即可。
```
cd similar_said
python get_word_similar_said.py
```
你会发现在　similar_said/　得到了similar_said.txt里面存储了所有与say相近的词语。

