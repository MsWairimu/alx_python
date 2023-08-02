print(', '.join(f'{i:02d}' for i in range(90) if any(str(j) in str(i) for j in range(1, 10))))
