##  install miniconda3 and pytorch in Ubuntu

### download

1\

sudo apt-get install wget

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh

2\  another way


download from miniconda3 website or from tsinghua source

3\

软件下载，使用清华镜像源，便于下载，进入清华镜像源anaconda页面：https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/，再进入miniconda下载目录https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/，由于python2已停止更新，我们选择以python3编写的miniconda3

wget -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py37_4.8.3-Linux-x86_64.sh


### install


# 一直按回车然后输入yes

please answer 'yes' or 'no':

>>> yes


不建议通过conda init进行初始化，因为可能会导致conda与系统里的软件相冲突。
Do you wish the installer to initialize Miniconda3
by running conda init? [yes|no]
[no] >>> no


### init miniconda3 

command:  eval "$(/home/frank/miniconda3/bin/conda shell.bash hook)"





Do you wish the installer to initialize Miniconda3 by running conda init? [yes|no]

[no] >>> yes



运行配置信息文件或重启电脑




