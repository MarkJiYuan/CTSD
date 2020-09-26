# CTSD
Computational Thinking &amp; System Design



## 2020-09-27

+ 完成Coursera第一周的课程

+ 需要修改权限才能运行脚本，之后可以创建软链接

  ~~~bash
  chmod +x HardwareSimulator.sh
  ~~~

+ 最大的坑：如果同一个文件夹里已经有Chip的话，会加载同一个文件夹里的Chip，而不是内置的Chip。所以我运行projects/demo/Xor.hdl没有问题，可是projects/01/Xor.hdl就会错。原因是因为01/Xor.hdl里面用了And，Or，Not，而这些当时还没被实现。demo里的能行得通因为调用了tools/builtinchips里面的。

  