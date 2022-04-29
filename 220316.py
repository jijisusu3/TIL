"""

보통 트리를 쓴다고 하면 따로 언급이 되어 있지 않는 이상
이진 트리로 접근하면 된다.
모든 노드를 3번 접근함 이건 전위, 중위, 후위일 때 모두 동일하며,
몇 번째 방문시에 기록할 지의 차이이다.

"""

def inorder(v):
    if v == 0: return
    # print(v) # 전위
    inorder(L[v])
    # print(v) # 중위
    inorder(R[v])
    # print(v) # 후위


