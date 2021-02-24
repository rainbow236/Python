import execjs # pip install PyExecJS

def js_from_file(file_name):
    """
    讀取js檔案
    :return:
    """
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()
    return result

str = '123456'
key = 'NeGqWKgwp07QXPdnh0HsEgkpEeb25SamoBU3bFRh1IQ='
iv = 'RH/nP5lzsAC7+LRidCmsGw=='
context1 = execjs.compile(js_from_file('aes256Encryption.js'))
encrypt = context1.call("Encrypt", str, key, iv)
decrypt = context1.call("Decrypt", str, key, iv)
