# Docker
1. docker隔离的东西(linux namespace+chroot)
   - UTS(主机名和域名)
   - User(用户)
   - Mount挂载点(文件系统)
   - IPC(信号量, 消息队列, 共享队列)
   - Pid(进程编号)
   - Network(网络)
2. Control Groups(控制组)
3. LinuX Container(LXC)的增强版是docker
4. 镜像:静态=>进程
5. 容器:生命周期=>程序  


# docker挂载机制
1. 采用分层挂载机制, 最底层为bootfs, 其次为rootfs
   1. bootfs:用于系统引导的文件系统, 包括bootloader和kernel, 容器启动后会被卸载以节约内存资源
   2. rootfs:位于bootfs之上, 表现为容器的根文件系统
      1. 传统模式中, 系统启动之时.内核会挂载rootfs时会首先将其挂载为只读模式, 完整性自检完成后将其重新挂载为读写模式
      2. docker中, rootfs有内核挂载为只读模式, 而后通过联合挂载技术额外挂载一个可写层
   3.  > 联合挂载的意思是自下往上依次挂载
   4.  > 每一个功能都是一个image(镜像)
   5. 位于最下层的镜像称为父镜像, 最底层的称为基础镜像
   6. 最上层的为可写层, 其下的均为只读层



# docker 虚拟网络
1. 在宿主机上建立一个桥接网卡docker0, brctl show显示桥接网卡绑定方式
2. 将docker0的网卡作为一条网线,一般在宿主机docker0上,一般在docker容器中
3. docker0是一个nat桥,iptables -t nat -vnL, 可以看见postrouting规则, 所有进入的流量, 只要不是从docker0桥出去的流量, 原地址来自172.17.0.0/16,无论到达任何主机, 都要进行地址伪装
4. docker四种网络模式
   1. none, 批处理文件所用, 挂载本地卷, docker run -it --name b1 --network none --rm busybox
   2. bridge网络, nat桥接docker0,default模式, docker run -it --name b1 --network bridge --rm busybox
   3. 共享同一个网络, IPC, pid模式, 网络对于多个容器可见
   4. 桥接物理网卡
5. 创建网络命名空间并实现网卡互联
   1. ip netns add r1创建一个网络名称空间r1
   2. ip netns list 列出名称空间的网卡
   3. ip netns exec r1 ifconfig -a进入名称空间r1执行ifconfig命令
   4. ip link add name veth1.1 type veth peer name veth1.2添加一块类型为veth的虚拟网卡veth1.1,另一半网卡名veth1.2
   5. ip link show 显示两块网卡连接状态
   6. ip link set dev veth1.2 netns r1,将veth1.2网卡迁移到r1名称空间
   7. ip netns exec r1 ip link set dev veth1.2 name eth0进入r1名称空间,并设置设备veth1.2的网卡名为eth0
   8. ip netns exec r1 ifconfig eth0 10.1.0.1/24 up,将eth0网卡开启并设置ip为10.1.0.1,24位掩码
   9. ip link set dev veth1.1 netns r2,将veth1.1网卡迁移到r2名称空间
   10. ip netns exec r2 ip link set dev veth1.1 name eth0,设置网卡名称
   11. ip netns exec r2 ifconfig eth0 10.1.0.2/24 up, 设置ip并开启网卡
   12. ip netns exec r1 ping 10.1.0.2测试网络连通性

# docker容器注入
1. 注入容器中主机名, docker run -it --name b1 --network bridge -h test --rm busybox
2. 注入dns服务器, docker run -it --name b1 --network bridge -h test --dns 114.114.114.114 --rm busybox
3. 注入host, docker run -it --name b1 --network bridge -h test --dns 114.114.114.114 --add-host www.baidu.com:192.168.0.148 --rm busybox

# docker 端口映射
1. docker run -d --name b1 --rm -p 80 ajinwu/httpd:v1.1
2. docker run -d --name b1 --rm -p 192.168.0.148::80 ajinwu/httpd:v1.1
3. docker run -d --name b1 --rm -p 192.168.0.148:80:80 ajinwu/httpd:v1.1
4. docker run -d --name b1 --rm -p 80:80 ajinwu/httpd:v1.1
5. 自动暴露使用大写的p

# 联盟式容器 
1. docker run -it --name b2 --network container:b1 --rm busybox, 共享b1的网络名称空间, 但是文件系统也是隔离的
2. docker run -it --name b1 --network host --rm busybox, 共享主机的网络
3. docker远程连接机器控制docker, 按照官方文档, 修改docker.service文件可行, ubuntu19.04修改daemon.json文件无效, 原因未知


# 自己创建网络
1. docker network create -d bridge --subnet "172.26.0.0/16" --gateway "172.26.0.1" mybr0, 创建网络mybr0,方式为桥接,子网为172.26.0.0, 网关如上


# 数据卷的必要性
1. 关闭并重启容器, 其数据不受影响, 但是删除docker容器, 其更改会消失
2. 存在的问题
   1. 存储在联合文件系统中, 不易于宿主机访问
   2. 容器间数据共享不方便
   3. 删除数据数据会丢失
3. 解决方案:卷
   1. 卷是容器上的一个或多个目录, 此类目录会绕过联合文件系统, 与宿主机上的某目录绑定关联
