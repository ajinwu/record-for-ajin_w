<!--
 * Author       : ajin
 * Date         : 2020-04-03 13:09:21
 * Description  : 
 * email        : ajin_w@163.com
 * 那曾梦想屠龙的少年，终会变成油腻的中年大叔，端坐于显示器前，从指尖流淌的代码，终会改变整个世界
 -->

## overview
grpc中, 客户端可以像使用本地对象一样, 直接调用其他机器上面的服务端应用程序方法, 能够很容易的构建分布式的应用程序和服务, grpc基于服务, 指定能够调用远程方法的参数和返回值, 在服务端, 服务实现接口并运行grpc服务去处理客户端调用, 在客户端, 客户端有一个stub(客户机), 提供和服务端相同的方法

![调用图](https://grpc.io/img/landing-2.svg)

grpc客户端和服务端可以在各种环境中运行并支持各种语言, 举个例子, 你可以使用服务端语言为Java, 客户端语言为python

## Protocol buffers
默认的, grpc使用Protocol buffers, Google成熟的开源序列结构化数据方式

第一步是在*proto*文件中定义你想序列化的结构化数据, 这是一个使用**proto**作为扩展名的文本文件, Protocol buffers数据结构为*message*;每一个message是一个小的包含一系列name-value组的可调用字段的逻辑记录,举个例子

```
message Person {
  string name = 1;
  int32 id = 2;
  bool has_ponycopter = 3;
}
```

接下来, 你需要指定你的数据结构, 你可以通过你的proto定义在你喜欢的语言中使用协议缓冲区编译proto文件去生成数据权限接口, 他提供了一个简单的存取访问, 例如 *name()*, *set_name()*, 以及一个从原始数据/序列化数据进行序列化/反序列化的方法, 你可以在你的应用中填充生成的class

你可以在普通文件中定义rpc服务, 并指定rpc方法参数和返回值类型

```
// The greeter service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings
message HelloReply {
  string message = 1;
}
```

grpc使用protoc指定grpc插件从你的proto文件中去生成代码, 你可以生成客户端和服务端代码, 他提供常用的protocol buffer代码去填充, 系列化, 返回消息类型