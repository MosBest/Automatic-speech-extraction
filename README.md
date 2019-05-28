# Automatic-speech-extraction
新闻人物言论自动提取

## 假如你想将该web项目 部署到　你的云服务器中，直接使用
### 部署环境
则操作为：
( 
详细请看　资料（非常详细）https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04)
1. 先安装辅助工具
```
sudo apt update

sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools


```
2. 安装python3.6
https://blog.csdn.net/qq_24326765/article/details/81916399
```
sudo add-apt-repository ppa:jonathonf/python-3.6 

sudo apt-get update

sudo apt-get install python3.6
```
3. 安装python3.6的venv模块
```
sudo apt install python3.6-venv
```
4. 创建一个虚拟环境
```
mkdir ~/myproject
cd ~/myproject
python3.6 -m venv myprojectenv
```
5. 激活虚拟环境
```
source myprojectenv/bin/activate

```
您的提示将更改为表示您现在正在虚拟环境中运行。它看起来像这样。`(myprojectenv)user@host:~/myproject$`

以后：

**无论您使用的是哪个版本的Python，在激活虚拟环境时，都应该使用pip命令（不是pip3）。**

### 拷贝该项目代码
本次项目中的　语法分析　都是使用　哈工大　的　LTP 。而该模型过大，不好传送到github上面，所以这里讲解下载方式。

1.

    1. 打开链接　https://github.com/HIT-SCIR/pyltp

    2. 安装pyltp 

	pip install pyltp
    
    （注意pyltp最高仅仅支持　python3.6, 如果是python3.7就会有错误）
   
    3.下载模型文件
		
        方法1:   http://ltp.ai/download.html 点击版本3.4.0 的 "模型" 下方的 ltp_data_v3.4.0.zip 文件。
        
        	然后使用git 上传到服务器中。
        
        方法2: 
        	由于可能是命令行界面，所以无法使用方法１，那么尝试方法2-----使用aria2从百度网盘中下载。
            
            首先在火狐浏览器上安装插件（也可以不安装）：    　				　　　　　　　　　https://www.jianshu.com/p/758b2cdbafa3
            
            然后安装　aria2
            ```
            sudo apt-get install aria2  (安装aria2)
            ```
            
            下载：
            命令行中直接输入
            ```
            aria2c -c -s10 -k1M -x16 --enable-rpc=false -o "ltp-models/3.4.0/ltp_data_v3.4.0.zip" --header "User-Agent: netdisk;5.3.4.5;PC;PC-Windows;5.1.2600;WindowsBaiduYunGuanJia" --header "Referer: https://pan.baidu.com/disk/home" --header "Cookie: BDUSS=3I5N1dNVU1OWmJ6eDZCfm1BbFRUbEZrM20xWDVyWFlDV0dUWERRVWNlYkp2dHRjRVFBQUFBJCQAAAAAAAAAAAEAAADrI7l0tqG088qmc2hpbmUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMkxtFzJMbRcc; pcsett=1559100731-ac8e8b067e0bc1a125ed1ca22aa1e20f" "https://d.pcs.baidu.com/file/9452681dc592872b3db4aed7864de446?fid=2738088569-250528-114982644725200&dstime=1559014341&rt=sh&sign=FDtAERV-DCb740ccc5511e5e8fedcff06b081203-SgWWAd2mj9JImnNUvfrZmhItw4s%3D&expires=8h&chkv=1&chkbd=0&chkpc=&dp-logid=3420496203325285758&dp-callid=0&shareid=1988562907&r=216576088"
            ```

2. 

	克隆该项目　git clone git@github.com:MosBest/Automatic-speech-extraction.git

3. 

将（１）中得到的　ltp_data_v3.4.0.zip　解压，然后将文件夹重命名为　model/ ，然后放在　该项目文件中　即可。

### 设置防火墙
```
pip install wheel

pip install uwsgi
sudo ufw allow 端口号
```
（端口号和你index.py的一致）

### 运行代码
安装代码中需要的函数库：
```
pip install gensim
pip install jieba
pip install bottle
```

运行 index.py文件。

(注意 index.py中　root.run(host='', port=8051) host应该是'0.0.0.1', port是端口号，看服务器提供了哪些可用)

(修改index.py时，可以使用nano命令，或者vim命令)


```
python index.py
```

### 结束

然后　浏览器中输入网址 “　http://你云服务器的域名或者ip: 端口号/　”既可以访问网址了。



## 如果你想自己从头到位理解一遍

### 语料库的获取
本次使用两个数据源，一个是wiki语料库，一个是新闻语料库。
1. wiki语料库	

	1. 
	找到链接 https://dumps.wikimedia.org/zhwiki/20190401/　
    
    找到　zhwiki-20190401-pages-articles.xml.bz
    (或者其他的.xml.bz也可以)　点击下载
    
	2. 
	打开链接 https://github.com/attardi/wikiextractor
    
    然后克隆到本地
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

### 语料库处理
进入 data/ 运行代码　get_data.py　即可。
```shell
$ cd data
$ python get_data.py
```
你会发现在　data/目录下，生成了一个名为 news-sentences-xut.txt的文本文件。

### 生成word2vec
进入　word2vec_model/　中,运行　make_word2vec.py　即可。
```
cd word2vec_model
python make_word2vec.py
```
你会发现在　word2vec_model/　得到了word2vermodel 这个word2vec 模型。

### 生成与"say"相近的词语
进入　similar_said/　中，　运行 get_word_similar_said.py 即可。
```
cd similar_said
python get_word_similar_said.py
```
你会发现在　similar_said/　得到了similar_said.txt里面存储了所有与say相近的词语。

