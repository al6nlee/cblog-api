from typing import List


class BaseResponse:
    Code = 500
    Message = '服务器内部错误或网络错误'

    def asdict(self):  # asdict 是 Python 数据类（dataclass）中的一个辅助函数，将数据类的实例转换为一个普通的 Python 字典
        return dict(code=self.Code, message=self.Message)


class SuccessResponse(BaseResponse):
    Code = 200
    Message = '请求成功'

    def __init__(self):
        self.items = None
        self.total = None
        self.item = None
        super().__init__()

    def set_item(self, item):
        self.item = item
        return self

    def set_items(self, items: List, total: int = None):
        self.items = items
        self.total = total if total is not None else len(items)
        return self

    def asdict(self):
        ret = super().asdict()
        if self.item is not None:
            ret['item'] = self.item
        elif self.items is not None:
            ret['items'] = self.items
            ret['total'] = self.total
        return ret
