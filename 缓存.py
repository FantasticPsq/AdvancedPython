v1 = "zhouqi"  # 开辟内存来存储float对象，并将对象添加到refchain链表。
print(id(v1))  # 内存地址：443603348
del v1  # 引用计数器-1，如果为0则在rechain链表中移除，不销毁对象，而是将对象添加到float的free_list.
v2 = "zhouqi"  # 优先去free_list中获取对象，并重置为9.999，如果free_list为空才重新开辟内存。
print(id(v2))
v1 = "wupeiqi"
v2 = "wupeiqi"
print(id(v1) == id(v2))

v1 = {"k1": 123}
print(id(v1))
del v1
v2 = {"name": "武沛齐", "age": 18, "gender": "男"}
print(id(v2))
