#붕어빵 재고
stock = {
    "팥붕어빵":10,
    "슈크림붕어빵":9,
    "초코붕어빵":6
}

#붕어빵 판매량
sales = {
    "팥붕어빵":0,
    "슈크림붕어빵":0,
    "초코붕어빵":0
}

#붕어빵 메뉴판
price = {
    "팥붕어빵" : 1000, 
    "슈크림붕어빵": 1200,
    "초코붕어빵" : 1500
}

#주문 기능
def order_bread():
    while True:
        bread_type = input("주문할 붕어빵을 선택하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵) 또는 '뒤로가기' 입력: ")
        if bread_type == "뒤로가기":
            return
        #메뉴 주문
        if bread_type in stock:
            bread_count = int(input("주문할 개수를 입력하세요: "))
            if stock[bread_type] >= bread_count:
                stock[bread_type] -= bread_count
                sales[bread_type] += bread_count
                print(f'{bread_type}을 {bread_count}개 판매했습니다.')
            else:
                print(f'재고가 부족합니다. {stock[bread_type]}개 만큼 주문할 수 있습니다.')
        else: 
            print("팥붕어빵, 슈크림붕어빵, 초코붕어빵 중 하나의 맛만 선택해주세요.")

#관리자 모드
def admin_mode():
    while True:
        bread_type = input("추가할 붕어빵을 선택하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵) 또는 '종료' 입력: ")
        if bread_type == "종료":
            break
        if bread_type in stock:
            bread_count = int(input("추가할 개수를 입력하세요: "))
            stock[bread_type] += bread_count
            print(f'{bread_type}의 재고가 {bread_count}개 추가되어 현재 {stock[bread_type]}개 입니다.')
        else:
            print("올바른 메뉴를 입력해주세요")

#계산 기능
def calculate_sales():
    total_sales = 0
    for key in sales: # 팥붕어빵
        total_sales += (price[key] * sales[key])
    print(f'오늘의 총 매출은 {total_sales}원 입니다.')

#메인 기능 선택
while True:
    mode = input("원하는 모드를 선택하세요. (주문, 관리자, 종료): ")
    if mode == "종료":
        print("시스템을 종료합니다.")
        break
    elif mode == "주문":
        order_bread() 
    elif mode == "관리자":
        admin_mode()

#매출 출력
calculate_sales()
