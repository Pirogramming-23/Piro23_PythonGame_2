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

def game_369(player,current_player,game_people_list):
    print(f"3 6 9 게임을 시작합니다!!")
    # 인트로
    print("3 6 9!! 3 6 9!! 3 6 9!! 3 6 9!! \n")
    # 패턴 설정
    patterns = three69_pattern()
    player_index = game_people_list.index(current_player)
    
    for i in range(100):
        current_player = game_people_list[player_index % len(game_people_list)]
        correct_answer = patterns[i]

        # 실제 사용자면 input, 아니면 90% 확률로 정답 자동 생성
        if current_player == player:
            user_input = input(f">> {current_player.get_name()}님 차례: ").strip()
        else:
            is_correct = random.random() < 0.9
            if is_correct:
                user_input = correct_answer
            else:
                user_input = str(i + 1) if correct_answer != str(i + 1) else "짝"
            print(f">> {current_player.get_name()}님 차례: {user_input}")
            time.sleep(1)

        # 정답 체크
        if user_input != correct_answer:
            print(f" X 틀렸습니다 ㅠㅠ. 정답은: {correct_answer}")
            print(f"{current_player.get_name()} 님은 하나 더 마신다!\n")
            current_player.set_count(current_player.get_count() + 1)
            current_player.life -= 1
            break
        else:
            print(f"{current_player.get_name()} 정답!\n")
        player_index += 1



