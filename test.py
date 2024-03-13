import os
import pickle
import pyzard
# 현재 디렉토리 내의 파일 목록을 얻습니다.
file_list = os.listdir()

# 피클 확장자를 가진 파일만 필터링합니다.
pickle_files = [file for file in file_list if file.endswith('.pkl')]

plkslotname_lst = []
plkslotnumber_lst = []
for pickle_file in pickle_files:
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)
        # 이곳에서 데이터 활용 가능
        plkslotname_lst.append(data[0])
        plkslotnumber_lst.append(data[1])
plkslotname_lst = pyzard.ll2l(plkslotname_lst)
plkslotnumber_lst = pyzard.ll2l(plkslotnumber_lst)

print(plkslotname_lst)