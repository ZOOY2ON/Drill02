from pico2d import *
import math

open_canvas()
move = True
go = 'RECT'

# 이미지 로딩
grass = load_image('grass.png')
character = load_image('character.png')

# === 사각형 ===

# 초기 위치 및 상태 변수 설정
x, y = 400, 90
way = 1  # 시작 방향을 처음 경로로 설정

# 이동 경로 정의: 사각형 경계를 따라 움직임
waypoints = [(400, 90), (750, 90), (750, 550), (50, 550), (50, 90)]

# === 원 ===

# 초기 위치 및 상태 변수 설정_원
center_x, center_y = 400, 300  # 원의 중심 좌표
radius = 210  # 원의 반지름
angle = 271  # 시작 각도

while move:

    if go == 'RECT' :
        character_point = (x,y)
        
        # waypoints 와 character_point(비교)
        if character_point != waypoints[way] :
            if way == 0 :
                x = x +5
            elif way == 1 :
                x = x+5
            elif way == 2 :
                y = y+5
            elif way == 3 :
                x = x-5
            elif way == 4 :
                y = y-5
                
        elif character_point == waypoints[way] :
            if way == 0 :
                go = 'CIRCLE'
                way = 1
            elif way == 4 :
                way = 0
            else :
                way = way+1

    elif go == 'CIRCLE' :
        angle += 1  # 각도를 1도씩 증가
        
        # 원의 중심에서 각도에 따라 이동
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))

        if y == 90 :
            go = 'RECT'
            x, y = 400, 90
        
    # 캐릭터 그리기
    clear_canvas()  # 이전 프레임 지우기
    character.draw(x, y)
    grass.draw(400, 30)
    update_canvas()
    #print(character_point)
    delay(0.01)

close_canvas()
