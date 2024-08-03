def greedy_algorithm(items, budget):
    # Сортуємо предмети за співвідношенням калорії/вартість у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    chosen_items = []
    
    for item, info in sorted_items:
        if budget >= info['cost']:
            budget -= info['cost']
            total_calories += info['calories']
            chosen_items.append(item)
    
    return chosen_items, total_calories

def dynamic_programming(items, budget):
    # Створюємо список для зберігання максимальної кількості калорій, яку можна отримати при кожному бюджеті
    dp = [0] * (budget + 1)
    
    for item, info in items.items():
        cost = info['cost']
        calories = info['calories']
        # Проходимо в зворотному порядку, щоб уникнути використання одного й того ж предмету більше одного разу
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories

    # Щоб знайти вибрані предмети, повертаємося по масиву dp
    current_budget = budget
    chosen_items = []
    for item, info in items.items():
        cost = info['cost']
        calories = info['calories']
        if cost <= current_budget and dp[current_budget] == dp[current_budget - cost] + calories:
            chosen_items.append(item)
            current_budget -= cost
    
    return chosen_items, dp[budget]

# Приклад предметів і бюджету
items = {
    "піца": {"cost": 50, "calories": 300},
    "гамбургер": {"cost": 40, "calories": 250},
    "хот-дог": {"cost": 30, "calories": 200},
    "пепсі": {"cost": 10, "calories": 100},
    "кола": {"cost": 15, "calories": 220},
    "картопля": {"cost": 25, "calories": 350}
}

budget = 100

# Тестування обох функцій
greedy_result, greedy_calories = greedy_algorithm(items, budget)
dp_result, dp_calories = dynamic_programming(items, budget)

print("Результат жадібного алгоритму:")
print("Вибрані предмети:", greedy_result)
print("Загальна кількість калорій:", greedy_calories)

print("\nРезультат динамічного програмування:")
print("Вибрані предмети:", dp_result)
print("Загальна кількість калорій:", dp_calories)
