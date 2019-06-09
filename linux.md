### 出现错误如下
```
Unable to init server: Could not connect: Connection refused
Unable to init server: Could not connect: Connection refused

(3-1_abnormal_check.py:1546): Gdk-CRITICAL **: 06:16:05.336: gdk_cursor_new_for_display: assertion 'GDK_IS_DISPLAY (display)' failed

(3-1_abnormal_check.py:1546): Gdk-CRITICAL **: 06:16:05.340: gdk_cursor_new_for_display: assertion 'GDK_IS_DISPLAY (display)' failed
```

### 解决办法
这个错误的原因在于ssh连接服务器时候，import pyplot因为没有图形界面所导致的故障，解决的方法很简单，直接在ssh连接服务器的时候，添加-X的标记：

ssh 192.168.0.1 -X
就可以搞定了。当然还有另外一种解决的方法：在import pyplot之前，加入

matplotlib.use("Pdf") 

<hr>
### Ubuntu
### 创建用户
1. sudo passwd root
2. sudo adduser linuxidc
3. E: Could not get lock /var/lib/dpkg/lock - open (11: Resource temporarily unavailable)
E: Unable to lock the administration directory (/var/lib/dpkg/), is another process using it?  
看提示：被锁了。使用
	1. 找到并且杀掉所有的apt-get 和apt进程
		- ps -A | grep apt
		- sudo kill -9 processnumber
	2. 删除锁定文件
		- sudo rm /var/lib/dpkg/lock
		- sudo dpkg --configure -a（强制重新配置软件包）
4. sudo vim /etc/sudoers（让此用户有root权限）
	- # User privilege specification  
root ALL=(ALL) ALL  
linuxidc ALL=(ALL) ALL
5. 查看用户列表cat /etc/passwd
6. 删除用户sudo userdel -r newuser

### 查看文件
1. 文件类型file、stat

### SSH 
1. 查看是否安装了SSH服务：sudo ps -e | grep ssh

2. 如果不存在sshd服务则是没安装：sudo apt-get install openssh-server

### Ubuntu 18.04 安装 Docker-ce
1. 更换国内软件源，推荐中国科技大学的源，稳定速度快（可选）

sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
sudo sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
sudo apt update

2. 安装需要的包

sudo apt install apt-transport-https ca-certificates software-properties-common curl

3. 添加 GPG 密钥，并添加 Docker-ce 软件源，这里还是以中国科技大学的 Docker-ce 源为例

curl -fsSL https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu \
$(lsb_release -cs) stable"

4. 添加成功后更新软件包缓存

sudo apt update

5. 安装 Docker-ce

sudo apt install docker-ce

6. 设置开机自启动并启动 Docker-ce（安装成功后默认已设置并启动，可忽略）

sudo systemctl enable docker
sudo systemctl start docker

7. 测试运行

sudo docker run hello-world

8. 添加当前用户到 docker 用户组，可以不用 sudo 运行 docker（可选）

sudo groupadd docker
sudo usermod -aG docker $USER

9. 测试添加用户组（可选）

docker run hello-world