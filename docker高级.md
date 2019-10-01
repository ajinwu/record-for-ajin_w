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