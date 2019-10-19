# 获取docker镜像
- 获取镜像
    - docker pull ubuntu:18.10  下载镜像
        - 默认不填版本号会选最新版本的，即latest，默认使用官方镜像
        - 非官方镜像下载 
            > docker pull hub.c.163.com/public/centos:6.5
        - pull 参数
            - -a，    --all表示获取所有镜像，默认为否


    - 查看镜像
        - docker images列出镜像
            - images参数
                - -a，    列出所有镜像
                - -f ，   列出过滤的镜像，例如列出没有被使用的镜像
                    >docker images -f dangling=true
        - docker tag ubuntu:latest ajinwu:test给镜像起别名，类似于软链接
        - docker inspect web列出web这个容器的详细信息(注意，并不是镜像名)
            - -f参数
                >docker inspect -f {{".Networks"}} web  显示web容器的网络信息
        - docker history ajinwu:test列出镜像的创建过程
            >docker history --no-trunc ajinwu:test  显示截断的信息


    - 搜寻镜像
        - docker search [option] keyword
            - -f    过滤输出内容
                > docker search -f=is-official=true nginx   查找镜像，官方给出的带有nginx的镜像
            - --limit int 限制输出内容
                > docker search --limit=3 nginx         显示前三条结果
    

    - 清理镜像
        - docker rmi ubuntu:18.10       删除镜像标签为18.10的ubuntu镜像
        - -f强制删除，即使有容器依赖
        - docker ps -a  列出本机用过的所有容器
        - 先删除容器在删除镜像
            > docker rm [CONTAINER ID]  删除镜像
            > docker rmi -f ajinwu/commit_test1:latest  强制删除镜像
            > docker images prune -f 自动清除遗留文件层
    

    - 创建镜像
        - docker commit -m "add a new file" -a "docker ajin" c57 ajinwu/commit_test     制作一个新镜像，信息为add  file，作者信息为docker  ajin，容器id为c57开头,仓库名为ajinwu/,镜像名为commit_test 的新镜像
        - 还可以添加-p暂停容器的运行
        - 可以使用openVZ提供的模板来创建镜像
            - cat ubuntu-18.04-x86_64.tar.gz | docker import - ubuntu:18.04
        - dockerfile构建镜像
            - docker build -t="ajinwu/dockerfile" .     -t参数为镜像名，后面加上dockerfile的目录
    

    - 存出镜像和载入镜像
        - 存出镜像 docker save -o ubuntu_commit.tar ajinwu/commit_test
        - 载入镜像  docker load < ubuntu_commit.tar
        - 上传镜像
            - 先修改标签，格式为用户ID/镜像名docker tag test:test ajinwu/test
            - 上传  docker push ajinwu/test


- 操作容器
    - 创建容器
        - docker create -it ajinwu:test创建一个容器不运行
        - docker run -it ajinwu:test /bin/bash 使用ajinwu:test镜像创建一个容器并开启交互式终端使用/bin/bash
        - docker run -p 8111:80 --name nginx -i -t ubuntu /bin/bash     创建一个容器名为nginx的容器，将本地的8111端口映射到容器的80端口，可使用容器的地址直接访问
        - 常用参数说明
            - -i    保持标准输入输出打开
            - -t    分配伪终端
            - -d    是否后台运行，默认为否
            - --net="bridge"    开启桥接网络
            - --expose      暴露端口
            - -p映射端口 -p

        - 开启容器docker start 042  注意，只能使用id
        - docker run ubuntu /bin/echo "hello wolrd"
            - 检查本地是否有ubuntu镜像
            - 利用镜像创建一个容器，并启动该容器
            - 分配一个文件系统给容器，并在只读镜像层外面挂载一层可读写层
            - 从宿主主机的配置的网桥接口中桥接一个虚拟接口到容器
            - 从网桥的地址池配置一个ip给容器
            - 执行用户指定的应用程序
            - 执行完命令容器被自动终止
        - 查看容器输出
            - >docker logs  -f -t  --tail 10 test       查看最后10条并持续输出显示时间

    - 停止容器
        - docker run --name=ajin2 -it --rm ubuntu bash运行一个容器，命名为ajin2，交互式伪终端运行bash，运行结束后删除该容器
        - Ctrl +p    Ctrl+q 后台运行容器，不停止容器的退出
        - docker pause ajin2 暂停容器ajin2
        - docker stop ajin2 终止容器ajin2
        - docker ps 查看容器
            - -l    查看正在运行的容器
            - -a    查看所有容器
            - -qa   只查看所有容器的id
        - docker restart 042    重启容器
    - 进入容器
        - docker attach 042  进入后台容器
        - docker exec -it 042 bash  推荐这种方式，在不影响运行应用的情况下开启一个新的bash
    - docker rm -f 042      强行删除容器（不建议）

    - 导入和导出容器
        - 导出容器
            - docker export -o test_export.tar 4ac
        - 导入容器
            - docker import test_export.tar - test/ubuntu:v11这命令我不知道为啥错了
    
    - 查看容器
        - docker top 4ac       查看运行中的容器进程
        - docker stats 4ac  类似与htop命令
        - docker inspect 4ac    查看容器信息
    
    - 其他容器命令
        - 复制文件docker cp dp_2.py 4ac:/tmp，复制本机的文件到容器的tmp下
        - 反向赋值docker cp 4ac:/test.txt .
        - docker  diff 4ac     查看容器数据修改
        - docker container port d8  查看端口映射
# 访问docker仓库
- 各大镜像仓库
    - 阿里云，网易云，腾讯云docker pull  url
- 搭建本地私有仓库，大家自行学习

# docker数据管理
- 数据卷
    - docker volume create -d local test 会在宿主机/var/lib/docker/volumes下创建一个test数据卷
    - 绑定数据卷
        docker run -it -p 80 --name=blog -v /home/ajin_w/blogbak:/home/ajin_w/blog ubuntu /bin/bash     此命令为开启一个名为blog的容器，-v参数为映射本地文件夹blogbak目录到容器blog下，映射目录相当于一个网络驱动器，容器内外的修改均会生效，可在映射结束的位置添加读写权限，例如ro
        
- 数据容器
    - 数据容器的创建使得挂载该数据容器的容器间可以很方便的进行数据交换
    - 创建数据容器
        - docker run -it -v /dbdata --name dbdata ubuntu
    - 挂载数据容器
        - docker run -it --volumes-from dbdata --name db1 ubuntu
    - 数据容器不需要保持在运行状态
    - 删除数据卷必须在最后一个挂载他的容器显式使用docker rm -v命令来指定同时删除关联的容器
    - 数据迁移
        - docker run --volumes-from dbdata -v $(pwd):/backup --name worker ubuntu tar -cvf /backup/backup.tar /dbdata
        - 以上命令解释：创建一个worker容器，挂载dbdata数据卷，使用-v参数挂载本地当前目录到worker的容器的backup目录，容器启动后，打包dbdata为容器的/backup/backup.tar，即宿主机的当前目录下的backup.tar      意思就是挂载两个数据卷，一个本地目录，一个数据卷或者数据容器，将容器内的数据卷打包到容器的backup目录，因为直接挂载数据卷在/目录下，在挂载一个目录，将/目录下的数据卷打包进backup就好，本地目录变成了backup

    - 数据恢复
        - docker run -v /dbdata --name dbdata2 ubuntu /bin/bash 
        - 创建一个容器挂载dbdata数据卷，名为dbdata2
        - docker run --volumes-from dbdata2 -v $(pwd):/backup ubuntu tar xvf /backup/backup.tar 
        - 创建另一份容器挂载dbdata2和当前目录到/backup目录，将本地的目录解压



