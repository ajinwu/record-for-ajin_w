<!--
 * Author       : ajin
 * Date         : 2020-04-03 13:51:11
 * Description  : 
 * email        : ajin_w@163.com
 * 那曾梦想屠龙的少年，终会变成油腻的中年大叔，端坐于显示器前，从指尖流淌的代码，终会改变整个世界
 -->

## 什么是protocol buffers?
protocol buffers是一个灵活的, 高性能的, 自动化的数据结构序列化机制, 就像xml, 但是更小, 更快, 更简单, 你可以定义你想要的数据结构, 然后使用特定的代码生成工具生成代码去从不同的数据流中使用不同的语言读写你的结构化数据, 你也可以从老的数据结构中更新你的数据结构

## 如何工作
你可以通过定义proto文件定义protocol buffers类型来指定你想序列化的数据, 每一个protocol buffers是一个小的逻辑记录消息, 包含name-value对, 这是一个例子, 包含了定义person的信息

```
message Person {
  required string name = 1;
  required int32 id = 2;
  optional string email = 3;

  enum PhoneType {
    MOBILE = 0;
    HOME = 1;
    WORK = 2;
  }

  message PhoneNumber {
    required string number = 1;
    optional PhoneType type = 2 [default = HOME];
  }

  repeated PhoneNumber phone = 4;
}
```

就像你看到的一样, 这个message格式非常简单, 每一个message类型有一个或多个唯一的字段, 每一个字段都有name类型和value, value的类型有数字(integer or floating-point), booleans, strings, raw bytes和一些其他的类型, 允许数据结构的层级排列, 你也可以指定其他的字段,  required fields, 和repeated fields.更多参考在[字段参考](https://developers.google.com/protocol-buffers/docs/proto)

第一次定义你的message, 你可以通过proto文件运行protocol buffer编译到你的程序语言来生成数据访问类

你也可以添加新的格式化字段在你的message中, 解析的时候旧的二进制文件将会被忽略, 使用新的二进制字段来使用, 如果你有一个proto文件, 你可以扩展你存在你的字段而不用担心被破坏

## 为什么不适用xml
Protocol buffers有比xml更多高级的序列化能力

1. 更简单
2. 比xml小3-10倍
3. 比xml快20-100倍
4. 不太模糊
5. 更容易生成用户使用的数据访问类

当message被编码成Protocol buffer二进制格式化文件(原先的proto文件只是人类可读的形式来用于调试编辑), 比xml有更小的文件长度和更快地解析

然而, Protocol buffers不会总是优于xml, 举个例子, Protocol buffers 在HTML文档中不能读, 另外xml是人类可读可编辑的, Protocol buffers 只能定义在proto文件中

## 开始使用
[下载地址](https://developers.google.com/protocol-buffers/docs/downloads), 通过文档来编译安装

## proto3
在proto3中引入新的语言版本, 添加了一些新的feature, proto3简化了Protocol buffers语言, 既可以方便使用, 又可以在很多编程语言中使用, 支持语言(Java, C++, Python, Java Lite, Ruby, JavaScript, Objective-C, and C#, Go proto plugin)

proto2和3并不完全兼容

## 历史
Protocol buffers要解决的问题

1. 方便引入新字段, 不需要检查数据的中间服务器可以简单解析数据并传递数据, 不需要知道所有的字段
2. 格式是自描述的, 能够使用多种语言来处理

特性和用途

1. 自动生成序列化/反序列化代码, 不需要手动解析
2. 除了使用短时间的rpc, 还可以永久存储数据(bigtable)
3. 服务器rpc接口开始被声明为协议文件的一部分, protocol编译器能够生成stub类, 用户可以在实现服务端的接口覆盖他们