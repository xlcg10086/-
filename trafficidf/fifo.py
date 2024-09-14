
class FIFO:
  """
  FIFO 类，用于保存坐标信息
  """

  def __init__(self, max_size):
    """
    初始化 FIFO 类

    Args:
      max_size: FIFO 队列的最大长度
    """

    self.max_size = max_size
    self.queue = []

  def add(self, point):
    """
    将坐标添加到 FIFO 队列中

    Args:
      x: X 坐标
      y: Y 坐标
    """

    # 如果队列已满，则弹出第一个元素
    if len(self.queue) == self.max_size:
      self.queue.pop(0)

    # 将新元素添加到队列末尾
    self.queue.append(point)

  def get(self):
    """
    从 FIFO 队列中获取坐标

    Returns:
      一个包含 X 坐标和 Y 坐标的元组
    """

    if len(self.queue) == 0:
      return None

    # 返回第一个元素
    return self.queue[0]

  def is_full(self):
    """
    判断 FIFO 队列是否已满

    Returns:
      True 如果队列已满，False 如果队列未满
    """

    return len(self.queue) == self.max_size

  def is_empty(self):
    """
    判断 FIFO 队列是否为空

    Returns:
      True 如果队列为空，False 如果队列非空
    """

    return len(self.queue) == 0