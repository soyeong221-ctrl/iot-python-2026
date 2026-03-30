# ex09_csv_read.py csv 파일 읽기

with open('./day02/부산시_해운대구_도서정보.csv', 'r', encoding = 'utf-8') as f:
    # line = f.read()
    for  line in f:
        print(line.strip()) # \n 줄바꿈 제거, 문자열로 출력, 한 번 더 가공 필요