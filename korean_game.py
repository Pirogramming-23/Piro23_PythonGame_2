import random
import time

def korean_game(player, game_people_list):
    word_list = [
        "오징어", "기러기", "토마토", "스위스", "사과", "바나나", "고양이", "강아지",
        "컴퓨터", "핸드폰", "커피", "맥주", "소주", "치킨", "피자", "토끼", "펭귄",
        "딸기", "수박", "포도", "귤", "감자", "고구마", "마우스", "키보드", "모니터",
        "텔레비전", "냉장고", "에어컨", "청소기", "선풍기", "신발", "모자", "가방",
        "시계", "안경", "노트북", "선물", "피로그래밍"]
    print("훈~민정~음 훈민정~음")
    time.sleep(1)
    print("\n🍺 훈민정음 게임을 시작합니다! 🍺")
    time.sleep(1)
    used_words = set()

    def get_chosung(word):
        chosung_list = []
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

    participants = []
    if player not in game_people_list:
        participants.append(player)
    participants.extend(game_people_list)

    answer_word = random.choice(word_list)
    chosung = get_chosung(answer_word)
    print(f"\n🍺 제시된 초성: {chosung}. 똑같은 단어는 안돼요~")

    for p in participants:
        print(f"\n현재 턴: {p.get_name()}")
        if p == player:  # 플레이어 차례
            user_word = input(f"{p.get_name()}님의 답변은? (패스하려면 Enter): ").strip()
            if user_word == "":
                time.sleep(1)
                print(f"{p.get_name()}님 패스! 벌칙 1잔~ 🍺")
                p.set_count(p.get_count() + 1)
                p.life -= 1
            elif get_chosung(user_word) == chosung and user_word not in used_words:
                time.sleep(1)
                print(f"{p.get_name()} 정답!")
                used_words.add(user_word)
            else:
                print(f"{p.get_name()} 오답! 벌칙 1잔~ 🍺")
                time.sleep(1)
                p.set_count(p.get_count() + 1)
                p.life -= 1
                
        else:  # AI 플레이어 차례
            possible_words = [w for w in word_list if get_chosung(w) == chosung and w not in used_words]
            if possible_words and random.random() > 0.3:  # 70% 확률로 정답
                comp_word = random.choice(possible_words)
                time.sleep(1)
                print(f"{p.get_name()}의 답: {comp_word} (정답!)")
                used_words.add(comp_word)
            else:
                time.sleep(1)
                print(f"{p.get_name()}의 답: (틀림!) 벌칙 1잔~ 🍺")
                p.set_count(p.get_count() + 1)
                p.life -= 1

    print("\n🍺 훈민정음 게임 종료! 🍺")