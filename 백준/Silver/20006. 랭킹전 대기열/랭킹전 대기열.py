# 입력 
p, m = map(int, input().split())

players = []
for _ in range(p):
    level_nick = input().split()
    level = int(level_nick[0])
    nickname = level_nick[1]
    players.append((level, nickname))

# 각 방은 [기준 레벨, 참가자 리스트] 형태로 저장
rooms = []

for level, nickname in players:
    room_found = False

    for room in rooms:
        base_level = room[0]
        participants = room[1]

        # 입장 조건: 정원이 안 찼고, 기준레벨 ±10 범위 안이면 입장
        if len(participants) < m and (base_level - 10) <= level <= (base_level + 10):
            participants.append((level, nickname))
            room_found = True
            break

    if not room_found:
        # 새로운 방 생성
        rooms.append([level, [(level, nickname)]])

# 출력
for room in rooms:
    participants = room[1]

    if len(participants) == m:
        print("Started!")
    else:
        print("Waiting!")

    # 사전순 정렬 
    for i in range(len(participants)):
        for j in range(i + 1, len(participants)):
            if participants[i][1] > participants[j][1]:
                participants[i], participants[j] = participants[j], participants[i]

    for player in participants:
        print(player[0], player[1])
