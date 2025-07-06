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



def korean_game(player, game_people_list):

    #훈민정음 게임 
    word_list = [
        "오징어", "기러기", "토마토", "스위스", "사과", "바나나", "고양이", "강아지", 
        "컴퓨터", "핸드폰", "커피", "맥주", "소주", "치킨", "피자", "토끼", "펭귄",
        "딸기", "수박", "포도", "귤", "감자", "고구마", "마우스", "키보드", "모니터",
        "텔레비전", "냉장고", "에어컨", "청소기", "선풍기", "신발", "모자", "가방",
        "시계", "안경", "노트북", "선물", "피로그래밍"]
    print("\n🍺 훈민정음 게임을 시작합니다! 🍺")
    used_words = set()

    if player not in game_people_list:
        participants = [player] + game_people_list
    else:
        participants = game_people_list

    def get_chosung(word):
        chosung_list = []
        CHOSUNG_START = 0x1100
        HANGUL_START = 0xAC00
        CHOSUNG_LIST = [
            'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ',
            'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ',
            'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
        ]

        for ch in word:
            if '가' <= ch <= '힣':
                code = ord(ch) - HANGUL_START
                cho = code // (21 * 28)
                chosung_list.append(CHOSUNG_LIST[cho])
            else:
                chosung_list.append(ch)
        return ''.join(chosung_list)


    game_continue = True
    while game_continue:
        answer_word = random.choice(word_list)
        chosung = get_chosung(answer_word)
        print(f"\n🍺 제시된 초성: {chosung}. 똑같은 단어는 안돼요~")

        for person in participants:
            if person.get_count() >= person.get_life():
                continue

            if person == player:
                user_word = input(f"{person.get_name()}님의 답변은? (패스하려면 Enter): ").strip()
                if user_word == "":
                    print(f"{person.get_name()}님 패스! 벌칙 1잔~ 🍺")
                    person.set_count(person.get_count() + 1)
                elif get_chosung(user_word) == chosung and user_word not in used_words:
                    print(f"{person.get_name()} 정답!")
                    used_words.add(user_word)
                else:
                    print(f"{person.get_name()} 오답! 벌칙 1잔~ 🍺")
                    person.set_count(person.get_count() + 1)
            else:
                possible_words = [w for w in word_list if get_chosung(w) == chosung and w not in used_words]
                if possible_words and random.random() > 0.3:
                    comp_word = random.choice(possible_words)
                    print(f"{person.get_name()}의 답: {comp_word} (정답!)")
                    used_words.add(comp_word)
                else:
                    print(f"{person.get_name()}의 답: (틀림!) 벌칙 1잔~ 🍺")
                    person.set_count(person.get_count() + 1)

        if game_continue:
            cont = input("\n게임 계속? (y/n): ").strip().lower()
            if cont != "y":
                print("🍺 훈민정음 게임 종료! 🍺")
                break



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