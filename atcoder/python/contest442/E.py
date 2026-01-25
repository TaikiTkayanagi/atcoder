# E - Laser Takahashi（外積を使った解法）
# 問題概要：
# - Takahashiが原点にいて、N匹のモンスターが各座標に配置されている
# - 各クエリで、モンスターA_jの方向から時計回りにモンスターB_jの方向まで回転
# - その間に視線が通過した全てのモンスターを破壊する
# - 何匹破壊されるかを求める

# 解法のポイント：
# 1. 外積（cross product）を使って方向を判定
# 2. 外積 = x1*y2 - x2*y1
# 3. 外積の符号で2つのベクトルの位置関係がわかる
#    - 正: ベクトル2はベクトル1から反時計回りの方向
#    - 負: ベクトル2はベクトル1から時計回りの方向
#    - 0: 同じ方向または正反対の方向

N, Q = map(int, input().split())

# 各モンスターの座標を保存
monsters = []
for i in range(N):
    x, y = map(int, input().split())
    monsters.append((x, y))


def cross_product(x1, y1, x2, y2):
    """
    2つのベクトル(x1, y1)と(x2, y2)の外積を計算

    外積 = x1*y2 - x2*y1

    外積の意味：
    - 正の値: ベクトル2はベクトル1から見て反時計回りの方向
    - 負の値: ベクトル2はベクトル1から見て時計回りの方向
    - 0: 同じ方向または正反対の方向
    """
    return x1 * y2 - x2 * y1


def in_clockwise_range(start, end, target):
    """
    startからendまで時計回りに回転するとき、
    targetがその範囲内にあるかを判定

    判定方法：
    1. startからtargetへの外積を計算
       - 負または0なら、targetはstartから時計回り側にある
    2. endからtargetへの外積を計算
       - 正または0なら、targetはendから反時計回り側にある
    3. 両方を満たせば、targetは時計回りの範囲内

    ただし、startからendまでの回転が180度を超える場合は
    判定を反転させる必要がある
    """
    sx, sy = start
    ex, ey = end
    tx, ty = target

    # startからtargetへの外積
    cross_st = cross_product(sx, sy, tx, ty)
    # startからendへの外積
    cross_se = cross_product(sx, sy, ex, ey)
    # endからtargetへの外積
    cross_et = cross_product(ex, ey, tx, ty)

    # startとendが同じ方向の場合（外積が0）
    if cross_se == 0:
        # targetも同じ方向なら範囲内
        return cross_st == 0

    # startからendが時計回り（外積が負）の場合
    # この場合は180度未満の時計回り
    if cross_se < 0:
        # targetがstartから時計回り側（cross_st <= 0）かつ
        # targetがendから反時計回り側（cross_et >= 0）なら範囲内
        return cross_st <= 0 and cross_et >= 0
    else:
        # startからendが反時計回り（外積が正）の場合
        # 実際には180度を超える時計回りを意味する
        # （時計回りで遠回りしている状態）
        # targetがstartから時計回り側（cross_st <= 0）または
        # targetがendから反時計回り側（cross_et >= 0）なら範囲内
        return cross_st <= 0 or cross_et >= 0


# 各クエリを処理
for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1  # 0-indexedに変換
    b -= 1

    # 開始位置と終了位置のモンスターの座標を取得
    start_pos = monsters[a]
    end_pos = monsters[b]

    # 各モンスターが範囲内にあるかチェック
    count = 0
    for monster in monsters:
        if in_clockwise_range(start_pos, end_pos, monster):
            count += 1

    print(count)
