### 这是一个抓取activeMQ页面信息的工具

```python
from get_queue_info import *

result = get_queue_info('admin', 'admin', '192.168.121.146',)
print(result)

```

**结果**

[[queue1, 0,1,100,100],[queue2,10,0,100,100],[queue1, 123425,1,2010345,
1932876]] 

返回结果是个列表，其中每个元素也是列表，列表元素是每个队列的信息
```bash
Name, Number Of Pending Messages,Number Of Consumers,Messages Enqueued  	
Messages Dequeued
```
可以根据列表内容判断队列是否积压，是否有消费者，制作告警脚本，