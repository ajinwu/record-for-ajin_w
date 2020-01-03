## for/else 当for循环结束(没有被break终止的时候)运行else模块
## while/else 当while条件为假退出(未被break)
## try/else 没有异常运行
## 上下文管理器协议包含enter和exit两个方法, with语句运行时, 会在上下文管理器对象上调用enter方法, 在With结束后, 调用exit方法
## 执行with后面的表达式得到的结果是上下文管理器对象, 不过, 把值绑定到目标变量上(as子句)是在上下文管理器对象上调用enter方法
## 解释器调用enter方法是, 除了隐式的self之外, 不会传入任何参数

## contextlib模块
1. closing, 如果对象提供了close方法, 但没有实现enter和exit协议, 可以使用这个
2. suppress, 构建临时忽略指定异常的上下文管理器
3. contextmanager, 将简单的生成器函数变成上下文管理器  
   1. 不用编写完成的类定义enter和exit, 只需要实现yield语句的生成器, 生成enter返回的值
   2. yield语句前面的所有的代码在With模块开始(即调用enter方法)执行, yield之后的代码在With结束时(exit)执行
4. contextDecorator, 用于定义基于类的上下文管理器
5. exitstack, 这个上下文管理器能进入多个上下文管理器
