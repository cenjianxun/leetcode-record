'''
1114. Print in Order

Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.


Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
'''

'''
题目意思是，按顺序执行这三个函数。
但是在多线程里，函数之间执行的顺序是不确定的。

https://blog.csdn.net/u010701274/article/details/122861891?spm=1001.2014.3001.5502

以下皆是copy
'''

'''
① lock （互斥）锁
互斥锁为资源引入一个状态：锁定/非锁定。某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性


- 锁对象（Lock）具有获取和释放两种状态，创建时处于释放状态。
- 默认创建的Lock具有阻塞作用，当Lock为一线程获取后，其他线程（包括其自身）若获取该锁，则线程阻止，不能往下运行，直到该锁释放。
- 若其他线程（包括自身）不获取该锁，则不发生阻塞作用，即阻塞作用发生在线程获取处于锁定状态的锁。
- 线程获取后的锁不一定必须释放，但若不释放，其他线程获取该锁时则发生死锁，程序假死。
- 每个线程会去acquire锁，如果这个锁被其他线程获取了，则acquire失败。但是，一个线程获得的锁，可以由其他线程进行释放！

有三个步骤：
mutex = threading.Lock() #创建锁
mutex.acquire([超时时间]) #锁定
mutex.release() #释放

在阅读顺序acquire()和release()之间的函数会被锁住

思路是： 
初始化类时先锁两个锁，这时子线程一直无法获得锁，就一直阻塞，直到first运行了释放锁1，才继续
first:不需要获取锁，直接run，然后释放第一个锁
second：第一个锁被释放了，所以second可以获取到，获取后run，然后释放第二个锁
third是：第二个锁被释放了，所以third可以获取到， 获取后run，

Lock支持上下文管理方法
'''
from threading import Lock

class Foo:
	def __init__(self):
		self.lock1 = threading.Lock()
		self.lock1.acquire()
		self.lock2 = threading.Lock()
		self.lock2.acquire()

	def first(self, printFirst):
		# printFirst() outputs "first". Do not change or remove this line.
		printFirst()
		self.lock1.release()

	def second(self, printSecond):
		# printSecond() outputs "second". Do not change or remove this line.
		self.lock1.acquire()
		printSecond()
		self.lock2.release()

	def third(self, printThird):
		# printThird() outputs "third". Do not change or remove this line.
		self.lock2.acquire()
		printThird()

class Foo:
    def __init__(self):
        self.locks = (Lock(),Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()
        
    def first(self, printFirst):
        printFirst()
        self.locks[0].release()
        
    def second(self, printSecond):
        with self.locks[0]:
            printSecond()
            self.locks[1].release()
            
    def third(self, printThird):
        with self.locks[1]:
            printThird()

'''
② Condition

互斥锁（Lock & RLock）是最简单的线程同步机制，在实际工作中会有很多复杂情况是互斥锁无法解决的，比如生产消费模式。而Python 提供的 Condition 对象提供了对复杂线程同步问题的支持。

生产者生产消费者需要的资料，消费者消耗生成的资料，生产者和消费者之间通过内存缓冲区进行通信，共享的内存缓冲池大小可变，生产者和消费者数量可变。 —————— 互斥锁难解决

Condition 被称为条件变量，可以理解为一种进阶的锁，使用的基本原理如下：

	1、Condition对象的构造函数可以接受一个 Lock/RLock 对象作为参数，如果没有指定，则默认是可重入锁 RLock，生成的 Condition 对象会维护一个 Lock/RLock 和一个 waiting 池。

	2、线程调用 acquire 方法获得 Condition 对象，这一点和 Lock/RLock类似 。

	# wait() 方法、notify() 方法、notifiy_all() 方法都只能在线程调用 acquire 方法之后，线程调用 release 方法之前！

	3、线程调用 wait 方法时，线程会释放 Condition 内部的锁并进入 blocked 状态，同时在waiting 池中记录这个线程。

	4、线程调用 notify/notify_all 方法时，Condition 对象会从 waiting 池中挑选一个线程，通知其调用 acquire 方法尝试取到锁。线程只能通过notify方法唤醒，所以notifyAll的作用在于防止有的线程永远处于沉默状态。

	5、线程调用 release 方法释放 Condition 对象


三个线程都尝试通过 Condition 获取 RLock。 线程1总是可以获取锁，另外两个得等待order赋相应的值。 线程1运行完设置order=1 通过notify(2)捞起了两个锁，然后线程2通过wait阻塞了锁1，运行，再设置order=2，再捞起剩下那个锁2，线程3再锁起锁2

'''

from threading import Condition

class Foo:
    def __init__(self):
        self.exec_condition = Condition()
        self.order = 0
        self.first_finish = lambda: self.order == 1
        self.second_finish = lambda: self.order == 2

    def first(self, printFirst):
        with self.exec_condition:
            printFirst()
            self.order = 1
            self.exec_condition.notify(2)

    def second(self, printSecond):
        with self.exec_condition:
            self.exec_condition.wait_for(self.first_finish)
            printSecond()
            self.order = 2
            self.exec_condition.notify()

    def third(self, printThird):
        with self.exec_condition:
            self.exec_condition.wait_for(self.second_finish)
            printThird()


'''
③ event

threading.Event 机制类似于一个线程向其它多个线程发号施令的模式，其它线程都会持有一个threading.Event 的对象，这些线程都会等待这个事件的“发生”，如果此事件一直不发生，那么这些线程将会阻塞，直至事件的“发生”。这种场景是非常普遍的。

构造方法非常简单，没有参数
event = threading.Event()

event.set() # 设置 Event 对象内部的信号标志为 True
event.wait() #该方法只有在内部信号为 True 的时候才会被执行并完成返回。当内部信号标志为False 时，则 wait() 一直等待到其为 True 时才返回。
event.clear() # 清除 Event 对象内部的信号标志，即设置为 False

三个线程一开始，1顺利执行，2被event1等住，3被event2等住，1执行完了以后设event1为true，则2才能执行返回，2执行完了以后设event2为true，3才能执行返回
'''

from threading import Event

class Foo:
    def __init__(self):
        self.done = (Event(),Event())
        
    def first(self, printFirst):
        printFirst()
        self.done[0].set()
        
    def second(self, printSecond):
        self.done[0].wait()
        printSecond()
        self.done[1].set()
            
    def third(self, printThird):
        self.done[1].wait()
        printThird()


'''
④ 信号量

泛泛的讲，多进程/线程中的信号量机制，可以理解为有二元组（S,Q），S是整形变量，初值为非负数，Q是一个初始状态为空的等待队列，这个机制设计就是为了为了实现进程/线程中同步和互斥关系。

threading.Semaphore 可以理解为一个内置的计数器，当调用 acquire 方法时候内置计数器 -1，对应着申请资源；调用 release 方法时候内置计数器+1，对应着释放可用资源。
'''

from threading import Semaphore

class Foo:
    def __init__(self):
        self.gates = (Semaphore(0),Semaphore(0))
        
    def first(self, printFirst):
        printFirst()
        self.gates[0].release()
        
    def second(self, printSecond):
        with self.gates[0]:
            printSecond()
            self.gates[1].release()
            
    def third(self, printThird):
        with self.gates[1]:
            printThird()