import matplotlib.pyplot as plt
import math

def draw_tree(ax, x, y, length, angle, level):
    if level == 0:
        return
    
    x_new = x + length * math.cos(math.radians(angle))
    y_new = y + length * math.sin(math.radians(angle))
    
    ax.plot([x, x_new], [y, y_new], color='green')
    
    # Розрахунок нової довжини і кутів для гілок
    нова_довжина = length * 0.7
    лівий_кут = angle + 45
    правий_кут = angle - 45
    
    # Рекурсивно малюємо ліву і праву гілки
    draw_tree(ax, x_new, y_new, нова_довжина, лівий_кут, level - 1)
    draw_tree(ax, x_new, y_new, нова_довжина, правий_кут, level - 1)

def main():
    # Введення рівня рекурсії від користувача
    рівень_рекурсії = int(input("Введіть рівень рекурсії: "))
    
    # Налаштування графіку
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Початкові параметри для дерева
    початкова_довжина = 100
    початковий_кут = 90
    
    # Малюємо дерево
    draw_tree(ax, 0, 0, початкова_довжина, початковий_кут, рівень_рекурсії)
    
    # Відображаємо графік
    plt.show()

if __name__ == "__main__":
    main()
