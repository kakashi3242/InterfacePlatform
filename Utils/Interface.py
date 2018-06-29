import requests


class Interface:
    """
    获取登录后的Session
    """
    session = requests.session()
    url = 'http://test.sis06.1course.cn'

    username = 'admin'
    password = '123456'
    loginApi = '/api/MemberShip/Login'
    apiUrl = url + loginApi
    loginData = {
        "Name": username,
        "Password": password
    }

    session.post(apiUrl, json = loginData)
