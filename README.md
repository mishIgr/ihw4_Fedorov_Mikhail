# ihw4_Fedorov_Mikhail

## Первый класс сообщающихся сотояний.
Финальный вектор это класса равен (0.5384, 0.4615)
Запустим код для для 10 шагов по ЦМ:
```
[0.5, 0.5]
```
Теперь для 100 шагов по ЦМ:
```
[0.58, 0.42]
```
Теперь для 1000 шагов по ЦМ:
```
[0.528, 0.472]
```
Теперь для 10_000 шагов по ЦМ:
```
[0.5412, 0.4588]
```
Теперь для 100_000 шагов по ЦМ:
```
[0.53661, 0.46339]
```
Теперь для 1_000_000 шагов по ЦМ:
```
[0.538594, 0.461406]
```
Теперь для 10_000_000 шагов по ЦМ:
```
[0.5383379, 0.4616621]
```
Теперь для 100_000_000 шагов по ЦМ:
```
[0.53848406, 0.46151594]
```


## Второй класс сообщающихся сотояний.
Финальный вектор это класса равен (0.2877, 0.1712, 0.3745, 0.1664)
Запустим код для для 10 шагов по ЦМ:
```
[0.1, 0.4, 0.3, 0.2]
```
Теперь для 100 шагов по ЦМ:
```
[0.27, 0.23, 0.29, 0.21]
```
Теперь для 1000 шагов по ЦМ:
```
[0.29, 0.21, 0.321, 0.179]
```
Теперь для 10_000 шагов по ЦМ:
```
[0.2919, 0.2081, 0.3222, 0.1778]
```
Теперь для 100_000 шагов по ЦМ:
```
[0.28626, 0.21374, 0.32166, 0.17834]
```
Теперь для 1_000_000 шагов по ЦМ:
```
[0.285798, 0.214202, 0.321286, 0.178714]
```
Теперь для 10_000_000 шагов по ЦМ:
```
[0.285848, 0.214152, 0.3214151, 0.1785849]
```
Теперь для 100_000_000 шагов по ЦМ:
```
[0.28566759, 0.21433241, 0.32145262, 0.17854738]
```

## Вывод
Финальный вектор первого класса, посчитан верно. Это видно экспереминтально, при увеличении количества шагов значения получившегося вектора стремятся к финальному.
Со вторым так не получилось. В вычислениях была произвидена ошибка, матрица вероятносного перехода была написанна неверно. Но точно знаю, что получившийся вектор стрмится к финальному.
*Посчитав с правильной матрицей, финальный вектор получился (0.2857, 0.2142, 0.3214, 0.1785). Получилось, что вектор из программы как раз стремится к этому значению.*
