import random
from korean_game import korean_game

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
        return f"이름: {self.name}, 주량: {self.life}잔"


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
        print("                 🍺 5. 훈민정음 게임 ")
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
                    game_369()
                    break
                case "2":
                    subway_game()
                    break
                case "3":
                    strawberry_game()
                    break
                case "4":
                    market_game()
                    break
                case "5":
                    korean_game(player, game_people_list) #tofu_game에서 korean_game으로 수정. 함수 파라미터 추가
                    break
                case _:
                    print("올바른 게임 번호를 골라주세요!")
        except Exception as e:
            print(e)

        turn += 1

def market_game():
    global game_people_list
    players = game_people_list
    item_list = []
    turn = 0
    current_player = players[turn % len(players)]
    print(f"\n{current_player.get_name()}가 좋아하는 시장 게임‼️ 시장 게임‼️ 게임 start~")
    print("시장에 가면~‼️ 시장에 가면~‼️")

    while True:
        current_player = players[turn % len(players)]
        print(f"\n🎯 {current_player.get_name()} 차례입니다.")
        user_input = input("→ '시장에 가면 ~~도 있고 ~~도 있고' 식으로 말하세요: ").strip()

        # "시장에 가면" 제거
        if user_input.startswith("시장에 가면"):
            user_input = user_input[len("시장에 가면"):].strip()

        # "도 있고" 기준으로 분리
        said_items = [item.strip() for item in user_input.split("도 있고") if item.strip()]

        # 검증
        if said_items[:len(item_list)] != item_list:
            print("❌ 순서 틀렸거나 리듬을 틀렸거나 빠뜨렸습니다!")
            print(f"{current_player.get_name()} 마셔라~ 🍻\n")
            break

        if len(said_items) != len(item_list) + 1:
            print("❌ 새 항목을 정확히 1개 추가해야 합니다!")
            print(f"{current_player.get_name()} 마셔라~ 🍺\n")
            break

        item_list.append(said_items[-1])
        print("✅ 정답입니다! 다음 차례로 넘어갑니다.")
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