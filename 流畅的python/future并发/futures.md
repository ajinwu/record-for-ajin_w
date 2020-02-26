1. 实例化ThreadPoolExecutor类, executor的exit方法会调用shutdown方法, 在所有线程结束前阻塞线程
2. future的submit返回一个可调用对象
3. future都有done方法, 不阻塞
4. result方法在future结束后调用, 返回对象的结果, 会阻塞
5. as_completed的参数是一个future列表, 返回值是一个迭代器, 在运行结束后产出future
6. cpu密集型使用多进程, IO密集型使用多线程
   