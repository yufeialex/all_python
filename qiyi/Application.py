#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
import logging
from alva.controller import AdminController
from com.qiyi.yufei import AIController

logger = logging.getLogger(__name__)

handlers = []
handlers.append((r'/apis/admin/server_status.action', AdminController.AdminController))
kafka_task_handler = None
kafka_parallel_num = 1

http_port = 8080


def register_handler(path, handler):
    handlers.append((path, handler))


def start_http():
    service_name = "aaa"
    if service_name is not None:
        task_path = '/apis/%s/task/create' % service_name
        register_handler(task_path, AIController.AIController)
        logger.info('registed task path:%s' % task_path)

    application = tornado.web.Application(handlers)
    application.listen(http_port)
    tornado.ioloop.IOLoop.instance().start()


def start():
    start_http()


if __name__ == "__main__":
    start()
