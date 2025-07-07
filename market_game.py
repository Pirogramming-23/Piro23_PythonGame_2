import random
import time

def market_game(player, game_people_list):
    print("\n📢 시장에 가면 게임을 시작합니다!")
    print("❗ 시장에 가면~‼️ 시장에 가면~‼️")
    print("❗ 규칙: 첫 사람은 '시장에 가면 사과도 있고'만 말하면 되고, 그 다음부터는 앞에 나온 모든 단어를 순서대로 말해야 합니다.")
    print("❗ 마지막은 반드시 '도 있고'로 끝나야 합니다!")

    items = []
    turn = 0

    while True:
        current_player = game_people_list[turn % len(game_people_list)]
        name = current_player.get_name()
        print()
        print(f"\n🎯 {name} 차례입니다.")
        print()

        # 플레이어 입력
        if current_player == player:
            user_input = input("→ '시장에 가면 ~~도 있고 ~~도 있고' 식으로 말하세요: ").strip()
        else:
            time.sleep(2)

            # AI가 말할 수 있는 단어 후보들
            ai_vocab = ["사과", "바나나", "귤", "수박", "딸기", "콩나물", "감자", "당근", "오이", "버섯"]

            if random.random() < 0.8:
                new_word = random.choice(ai_vocab)
                ai_items = items + [new_word]
                ai_phrase = "시장에 가면 " + "도 있고 ".join(ai_items) + "도 있고"
                time.sleep(1)
            else:
                ai_phrase = "시장에가면 아무말도 있고"

            print(f"🤖 AI({name}): {ai_phrase}")
            user_input = ai_phrase  # ✅ 무조건 정의됨
                                
        # 시작 문구 확인
        if not user_input.startswith("시장에 가면"):
            print(f"❌ '{name}'님, '시장에 가면'으로 시작하지 않았습니다! 🍺")
            print(f"{name} 마셔라~ 🍻\n")
            current_player.set_count(current_player.get_count() + 1)
            current_player.life -= 1
            return 

        # '도 있고'로 끝나는지 확인
        if not user_input.strip().endswith("도 있고"):
            print(f"❌ '{name}'님, 문장은 반드시 '도 있고'로 끝나야 합니다! 🍺")
            print(f"{name} 마셔라~ 🍻\n")
            current_player.set_count(current_player.get_count() + 1)
            current_player.life -= 1
            return

        # 아이템 추출
        phrase = user_input.replace("시장에 가면", "").strip()
        phrase = phrase[:-4].strip()  # '도 있고' 제거
        given_items = [p.strip() for p in phrase.split("도 있고") if p.strip()]

        # 검증
        if turn == 0:
            if len(given_items) != 1:
                print(f"❌ 첫 번째 차례는 단어 하나만 말해야 합니다! 🍺")
                print(f"{name} 마셔라~ 🍻\n")
                current_player.set_count(current_player.get_count() + 1)
                current_player.life -= 1
                return
        else:
            if len(given_items) != len(set(given_items)): 
                print(f"❌ 같은 단어를 두 번 이상 말했어요! 🍺")
                print(f"{name} 마셔라~ 🍻\n")
                current_player.set_count(current_player.get_count() + 1)
                current_player.life -= 1
                return
            
            if given_items[:-1] != items:
                print(f"❌ 순서를 틀렸거나 박자를 놓쳤습니다! 🍺")
                print(f"{name} 마셔라~ 🍻\n")
                current_player.set_count(current_player.get_count() + 1)
                current_player.life -= 1
                return

        # 성공
        items = given_items
        print(f"✅ {name} 정답!")
        turn += 1