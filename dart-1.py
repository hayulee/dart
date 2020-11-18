import requests

AUTH_KEY = 'd47381546862713484d04da86d84ebd6b02c194d'

args = {
    'bgn_de':'20201001',
    'end_de':'20201101',
    'corp_cls':'K'
}

args_str = ''
for k, v in args.items():
    args_str += '&%s=%s' %(k, v)

# print(args_str)

res = requests.get('https://opendart.fss.or.kr/api/list.json?crtfc_key=%s%s' %(AUTH_KEY, args_str))
data = res.json()
print(data)