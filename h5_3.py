import requests
import timeit


url1 = 'https://drive.google.com/uc?export=download&id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh'
url2 = 'https://drive.google.com/uc?export=download&id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ'

response1 = requests.get(url1)
response2 = requests.get(url2)

text1 = response1.text
text2 = response2.text

# Вибір підрядків для пошуку
existing_substring = "Література"  # підрядок, який існує в тексті
non_existing_substring = "немає_такого_рядку"



# Алгоритм Кнута-Морріса-Пратта
def kmp_search(pattern, text):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = build_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1




# Алгоритм Боєра-Мура
def bm_search(pattern, text):
    def build_last(pattern):
        last = {}
        for i in range(len(pattern)):
            last[pattern[i]] = i
        return last

    last = build_last(pattern)
    m = len(pattern)
    n = len(text)
    i = m - 1
    j = m - 1

    if i > n - 1:
        return -1

    while i <= n - 1:
        if pattern[j] == text[i]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            lo = last.get(text[i], -1)
            i = i + m - min(j, 1 + lo)
            j = m - 1
    return -1




# Алгоритм Рабіна-Карпа
def rk_search(pattern, text):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1




# Функції для заміру часу виконання
def measure_time(func, text, pattern):
    return timeit.timeit(lambda: func(pattern, text), number=1)



# Вимірювання часу виконання для тексту 1
print("Text 1:")
print("KMP (existing):", measure_time(kmp_search, text1, existing_substring))
print("KMP (non-existing):", measure_time(kmp_search, text1, non_existing_substring))
print("BM (existing):", measure_time(bm_search, text1, existing_substring))
print("BM (non-existing):", measure_time(bm_search, text1, non_existing_substring))
print("RK (existing):", measure_time(rk_search, text1, existing_substring))
print("RK (non-existing):", measure_time(rk_search, text1, non_existing_substring))

# Вимірювання часу виконання для тексту 2
print("Text 2:")
print("KMP (existing):", measure_time(kmp_search, text2, existing_substring))
print("KMP (non-existing):", measure_time(kmp_search, text2, non_existing_substring))
print("BM (existing):", measure_time(bm_search, text2, existing_substring))
print("BM (non-existing):", measure_time(bm_search, text2, non_existing_substring))
print("RK (existing):", measure_time(rk_search, text2, existing_substring))
print("RK (non-existing):", measure_time(rk_search, text2, non_existing_substring))
