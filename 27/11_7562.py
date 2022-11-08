from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1] # 8방향
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs():
    q = deque()
    q.append([x,y]) # 입력받은 x,y를 한번에 append함
    move[x][y] = 1
    
    while q:
        a,b = q.popleft()
        
        if a == goal_x and b == goal_y:
            print(move[goal_x][goal_y] - 1)
            return 
        
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < l and 0 <= ny < l and move[nx][ny] == 0:
                q.append([nx, ny])
                move[nx][ny] = move[a][b] + 1




T = int(input())

for _ in range(T):
    
    l = int(input())
    x,y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    
    move = [[0]*l for _ in range(l)]
    bfs()



    
    
    