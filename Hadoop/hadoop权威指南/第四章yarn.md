<!--
 * Author       : ajin
 * Date         : 2020-02-26 12:17:17
 * Description  : 
 * email        : ajin_w@163.com
 * ajin是最好的人啦
 -->


## yarn的优点
1. yarn作为资源管理器和调度器, 在产生每一个作业任务都会生成一个application master, 管理作业的运行, 进行了解耦, 提高了可扩展性
2. yarn中的每个node manager管理着资源池,完成了资源复用

## yarn调度
1. FIFO调度器, 容量调度器, 公平调度器
2. 实际生产中应该是相互配合使用来提交集群利用率