4. docker run --name b1 -it -v /data busybox, docker自己管理的绑定卷, 使用inspect可以查看挂载地址
5. docker run --name b1 -it -v /home/ajin_w/docker/volumes:/data --rm busybox, 挂载本地卷存放数据, 不存在会默认创建, 双向创建
6. 容器间共享数据:使用挂载卷, 两个容器使用同一个挂载卷
7. 复制一个容器已存在的卷
   1. docker run --name infracon -it -v /home/ajin_w/docker/volumes/infracon:/data/web/html busybox, 创建一个基础容器, 可以不用交互式, 也可以不用启动, 但是不能删除, 只提供给其他容器复制
   2. docker run --name nginx --network container:infracon --volumes-from infracon -it --rm busybox, 创建一个nginx容器, 继承infracon容器的网络, 存储卷也使用infracon相同的配置


# docker信息查询
1. docker inspect b1 -f {{.NetworkSettings.IPAddress}}, 使用json层级读取数据

# dockerfile制作
1. 指令格式format
   1. comment, 注释信息
   2. 指令和指令参数
2. 指令本身不区分字符大小写, 约定俗称使用大写
3. docker运行自上而下
4. 第一个非注释行一定是以from开头
5. dockerfile文件首字母一定要大写
6. 打包文件一定要在本目录以及本目录之下
7. FROM格式, FROM <repository>[:tag] 或者FROM <repository>@<digest> digest为哈希码, 不会被冒名顶替
8. COPY, 将本机的文件复制到镜像, 源文件一般为相对与dockerfile文件目录, 目标文件一般为镜像中的绝对路径
   1. 复制目录目录本身不会被复制, 只会递归复制目录下的文件
   2. 必须以/结尾
9. ADD, 语法和COPY相同, 可以加上url, 会自动下载文件, 本地打包文件会自动解压
10. WORKDIR, 制定工作目录
11. VOLUME, 指定挂载卷, 只能指定容器内的, 容器外只能使用默认的
12. EXPOSE, 为容器打开指定要监听的端口与外部通信, 在dockerfile中写入只是会作为待暴露的端口, 而不是直接暴露, 加上P会暴露
13. ENV <key>=<value> ...value中含有空白字符等需要使用反斜杠转义, 或者引号转义, 反斜线也可以进行续行
14. RUN, 正常写linux操作命令, 必须是基础镜像有的命令, 在docker build的时候执行
    1. 作为shell的子进程来运行, 以"/bin/bash -c"来运行, 此进程pid不为1, 不能接受unix信号, 因此, docker stop无法停止容器
    2. RUN ["<executable>", "param"]格式的命令不以"bash"运行, 因此shell常见操作不会进行(通配符))
    3. 依赖shell特性可RUN["bin/bash", "-c", "executable", "param"]信号也不是1
15. CMD, 类似与RUN指令, 定义一个镜像文件启动为容器时默认要运行的程序, 只能出现一个CMD, CMD指令可以被dockerfile命令选项覆盖
    1.  CMD <commend> pid不为1,可以使用shell命令
    2. CMD["executable","param"]创建的是pid为1的进程, 这里不能默认启动shell, 可以手动运行为shell子进程
    3. CMD ["param"]结合entrypoint来运行
16. ENTRYPOINT命令不会被覆盖, 也不允许被覆盖, 多余输入的命令会被当做参数传入, 可以在启动容器时修改entrypoint命令
    1.  如果CMD和ENTRYPOINT同时使用, 则CMD的命令会被当做参数传入ENTRYPOINT
17. docker参数-e, 设置环境变量
18. shell命令, exec顶替上一个进程, "$@", 后面任意长度字段的作为参数, exec "$@", 顶替当前进程, 然后将后面的命令传入当做下一个程序执行
19. HEALTHCHECK健康监测
    1. HEALTHCHECK --interval=duration(default:30s), 检测周期
    2. --timeout=duration(default:30s)超时时间
    3. --start-period=duration(default:0s), 容器启动多少秒开始检测
    4. --retries=N (default:3), 检测次数
    5. example===> HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost/ || exit 1
20. ONBUILD触发器命令, 在别人使用你的镜像时会执行这个命令, 后门


# docker 仓库
1. apt install docker-registry
2. insecure-registries
3. vmrare harbor


# docker 资源限制
1. linux 通过内核来管理资源调度, 使用内存计算算法来管理, oom-score最高的会被最先杀死, 重要应用应使用oom_obj来分配权重
2. 内存限制
   1. --momery内存不应该大于主机内存
   2. --momery-swap为交换空间, 不设置memory则无法设置此选项
      1. -m-s为正数S, m为正数M, 容器总空间为S, 其中ram为M, swap为(S-M), 如S=M, 则无可用swap资源
      2. 0, M, 相当于未设置swap(unset)
      3. unset, M, 若主机弃用了swap, 容器可用swap为2*M
      4. -1, M, 若主机弃用了swap, 容器可使用最大主机swap资源
   3. --oom-kill-disable, 禁止kill
3. cpu限制
   1. 默认可使用所有的cpu
   2. cpu可压缩, 共享式cpu-shares共享, 按照比例切分, 不用的时候cpu可以尽可能共享给他人, 使用的时候按比例给他最大的, 然后检查其他进程cpu资源是否空闲, 空闲可继续使用
   3. --cpus=1.5, 显示cpu最多使用几核, 可使用小数
   4. --cpuset-cpus, 限制使用的cpu是哪几个, 不建议使用
4.  docker run --name stress -it --rm -m 256m lorel/docker-stress-ng stress --vm 2, 验证memory限制, docker stats显示详细信息
5.  docker run --name stress -it --rm --cpus 2 lorel/docker-stress-ng stress --cpu 8, cpu压测
6.  docker run --name stress -it --rm --cpu-shares 1024 lorel/docker-stress-ng stress --cpu 8, 共享式分配, 首先会占用完cpu, 然后再来一个容器会互相分配