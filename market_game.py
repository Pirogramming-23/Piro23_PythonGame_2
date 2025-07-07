def market_game(game_people_list):
    players = game_people_list
    item_list = []
    turn = 0
    current_player = players[turn % len(players)]
    print(f"\n{current_player.get_name()}가 좋아하는 시장 게임‼️ 시장 게임‼️ 게임 start~")
    print("시장에 가면~‼️ 시장에 가면~‼️")

    while True:
        current_player = game_people_list[turn % len(game_people_list)]
        name = current_player.get_name()

        print(f"\n🎤 {name} 차례입니다!")
        user_input = input("👉 문장을 말해주세요: ").strip()

        # 시작 문구 확인
        if not user_input.startswith("시장에 가면"):
            print(f"❌ '{name}'님, '시장에 가면'으로 시작하지 않았어요! 🍺 마셔요~")
            current_player.set_count(current_player.get_count() + 1)
            break

        # 문장에서 아이템들 추출
        phrase = user_input.replace("시장에 가면", "").strip()
        parts = [p.strip() for p in phrase.split("도 있고")]
        last = parts[-1].replace("이 있어", "").replace("가 있어", "").strip()
        items = parts[:-1] + [last]

        # 검증
        if turn == 0:
            if len(items) != 1:
                print(f"❌ 첫 차례엔 단어 하나만 말해야 해요! 🍺")
                current_player.set_count(current_player.get_count() + 1)
                break
        else:
            if items[:-1] != item_list:
                print(f"❌ 순서가 틀렸거나 빠뜨렸어요! 🍺")
                print(f"✅ 정답은: 시장에 가면 {'도 있고 '.join(item_list)}도 있고 {item_list[-1]}이(가) 있어")
                current_player.set_count(current_player.get_count() + 1)
                break

        # 정답 처리
        item_list = items
        print(f"✅ 잘했어요! 현재 목록: {', '.join(item_list)}")
        turn += 1
