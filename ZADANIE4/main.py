import numpy as np
import pandas as pd

def create_and_filter_data():
    """
    1) Wygeneruj tablicę numpy z losowymi liczbami całkowitymi.
    2) Umieść je w DataFrame (np. kolumny ['A', 'B']).
    3) Odfiltruj wiersze, w których kolumna 'A' spełnia pewien warunek (np. > 50).
    4) Zwróć przefiltrowany DataFrame.
    """
    np.random.seed(123)

    # Generowanie losowej tablicy 10x2 z zakresu 0-100
    arr = np.random.randint(0, 100, size=(10, 2))

    # Konwersja do DataFrame z nazwami kolumn
    df = pd.DataFrame(arr, columns=['A', 'B'])

    # Filtrowanie: wybierz wiersze, gdzie A > 50
    filtered_df = df[df['A'] > 50]

    return filtered_df

if __name__ == '__main__':
    # Przykładowe wywołanie
    result_df = create_and_filter_data()
    print("Otrzymany DataFrame (A > 50):")
    print(result_df)
