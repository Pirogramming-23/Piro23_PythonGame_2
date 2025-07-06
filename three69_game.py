import time
# 100개 까지 
def three69_pattern():
    patterns = []
    numList = list(range(1,101))
    for num in numList:
        clap = 0
        if num//10 in [3,6,9]:
            clap += 1
        if num%10 in [3,6,9]:
            clap += 1

        if clap:
            patterns.append("짝"*clap)
        else:
            patterns.append(str(num))
    return patterns

def game_369(current_player,game_people_list):
    print(f"3 6 9 게임을 시작합니다!!")
    # 인트로
    print("3 6 9!! 3 6 9!! 3 6 9!! 3 6 9!! \n")
    # 패턴 설정
    patterns = three69_pattern()
    player_index = game_people_list.index(current_player)

    for i in range(100):
        current_player = game_people_list[player_index%len(game_people_list)]
        user_input = input(f"{current_player.get_name()}님 차례!! (숫자 또는 짝): ")
        if user_input != patterns[i]:
            print(f"틀렸습니다 ㅠㅠ. 정답은: {patterns[i]}")
            print(f"{current_player.get_name()} 님은 하나 더 마신다!")
            current_player.set_count(current_player.get_count() + 1)
            current_player.life -= 1
            break
        else:
            print("잘했습니다! 이어서 다음으로...")

        player_index+=1