# -*- coding: UTF-8 -*-
from sql.utils.workflow import Workflow


def global_info(request):
    """存放用户，菜单信息等."""
    user = request.user
    if user:
        # 获取待办数量
        try:
            todo = Workflow().auditlist(user, 0, 0, 1)['data']['auditlistCount']
        except Exception:
            todo = 0
    else:
        todo = 0

    return {
        'todo': todo,
    }
