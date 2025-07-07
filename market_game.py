def market_game(game_people_list):
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

        if not user_input.startswith("시장에 가면"):
            print(f"❌ '{current_player.get_name()}'님, '시장에 가면'으로 시작하지 않았어요! 🍺 마셔요~")
            current_player.set_count(current_player.get_count() + 1)
            continue  # 틀려도 한 잔만 마시고 계속 진행

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

        