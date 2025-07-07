import time
import random
# 100개 까지 의 번호들로 정답 생성
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
        

def game_369(player, current_player, game_people_list):
    print(f"3 6 9 게임을 시작합니다!!")
    print("3 6 9!! 3 6 9!! 3 6 9!! 3 6 9!! \n")
    print("1부터 숫자를 하나씩 대면서, 3, 6, 9가 들어가는 숫자는 숫자 대신 '짝'을 쳐야 한다")

    patterns = three69_pattern()
    player_index = game_people_list.index(current_player)
    current_num = 1  # 시작 숫자

    while True:
        current_player = game_people_list[player_index % len(game_people_list)]
        correct_answer = patterns[current_num - 1]  # 0-based index

        # 유저/AI 구분
        if current_player == player:
            user_input = input(f">> {current_player.get_name()}님 차례: ").strip()
        else:
            is_correct = random.random() < 0.9
            if is_correct:
                user_input = correct_answer
            else:
                user_input = str(current_num) if correct_answer != str(current_num) else "짝"
            print(f">> {current_player.get_name()}님 차례: {user_input}")
            time.sleep(1)

        # 정답 체크
        if user_input != correct_answer:
            print(f"X 틀렸습니다 ㅠㅠ. 정답은: {correct_answer}")
            print(f"{current_player.get_name()} 님이 마신다!~~!!\n")
            current_player.set_count(current_player.get_count() + 1)
            current_player.decrease_life()
            break
        else:
            print(f"{current_player.get_name()} 정답!")

        print(f"{current_player.get_name()}은 (는) 지금까지 {current_player.get_count()}🍺 : 치사량까지 {current_player.get_life()}")            

        current_num += 1
        player_index += 1






