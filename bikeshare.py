import time
import pandas as pd
import numpy as np

# 도시 이름을 키로 하고 해당 도시의 데이터 파일 경로를 값으로 하는 딕셔너리
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """사용자로부터 분석할 도시, 월, 요일을 입력받습니다."""
    print('안녕하세요! 미국 자전거 공유 데이터를 탐색해봅시다!')

    city = get_city_input()
    month = get_month_input()
    day = get_day_input()

    print(f"\n입력한 값 - 도시: '{city}', 월: '{month}', 요일: '{day}'")
    print('-' * 40)

    return city, month, day

def get_city_input():
    """유효한 도시 이름을 입력받습니다."""
    city_names = list(CITY_DATA.keys())
    city = ""
    while city not in city_names:
        city = input(f"분석할 도시 이름을 입력하세요 {city_names}: ").lower()
    return city

def get_month_input():
    """유효한 월을 입력받습니다."""
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june',
                    'july', 'august', 'september', 'october', 'november', 'december']
    month = ""
    while month not in valid_months:
        month = input("필터링할 월을 입력하세요 (예: 'all', 'january' ... 'december'): ").lower()
    return month

def get_day_input():
    """유효한 요일을 입력받습니다."""
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ""
    while day not in valid_days:
        day = input("필터링할 요일을 입력하세요 (예: 'all', 'monday' ... 'sunday'): ").lower()
    return day

def load_data(city, month, day):
    """지정된 도시의 데이터를 불러오고 필터링합니다."""
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.strftime('%B').str.lower()
    df['Day'] = df['Start Time'].dt.day_name().str.lower()

    # 필터링
    return filter_data(df, month, day)

def filter_data(df, month, day):
    """데이터프레임을 월과 요일에 따라 필터링합니다."""
    if month != 'all':
        df = df[df['Month'] == month]
    if day != 'all':
        df = df[df['Day'] == day]
    return df

def time_stats(df):
    """가장 빈번한 여행 시간에 대한 통계를 계산하고 출력합니다."""
    print('\n가장 빈번한 여행 시간 통계를 계산 중입니다...\n')
    start_time = time.time()

    common_month = df['Month'].mode()[0]
    common_day = df['Day'].mode()[0]
    common_hour = df['Start Time'].dt.hour.mode()[0]

    print(f"가장 흔한 월은: {common_month}")
    print(f"가장 흔한 요일은: {common_day}")
    print(f"가장 흔한 시간은: {common_hour}시")
    print(f"\n이 통계를 계산하는 데 {time.time() - start_time:.4f}초가 걸렸습니다.")
    print('-' * 40)

def station_stats(df):
    """가장 인기 있는 출발지와 도착지 통계를 계산합니다."""
    print('\n가장 인기 있는 출발지와 도착지 통계를 계산 중입니다...\n')
    start_time = time.time()

    common_start_station = df['Start Station'].mode()[0]
    common_end_station = df['End Station'].mode()[0]
    freq_start_and_end_station = (df['Start Station'] + " -> " + df['End Station']).mode()[0]

    print(f"가장 많이 사용된 출발지는: {common_start_station}")
    print(f"가장 많이 사용된 도착지는: {common_end_station}")
    print(f"가장 빈번한 출발지와 도착지 조합은: {freq_start_and_end_station}")
    print(f"\n이 통계를 계산하는 데 {time.time() - start_time:.4f}초가 걸렸습니다.")
    print('-' * 40)

def trip_duration_stats(df):
    """총 여행 시간과 평균 여행 시간에 대한 통계를 계산하고 출력합니다."""
    print('\n여행 시간 통계를 계산 중입니다...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()

    print(f"총 여행 시간은 {total_travel_time // 3600}시간 {(total_travel_time % 3600) // 60}분 {total_travel_time % 60}초입니다.")
    print(f"평균 여행 시간은 {mean_travel_time // 3600}시간 {(mean_travel_time % 3600) // 60}분 {mean_travel_time % 60}초입니다.")
    print(f"\n이 통계를 계산하는 데 {time.time() - start_time:.4f}초가 걸렸습니다.")
    print('-' * 40)

def user_stats(df):
    """사용자 유형, 성별, 출생 연도에 대한 통계를 계산하고 출력합니다."""
    print('\n사용자 통계를 계산 중입니다...\n')
    start_time = time.time()

    print("사용자 유형별 개수:")
    print(df['User Type'].value_counts())
    print('-' * 40)

    if 'Gender' in df.columns:
        print("성별별 개수:")
        print(df['Gender'].value_counts())
    else:
        print("성별 데이터가 없습니다.")

    if 'Birth Year' in df.columns:
        print(f"가장 오래된 출생 연도: {int(df['Birth Year'].min())}")
        print(f"가장 최근 출생 연도: {int(df['Birth Year'].max())}")
        print(f"가장 흔한 출생 연도: {int(df['Birth Year'].mode()[0])}")
    else:
        print("출생 연도 데이터가 없습니다.")

    print(f"\n이 통계를 계산하는 데 {time.time() - start_time:.4f}초가 걸렸습니다.")
    print('-' * 40)

def display_raw_data(df):
    """사용자 요청에 따라 원시 데이터를 5행씩 출력합니다."""
    start_row = 0
    while True:
        show_data = input("\n원시 데이터를 5행씩 더 보고 싶으신가요? 'yes' 또는 'no'로 입력하세요: ").lower()
        if show_data == 'yes':
            print(df.iloc[start_row:start_row + 5])
            start_row += 5
            if start_row >= len(df):
                print("\n더 이상 표시할 데이터가 없습니다.")
                break
        elif show_data == 'no':
            print("\n원시 데이터 표시를 종료합니다.")
            break
        else:
            print("\n잘못된 입력입니다. 'yes' 또는 'no'로 입력해주세요.")

def main():
    """주요 프로그램 실행 루프"""
    while True:
        city, month, day = get_filters()  # 사용자로부터 필터 입력 받기
        df = load_data(city, month, day)   # 입력받은 필터로 데이터 불러오기

        if df.empty:
            print("입력한 조건에 맞는 데이터가 없습니다.")
        else:
            display_raw_data(df)          # 원시 데이터 표시
            time_stats(df)                # 시간 통계 계산 및 출력
            station_stats(df)             # 역 통계 계산 및 출력
            trip_duration_stats(df)       # 여행 시간 통계 계산 및 출력
            user_stats(df)                # 사용자 통계 계산 및 출력

        # 프로그램을 다시 실행할지 여부 묻기
        restart = input('\n다시 시작하시겠습니까? "yes" 또는 "no"를 입력하세요.\n').lower()
        if restart != 'yes':
            print("프로그램을 종료합니다. 감사합니다!")
            break

if __name__ == "__main__":
    main()
