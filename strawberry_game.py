import time 
# [['X', 'X', 'X', '딸기'], ['X', 'X', '딸기', '딸기'], ['X', '딸기', '딸기', '딸기'], ['딸기', '딸기', '딸기', '딸기'], ['딸기', '딸기', '딸기', '딸기', 'X', 'X', 'X', '딸기'], ['딸기', '딸기', '딸기', '딸기', 'X', 'X', '딸기', '딸기'], ['딸기', '딸기', '딸기', '딸기', 'X', '딸기', '딸기', '딸기'], ['딸기', '딸기', '딸기', '딸기', '딸기', '딸기', '딸기', '딸기']]
def strawberry_pattern():
    patterns = []
    for position in range(1,9):
        if position<=4:
            pattern = ["X"]*4
            for i in range(position):
                # 1=>3 / 2=>2,3 / 3=>1,2,3 / 4=>0,1,2,3
                pattern[3-i] = "딸기"
        else:
            pattern = ["X"]*8
            for i in range(4):
                pattern[i] = "딸기"
            # 5=>7 / 6=>6,7 / 7=>5,6,7 / 8=>4,5,6,7
            for i in range(position-4):
                pattern[7-i] = "딸기"
        patterns.append(pattern)
    return patterns

def print_rhythm(pattern):
    for beat in pattern:
        print(beat, end=' ', flush=True)
        time.sleep(0.3)
    print()

def strawberry_game(current_player,game_people_list):
    print(f"딸기 게임을 시작합니다!!")
    # 룰 소개
    # 인트로
    print("딸기가 좋아~ 딸기가 좋아~ 딸기! 딸기! 딸기!딸기!딸기\n")
    # 패턴 설정
    patterns = strawberry_pattern()
    pattern_count = 0
    player_index = game_people_list.index(current_player)

    while True: 
        current_player = game_people_list[player_index%len(game_people_list)]
        pattern = patterns[pattern_count%8]
        user_input = input(f"{current_player.get_name()}님 차례!! 정확한 박자에 딸기를 입력해주세요 (예: 1번 - X X X 딸기): ").replace(" ","").lower()
        pattern = ''.join(pattern).lower()
        if user_input != pattern:
            print("틀렸습니다 ㅠㅠ. 정답은: ",end="")
            print_rhythm(pattern.upper())
            print(f"{current_player.get_name()} 님은 하나 더 마신다!")
            current_player.set_count(current_player.get_count() + 1)
            current_player.life -= 1
            break
        else:
            print("잘했습니다! 이어서 다음으로...")

        pattern_count += 1
        player_index+=1