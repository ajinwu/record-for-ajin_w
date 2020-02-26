# 概述
1. namenode:存储文件元数据,文件名,文件目录结构,文件属性(生成时间,副本数,文件权限等)以及每个文件的块列表和块所在的datanode等
2. datanode:在本地文件系统存储文件块数据,以及块数据的校验和
3. secondary namenode:用来监控HDFS的状态的辅助后台程序,每隔一段时间获取HDFS元数据的快照

# HDFS写数据流程()

# namenode故障处理
1. 将SecondaryNameNode中数据拷贝到NameNode存储数据的目录
2. 使用-importCheckpoint选项启动NameNode守护进程，从而将SecondaryNameNode中数据拷贝到NameNode目录中。

# 安全模式
1. 集群在启动namenode时会进入安全模式,加载fsimage和edits时不能进行写操作
2. 在安全模式下datanode会向namenode上报块信息
3. 安全模式会在满足最小副本条件,即99%的块副本数大于1
4. 安全模式查看`bin/hdfs dfsadmin -safemode get	`

# maptask并行度机制
1. 一个job的并行度由客户端在提交job时的切片决定
2. 每一个切片分配一个maptask处理
3. 默认情况下切片大小等于blocksize
4. 切片时不考虑整体,而是按照单个文件进行

Filesplit获取切片信息(主要为文件名)

CombineTextInputFormat应用于小文件较多的场景下,可以将多个小文件逻辑划分为单个切片,在Driver直接设置(先设置InputFormat为本类)

# FileInputFormat实现类
1. TextInputFormat是默认的实现类,按行读取数据,key为偏移量,v为content
2. keyValueInputFormat,可以使用分隔符来进行区分
3. NLineInputformat,不按照块大小来切分,按照指定的行数来切分,输入文件的总行数/N=切片数，如果不整除，切片数=商+1

# partition分区
1. 分区的数量表示去往哪个reducetask,reducetask数量是手动设置的
2. 分区和排序是两个过程,每个分区区内有序

# 排序实现在bean内
CompareTO方法重写,继承自WritableComparable

# Combiner合并
1. Combiner的父类是reduce
2. Combiner在每个maptask结点运行
3. 进行的是局部汇总,不能影响全局数据

# GroupingComparator辅助排序
1. 自定义继承自WritableComparator