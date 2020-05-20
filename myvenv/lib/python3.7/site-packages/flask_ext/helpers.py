# -*- coding: utf-8 -*-

from werkzeug.local import LocalProxy


def get_real_object(obj):
    """获取真实的 object（例如：用于获取 Flask-Login 的 current_user 的 object）"""
    if isinstance(obj, LocalProxy):
        return obj._get_current_object()
    return obj
