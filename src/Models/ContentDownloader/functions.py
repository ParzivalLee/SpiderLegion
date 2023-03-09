import requests



# 文件下载参数
DCParams = {
        'mehtod':'请求方法',
        'url':'文件下载网址',
        'path':'文件保存路径',
        'filename':'保存的文件名',
        'headers':'文件请求头'
        }

# 文件下载
def downloadContent(params):
    response = requests.request(params['method'],
                                params['url'],
                                headers=headers)
    if response.status_code == 200 or response.status_code == '301':
        with open(os.path.join(params['path'], params['filename']),
                  'wb', encoding='utf-8') as fp:
            fp.write(response.content)

    result = params
    result['stats_code'] = response.status_code

