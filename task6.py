def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості (від найбільшого до найменшого)
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0

    for name, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(name)
            total_cost += info["cost"]
            total_calories += info["calories"]
    
    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    costs = [items[name]["cost"] for name in item_names]
    calories = [items[name]["calories"] for name in item_names]

    # Створюємо таблицю DP
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнюємо таблицю
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-costs[i-1]] + calories[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    # Відновлюємо обрані страви
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(item_names[i-1])
            w -= costs[i-1]

    total_cost = sum(items[name]["cost"] for name in selected_items)
    total_calories = dp[n][budget]
    return selected_items, total_cost, total_calories

# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Приклад використання
budget = 100

greedy_result = greedy_algorithm(items, budget)
dynamic_result = dynamic_programming(items, budget)

print("Жадібний алгоритм:")
print(f"Обрані страви: {greedy_result[0]}")
print(f"Витрачено: {greedy_result[1]} грн, Калорії: {greedy_result[2]}\n")

print("Динамічне програмування:")
print(f"Обрані страви: {dynamic_result[0]}")
print(f"Витрачено: {dynamic_result[1]} грн, Калорії: {dynamic_result[2]}")
