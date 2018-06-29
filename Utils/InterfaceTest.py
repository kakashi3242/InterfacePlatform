from Utils.Interface import Interface
import json, ast


class InterfaceTest(Interface):
    def __init__(self, ):
        super().__init__()
        self.total_pass = 0
        self.total_fail = 0
        self.total_count = 0
        self.except_error = 0
        self.error_info = []

    def test_interface(self, reqMethod, reqUrl, reqParam, expectInfo):
        try:

            if reqMethod == 'get':

                url = self.url + reqUrl
                respInfo = self.session.get(url)
                respInfo = json.loads(respInfo.text)
                if respInfo['state'] == expectInfo:
                    self.total_pass += 1
                else:
                    self.total_fail += 1

            elif reqMethod == 'post':
                url = self.url + reqUrl
                reqParam = ast.literal_eval(reqParam)
                respInfo = self.session.post(url, json = reqParam)
                respInfo = json.loads(respInfo.text)
                if respInfo['state'] == expectInfo:
                    self.total_pass += 1
                else:
                    self.total_fail += 1
            else:
                self.except_error += 1

            self.total_count += 1

            return self.total_pass, self.total_fail, self.total_count, self.except_error

        except Exception as e:

            self.except_error += 1
            self.total_count += 1
            self.error_info.append(e)

            return self.total_pass, self.total_fail, self.total_count, self.except_error
