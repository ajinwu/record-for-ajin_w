<!--
 * Author       : ajin
 * Date         : 2020-02-25 15:44:15
 * Description  : 
 * email        : ajin_w@163.com
 * ajin是最好的人啦
 -->
## 数据流
1. 分片,通过将一个数据集进行分片操作, 并行处理每一个分片,则整个处理过程会更好的负担
2. map的输出写入到磁盘,中间结果是可以丢弃的
3. combine, 相当于一个reduce的操作,但是combine的操作不能影响最后结果
4. 通过管线操作能使用更多的语言来实现Hadoop mapreduce操作