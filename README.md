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
+ 如果用自己的芯片实现的底层，越到上面效率越可能爆炸。抛开实现的正确与否，模拟器不可能真正模拟硬件的并行等特性，所以如果不用内置好的算法，效率越到后面就会越慢。（不过还是让人很有冲动尝试下啊）
+ 实现了一个helper chip，Extendx系列。效果是将真值扩展为x位。如Extend16，输入为1个bit，值1，输出16个bit，每个都是1。（从实现上，取反要更简单，这也就是为什么要用Nand吧）
+ 应该如何正确地实现if的效果？？而不是把结果都算出来然后Mux。
+ 可以直接在命令行里运行测试，比图形界面快很多
+ internal pin是不能用sub_bus的，导致使用Or8Way的时候非常麻烦，所以又弄了一个Or16Way chip。
+ 如何从一个16bit中选择一位的值？Simulator不允许使用内部变量的sub_bus，也不能将外部输出进一步用于运算，导致这个问题变得非常麻烦。不过当然可能是我没想到好办法。



## 2020-09-29（第三周）

上课笔记：

+ __TOC__改变目录在的位置
+ 使用Ref
+ quoteinvestigator
+ TLA+
+ 时间与空间
+ Logic Model

## 2020-10-04

+ 根据上课与老师和同学的讨论，改进了第二周的Chip实现
+ 一上来转换成有时间概念的Chip有点不习惯。不过其实原理还是接线，把图画明白了编码是一样的。
+ 完成了第三周的Chip
+ 第十二周的Sys看了看，但是没什么头绪，不知道怎么下手。。可能需要先看下11周和12周的视频


## 2020-10-07

+ [Hyper Threading Explained](https://www.youtube.com/watch?v=lrT9Bl0MCXQ): Intel提出的概念，可以虚拟两倍的核。操作系统对任务进行负载均衡。提高pipeline的效率。在计算密集且任务可分解的情况下效果很好。
+ [AMD CPU发展史](https://www.youtube.com/watch?v=CHERD3gVF98): CPU设计要不断进行trade off。性能与能耗的权衡、CPU和显卡的平衡、核数和频率等等。最后AMD真是一家神奇的公司。

## 2020-10-08
+ 完成了Week4的作业：虽然一开始写起来不是很习惯，但是后来就觉得很爽了。以及深刻地感受到了一旦代码逻辑变复杂之后汇编是多么地不利于维护


## 2020-10-13
上课笔记：
+ 量子计算
+ CAPTCHA
+ Agent based architectures
+ Net logo
+ Q bit, Quantum Terminology
+ kframework
+ Paxos
+ Raft
+ Symmetry/Symmetry-breaking



















