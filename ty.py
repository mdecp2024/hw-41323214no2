
# 定義已知數據
initial_velocity_kmh = 300  # 初始速度，單位 km/h
final_velocity = 0          # 最終速度，單位 m/s
distance = 1500             # 距離，單位 m

# 第一步：將初始速度轉換為 m/s
initial_velocity = initial_velocity_kmh * (1000 / 3600)

# 第二步：使用公式計算加速度
acceleration = -(initial_velocity ** 2) / (2 * distance)

# 顯示結果
print(f"加速度為 {acceleration:.2f} m/s²")

