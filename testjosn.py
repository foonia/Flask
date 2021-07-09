import json
# json은 바이너리 데이터로 이해하고 있는것이 맡다
info1 ={
    '단말': '기가지니1',
    'MAC 주소': '1234',
    'SAID' : 'T13',
    'OTV 개통여부' : 'O',
    '사용자': '최세찬',
}
info2={
    '단말': '기가지니1',
    'MAC 주소': '80:8C:97:7C:15:C8',
    'SAID' : 'T13',
    'OTV 개통여부' : 'O',
    '사용자': '최세찬',
}

json_info = json.dumps(info1,ensure_ascii=False)

