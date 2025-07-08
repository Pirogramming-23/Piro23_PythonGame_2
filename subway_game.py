#지하철 게임
def subway_game(game_people_list):
    import time
    print("\n🚇 지하철 2호선 게임을 시작합니다!")
    print("※ 돌아가며 실제 2호선 역을 입력하세요.")
    print("※ 이미 나온 역, 없는 역, 입력 지연은 벌주입니다.\n")

    station_list = [
        "시청", "을지로입구", "을지로3가", "을지로4가", "동대문역사문화공원", "신당", "상왕십리", "왕십리",
        "한양대", "뚝섬", "성수", "건대입구", "구의", "강변", "잠실나루", "잠실", "잠실새내", "종합운동장",
        "삼성", "선릉", "역삼", "강남", "교대", "서초", "방배", "사당", "낙성대", "서울대입구",
        "봉천", "신림", "신대방", "구로디지털단지", "대림", "신도림", "도림천", "양천구청", "신정네거리",
        "까치산", "당산", "합정", "홍대입구", "신촌", "이대", "아현", "충정로"
    ]
    used_stations = set()
    turn = 0

    while True:
        current_player = game_people_list[turn % len(game_people_list)]
        name = current_player.get_name()

        print(f"\n🎮 {name}님의 차례입니다!")
        print("지하철 2호선 역 이름을 입력해주세요 (10초 제한).")

        start_time = time.time()
        station = input(f"{name} ▶ ").strip()
        elapsed_time = time.time() - start_time

        if elapsed_time > 10:
            print(f"⏰ 시간 초과! {name}님은 벌주 한 잔! 🍻")
            current_player.set_count(current_player.get_count() + 1)
            current_player.life -= 1
            break
        elif station == "":
            print(f"❌ 입력 없음! 벌주! 🍻")
            current_player.set_count(current_player.get_count() + 1)
            current_player.life -= 1
            break
        elif station not in station_list:
            print(f"❌ {station}는 2호선 역이 아닙니다! 벌주! 🍻")
            current_player.set_count(current_player.get_count() + 1)
            current_player.life -= 1
            break
        elif station in used_stations:
            print(f"❌ {station}은(는) 이미 나왔습니다! 벌주! 🍻")
            current_player.set_count(current_player.get_count() + 1)
            current_player.life -= 1
            break
        else:
            print(f"✅ {station} 통과!")
            used_stations.add(station)

        # 현재 플레이어의 상태 출력
        print(f"🍺 {name}님의 현재 잔 수: {current_player.get_count()} / {current_player.get_life()}")

        turn += 1 #지하철 게임 끝//