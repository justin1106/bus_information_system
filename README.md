# 스마트 버스 도착정보 시스템


## 소개

**스마트 버스 도착정보 시스템**은 사용자가 선택한 정류장의 버스 도착 정보를 시각적으로 보여주는 프로그램입니다. 이 프로그램을 통해 사용자는 버스의 도착 시간, 버스의 위치 등을 파악할 수 있습니다.

## 기능

- 지정된 버스정류장의 실시간 버스 도착 정보 조회
- 버스 도착 위치를 원과 버스 아이콘 등의 그래픽으로 시각화
- 정류장 이름, 버스 번호, 도착 예상 시간 표시
- 네이버 날씨 및 뉴스 크롤링 가능

## 사용 기술

- Python
- Pygame (UI 렌더링)
- BeautifulSoup (웹 크롤링)

## 디렉토리 구조
``` bash
smart-bus-info/
├── smart_bus_info.py # 메인 실행 파일
├── config.txt # 지역명, 정류장 이름, ID 정보를 담은 설정 파일
├── config.py # API 키를 담은 파일 (SERVICE_KEY)
├── bus_blue.png # 버스 아이콘 이미지
├── font/
│ └── NanumGothic.ttf # 한글 폰트 파일
└── README.md # 설명 파일
```

## 실행 방법

1. 필수 모듈 설치:
    ```bash
    pip install -r requirements.txt
    ```

2. `config.txt` 파일 구성:
    ```
   지역이름:정류장명:정류장ID
    ```
    예시:
    ```
   서울:강남역:12345
    ```

3. `config.py` 파일 생성 후 다음과 같이 작성:
    ```python
    SERVICE_KEY = "발급받은_버스_API_서비스_키"
    ```

4. 프로그램 실행:
    ```bash
    python smart_bus_info.py
    ```




## 주의 사항

- 날씨 및 뉴스 관련 코드는 현재 에러로 인해 주석 처리되어 있으며, 추후 수정 예정
- API 키는 공공데이터포털에서 [서울시 버스 도착 정보 API](https://www.data.go.kr/data/15000565/openapi.do) 신청 후 사용 가능
- 한글 폰트 `NanumGothic.ttf`는 `font/` 폴더에 있어야 함

## 실행 화면

<img width="70%" height="70%" alt="Image" src="https://github.com/user-attachments/assets/8c656097-95fb-4518-aa5e-95afcadd0ff2" />

## 라이선스

MIT License


