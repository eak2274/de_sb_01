import argparse

def main():
    # Создаем парсер
    parser = argparse.ArgumentParser(description="Sample script with params")
    
    # Добавляем аргументы
    parser.add_argument('--name', type=str, help='User name')
    parser.add_argument('--age', type=int, help='User age')
    parser.add_argument('--city', type=str, help='City of residence')
    
    # Парсим аргументы
    args = parser.parse_args()
    
    # Обрабатываем параметры
    print(f"Hi, {args.name}!")
    print(f"You are {args.age} years old.")
    print(f"Ты из города {args.city}.")

if __name__ == "__main__":
    main()
