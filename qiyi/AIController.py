# -*- coding: utf-8 -*-
import tornado.web
import traceback, random
import json, time, logging, os
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
from alva.config import ApiCode

logger = logging.getLogger(__name__)


class AIController(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(10)

    def process(self):
        try:
            remote_ip = self.request.remote_ip
            data = self.get_argument("data", None)
            jobId = self.get_argument("jobId", None)
            serviceName = self.get_argument("serviceName", None)
            serviceVersion = self.get_argument("serviceVersion", None)
            serviceTag = self.get_argument("serviceTag", None)
            priority = self.get_argument("priority", None)
            timeout = self.get_argument("timeout", None)
            nologging = self.get_argument("nologging", None)
            ext = self.get_argument("ext", None)
            timestamp = self.get_argument("timestamp", None)
            tracingId = self.get_argument("tracingId", None)
            source = self.get_argument("source", None)
            callbackUrl = self.get_argument("callbackUrl", None)
            syn = self.get_argument("syn", 1)

            if os.path.exists('/tmp/aiservice/disabled.txt'):
                self.write(json.dumps({'code': ApiCode.ERR_SERVER_UPGRADING, 'msg': 'server is upgrading'}))
                return

            try:
                data = json.loads(data)
            except:
                self.write(json.dumps({'code': ApiCode.ERR_WRONG_PARAMS, 'msg': 'data param should be a jsonobject!'}))
                return

            if jobId is None:
                self.write(json.dumps({'code': ApiCode.ERR_WRONG_PARAMS, 'msg': 'jobId param is mandatory !'}))
                return

            alva_upload_files = []
            file_metas = self.request.files.get('files', None)
            if file_metas:
                for meta in file_metas:
                    filename = meta['filename']
                    file_path = os.path.join(self.upload_path, filename)

                    with open(file_path, 'wb') as up:
                        up.write(meta['body'])
                        alva_upload_files.append(file_path)

            json_data = {}
            json_data['jobId'] = jobId
            json_data['serviceName'] = serviceName
            json_data['serviceVersion'] = serviceVersion
            json_data['serviceTag'] = serviceTag
            json_data['priority'] = priority
            json_data['timeout'] = timeout
            json_data['nologging'] = nologging
            json_data['ext'] = ext
            json_data['timestamp'] = timestamp
            json_data['tracingId'] = tracingId
            json_data['source'] = source
            json_data['callbackUrl'] = callbackUrl
            json_data['data'] = data

            json_data = {k: v for k, v in json_data.items() if v is not None}

            if len(alva_upload_files) > 0:
                json_data['files'] = alva_upload_files
        except Exception:
            res = {}
            res['code'] = ApiCode.ERR_UNKNOW
            res['msg'] = traceback.format_exc()
            self.write(json.dumps(res))
            logger.warning('AIController exception', exc_info=1)

    @run_on_executor
    def get(self):
        self.process()

    @run_on_executor
    def post(self):
        self.process()
