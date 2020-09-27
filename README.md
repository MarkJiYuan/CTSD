# CTSD
Computational Thinking &amp; System Design



## 2020-09-27

+ 完成Coursera第一周的课程

+ 需要修改权限才能运行脚本，之后可以创建软链接

  ~~~bash
  chmod +x HardwareSimulator.sh
  ~~~

+ 最大的坑：如果同一个文件夹里已经有Chip的话，会加载同一个文件夹里的Chip，而不是内置的Chip。所以我运行projects/demo/Xor.hdl没有问题，可是projects/01/Xor.hdl就会错。原因是因为01/Xor.hdl里面用了And，Or，Not，而这些当时还没被实现。demo里的能行得通因为调用了tools/builtinchips里面的。




## 2020-09-28

+ 不同的chip的实现，结果非常的不同。如何能化简为最简形式呢？
+ true和false可以自己改变长度，但是一个普通的01没法扩展到相应的位数。在Mux8Way16中就很麻烦，需要挨个给输入的16位的变量赋值。（应该有什么简写的方法）
+ 写到后来就跟函数调用感觉差不多了。但是让人隐约觉得可以化简，这样直接去套得到的性能很不放心。（真实的计算机组成的话，要考虑每个门的延迟时间。如果是这种串行的方法，机器的主频根本上不去）
+ 还是挺好玩的，真的挺有创造的感觉。这个一遍过的感觉比高级语言调包激动多了。