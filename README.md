>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

# 자전거 공유 데이터 분석 프로그램

이 프로그램은 미국의 자전거 공유 데이터를 분석하는 도구입니다. 사용자는 특정 도시, 월, 요일을 선택하여 해당 조건에 맞는 데이터를 필터링하고, 다양한 통계 정보를 출력할 수 있습니다.

## 데이터 파일

프로그램은 다음의 도시 데이터를 사용합니다:
- Chicago: `chicago.csv`
- New York City: `new_york_city.csv`
- Washington: `washington.csv`

## 생성 날짜

2025-01-23

## 기능

1. **도시, 월, 요일 필터링**: 사용자가 분석할 도시, 월, 요일을 입력받습니다.
2. **데이터 로드**: 선택한 도시의 데이터를 CSV 파일에서 불러옵니다.
3. **통계 계산**:
   - 가장 빈번한 여행 시간
   - 가장 인기 있는 출발지와 도착지
   - 총 여행 시간 및 평균 여행 시간
   - 사용자 유형, 성별, 출생 연도 통계
4. **원시 데이터 표시**: 사용자가 요청할 경우 원시 데이터를 5행씩 출력합니다.

## 코드 설명

### 1. 필터 입력 받기

`get_filters()` 함수는 사용자가 분석할 도시, 월, 요일을 입력받습니다.

### 2. 데이터 로드

`load_data(city, month, day)` 함수는 선택한 도시의 데이터를 불러오고, 월과 요일에 따라 필터링합니다.

### 3. 통계 계산

- `time_stats(df)`: 가장 빈번한 여행 시간 통계를 계산합니다.
- `station_stats(df)`: 가장 인기 있는 출발지와 도착지 통계를 계산합니다.
- `trip_duration_stats(df)`: 총 여행 시간과 평균 여행 시간을 계산합니다.
- `user_stats(df)`: 사용자 유형, 성별, 출생 연도에 대한 통계를 계산합니다.

### 4. 원시 데이터 표시

`display_raw_data(df)` 함수는 사용자가 요청할 경우 원시 데이터를 5행씩 출력합니다.

### 5. 프로그램 실행 루프

`main()` 함수는 프로그램의 주요 실행 루프를 담당합니다. 사용자가 원하는 조건을 입력받고, 통계 정보를 출력한 후, 프로그램을 다시 실행할지 여부를 묻습니다.

## 사용 방법

1. 프로그램을 실행합니다.
2. 분석할 도시, 월, 요일을 입력합니다.
3. 통계 정보를 확인합니다.
4. 원시 데이터를 추가로 보고 싶으면 'yes'를 입력합니다.
5. 프로그램을 종료하려면 'no'를 입력합니다.

## 라이센스

이 프로그램은 MIT 라이센스에 따라 배포됩니다.
