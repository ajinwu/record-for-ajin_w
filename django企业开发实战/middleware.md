# 中间件的顺序问题
在请求阶段, 调用视图之前, django按照定义的顺序执行中间件, 自顶向下, 返回响应是以相反的顺序通过每一个中间件层, 最终返回给用户, 如果某一层认为当前响应请求需要被拒绝, 或者发生错误, 直接回了一个响应, 那么剩下的中间件以及核心函数都不回被执行

中间件调用顺序时机

钩子函数|执行时间|执行顺序|返回值
---|---|---|---
process_request|请求到来,执行视图之前|按照配置顺序|NOne或者HttpResponse对象
process_response|视图执行完毕, 返回响应时|逆序|HttpResponse对象
process_view|process_request之后, 路由转发到视图, 执行视图之前|正序|None或者HttpResponse对象
process_exception|视图执行中发生异常|逆序|NOne或者HttpResponse对象
process_template_response|视图刚执行完毕, process_response之前|逆序|实现了render方法的响应对象


1. process_request(request), 只有一个request参数, 返回值如果为None表示一切正常, 继续往下, 交给下一个中间件处理, 返回HttpResponse对象, 发生短路不继续执行后面的中间件, 也不执行视图函数, 而是将响应返回给浏览器
2. process_response(request, response), response是视图函数返回的HttpResponse对象, 该方法返回值必须是一个HttpResponse对象, 不能是None
3. process_view(request, view_func, view_args, view_kwargs), view_func: 真正的业务逻辑处理函数, 不是函数的字符串名称, 在django调用真正的业务视图之前执行, 并且以正序执行, 返回None或者HttpResponse
4. process_exception(request, exception), 错误处理模块, 返回None或者HttpResponse
5. process_template_response(request, reesponse), 正常情况下一个视图执行完毕, 会渲染一个模板, 作为响应返回给用户, 使用此方法, 可以重新处理渲染末班的过程, 添加业务逻辑

一旦一个中间件返回了一个HttpResponse对象, 立刻进入响应流程, 是短路操作

# 官方推荐方法
get_response是一个实际视图, 代表了下一个要进行的操作, 可以编写这些方法, 也可以将将具体操作放在call里面