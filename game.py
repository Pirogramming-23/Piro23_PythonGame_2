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
        elif station == "":
            print(f"❌ 입력 없음! 벌주! 🍻")
            current_player.set_count(current_player.get_count() + 1)
        elif station not in station_list:
            print(f"❌ {station}는 2호선 역이 아닙니다! 벌주! 🍻")
            current_player.set_count(current_player.get_count() + 1)
        elif station in used_stations:
            print(f"❌ {station}은(는) 이미 나왔습니다! 벌주! 🍻")
            current_player.set_count(current_player.get_count() + 1)
        else:
            print(f"✅ {station} 통과!")
            used_stations.add(station)

        # 현재 플레이어의 상태 출력
        print(f"🍺 {name}님의 현재 잔 수: {current_player.get_count()} / {current_player.get_life()}")

        if current_player.get_count() >= current_player.get_life():
            print(f"\n💀 {name}님은 전사하셨습니다... 꿈나라에서 편히 쉬세요.")
            break

        turn += 1 #지하철 게임 끝//




import random


class Person:
    def __init__(self, name, life):
        self.name = name
        self.life = life
        self.count = 0

    def get_name(self):
        return self.name

    def get_life(self):
        return self.life

    def set_count(self, value):
        self.count = value

    def get_count(self):
        return self.count

    def __str__(self):
        return f"이름: {self.name}, 주량: {self.life}잔"  # 자바의 toString 오버라이딩과 비슷


people_list = [
    Person("은서", 2),
    Person("예진", 8),
    Person("헌도", 6),
    Person("연서", 4),
]


def init_setting():
    print("게임을 시작합니다!")
    try:
        player_name = input("오늘 거하게 취해볼 당신의 이름은? : ")

        print("~~~~~~~~~~~~~~~~🍺 소주 기준 당신의 주량은? 🍺~~~~~~~~~~~~~~~~")
        print("                 🍺 1. 소주 반 병 (2잔) ")
        print("                 🍺 2. 소주 반 병에서 한 병  (4잔) ")
        print("                 🍺 3. 소주 한 병에서 한 병 반 (6잔) ")
        print("                 🍺 4. 소주 한 병에서 두 병 (8잔) ")
        print("                 🍺 5. 소주 두 병 이상 (10잔) ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        while True:
            try:
                player_life_temp = input(
                    "당신의 치사량 (주량)은 얼마만큼인가요 ? (1~5을 선택해주세요) : "
                ).strip()
                match player_life_temp:
                    case "1":
                        player_life = 2
                    case "2":
                        player_life = 4
                    case "3":
                        player_life = 6
                    case "4":
                        player_life = 8
                    case "5":
                        player_life = 10
                    case _:
                        print("1~5 중에서 골라주세요.")
                        continue
                break
            except Exception as e:
                print("입력 오류:", e)

        return Person(player_name, player_life)

    except ValueError as e:
        print(e)

def play_setting():
    while True:
        try:
            number = input(
                "함께 취할 친구들은 얼마나 필요하신가요? (사회적 거리두기로 인해 최대 3명까지 초대할 수 있습니다!) : "
            ).strip()
            match number:
                case "1":
                    game_people_list = random.sample(people_list, k=1)
                    print("\n🍺 한 명이 초대되었습니다!")
                case "2":
                    game_people_list = random.sample(people_list, k=2)
                    print("\n🍺 두 명이 초대되었습니다!")
                case "3":
                    game_people_list = random.sample(people_list, k=3)
                    print("\n🍺 세 명이 초대되었습니다!")
                case _:
                    print("1~3 중에서 선택해주세요.")
                    continue

            for person in game_people_list:
                print(f"- {person}")
            return game_people_list

        except Exception as e:
            print(e)


def play_game(player, game_people_list):
    turn = 0
    while True:
        current_player = game_people_list[turn % len(game_people_list)]

        for person in game_people_list:
            print(
                f"{person.get_name()}은 (는) 지금까지 {person.get_count()}🍺 : 치사량까지 {person.get_life()}"
            )

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~🍺 오늘의 Alcohol Game 🍺~~~~~~~~~~~~~~~~~~~")
        print("                 🍺 1. 369 게임 ")
        print("                 🍺 2. 지하철 게임 ")
        print("                 🍺 3. 딸기 게임 ")
        print("                 🍺 4. 시장 게임 ")
        print("                 🍺 5. 두부 게임 ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        user_input = input(
            f"\n술게임 진행 중! {current_player.get_name()}님의 턴입니다.\n그만하고 싶으면 'exit'을, 계속하려면 Enter를 눌러주세요: "
        )
        if user_input.strip().lower() == "exit":
            print("🍺 게임을 종료합니다. 🍺")
            break

        if current_player.get_count() >= current_player.get_life():
            print("GAME OVER!")
            print(
                f"{current_player.get_name()}이 (가) 전사했습니다...꿈나라에서는 편히 쉬시길...zzz"
            )
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("                 🍺 다음에 술마시면 또 불러주세요~안녕! 🍺")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            break

        try:
            choice = input(
                f"{current_player.get_name()}님이 선택할 게임 번호는? (1~5): "
            ).strip()
            match choice:
                case "1":
                    #game_369()
                    break
                case "2":
                    subway_game(game_people_list)
                    break
                # case "3":
                #     strawberry_game()
                #     break
                # case "4":
                #     market_game()
                #     break
                # case "5":
                #     tofu_game()
                #     break
                case _:
                    print("올바른 게임 번호를 골라주세요!")
        except Exception as e:
            print(e)

        turn += 1


# 메인 루프
while True:
    choice = input("게임을 진행할까요? (y/n): ").strip().lower()
    try:
        match choice:
            case "y":
                player = init_setting()
                game_people_list = play_setting()
                game_people_list.append(player)
                play_game(player, game_people_list)
            case "n":
                print("게임을 종료합니다.")
                break
            case _:
                raise ValueError("잘못된 입력입니다. y 또는 n을 입력하세요.")
    except ValueError as e:
        print(e)


