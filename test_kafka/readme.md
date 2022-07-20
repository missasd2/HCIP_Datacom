
pip 安装kafka报错return '<SimpleProducer batch=%s>' % self.async解决办法

```shell

# 方法一
# 因为py3.7里面async已经变成了关键字。所以导致了不兼容。
pip install kafka-python

# 方法二
切换到3.6版本
```