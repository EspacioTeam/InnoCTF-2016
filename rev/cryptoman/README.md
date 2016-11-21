Посмотрим на библиотечные вызовы:
```
% ltrace ./cryptoman
fopen("flag", "r")                                                       = 0
fseek(0, 0, 2, -4096 <no return ...>
--- SIGSEGV (Segmentation fault) ---
+++ killed by SIGSEGV +++
```
Прога хочет файл "flag". Создаём.
```
% touch flag
% ltrace ./cryptoman        
fopen("flag", "r")                                                       = 0x1d13010
fseek(0x1d13010, 0, 2, 0x7f1461a19330)                                   = 0
ftell(0x1d13010, 0x1d130f0, 0, 0x1d130f0)                                = 0
rewind(0x1d13010, 0x1d130f0, 0, 0x1d130f0)                               = 0x1d130f0
fread(0x7ffd4ba37e90, 0, 1, 0x1d13010)                                   = 0
fclose(0x1d13010)                                                        = 0
fopen("key", "r")                                                        = 0
fread(0x7ffd4ba37e90, 8, 1, 0 <no return ...>
--- SIGSEGV (Segmentation fault) ---
+++ killed by SIGSEGV +++
```
Теперь прога хочет файл "key".
```
% touch key
% ltrace ./cryptoman
fopen("flag", "r")                                                       = 0x1b72010
fseek(0x1b72010, 0, 2, 0x7fc5952ec330)                                   = 0
ftell(0x1b72010, 0x1b720f0, 0, 0x1b720f0)                                = 0
rewind(0x1b72010, 0x1b720f0, 0, 0x1b720f0)                               = 0x1b720f0
fread(0x7fff6a7da540, 0, 1, 0x1b72010)                                   = 0
fclose(0x1b72010)                                                        = 0
fopen("key", "r")                                                        = 0x1b72010
fread(0x7fff6a7da540, 8, 1, 0x1b72010)                                   = 0
fclose(0x1b72010)                                                        = 0
fopen("encrypted", "w")                                                  = 0x1b72010
fwrite("n\245}j\377\177", 0, 1, 0x1b72010)                               = 0
fclose(0x1b72010)                                                        = 0
+++ exited (status 0) +++
```
Прога хочет прочесть 8 байт из файла "flag". Любой каприз!..
```
% echo -n KEYKEYKE > key
```
В вызове fread запрошенный размер данных 0 скорее всего был получен предыдущими вызовами fseek и ftell. Файл "flag" пуст, поэтому из него читается 0 байт. Запишем туда немного чепухи
```
% echo veryplaintext > flag
% ltrace ./cryptoman
fopen("flag", "r")                                                       = 0x2293010
fseek(0x2293010, 0, 2, 0x7fc98154a330)                                   = 0
ftell(0x2293010, 0x22930f0, 0, 0x22930f0)                                = 14
rewind(0x2293010, 0x22930f0, 14, 0x22930f0)                              = 0x22930f0
fread(0x7ffd12f7c250, 14, 1, 0x2293010)                                  = 1
fclose(0x2293010)                                                        = 0
fopen("key", "r")                                                        = 0x2293010
fread(0x7ffd12f7c260, 8, 1, 0x2293010)                                   = 1
fclose(0x2293010)                                                        = 0
fopen("encrypted", "w")                                                  = 0x2293010
fwrite("`wyvou~pwvhnEYS1veryplaintext\n", 14, 1, 0x2293010)              = 1
fclose(0x2293010)                                                        = 0
+++ exited (status 0) +++
```
Действительно, теперь читаются все 14 байт.
Пора посмотреть, что происходит внутри
```
% gdb cryptoman
```
Включим удобный режим...
```
(gdb) layout regs
```
... и вперёд!
```
(gdb) start
Temporary breakpoint 1 at 0x400774
Starting program: /home/muxa/Documents/ICTF/crypto/1/cryptoman

Temporary breakpoint 1, 0x0000000000400774 in main ()
```
В окошке дизассемблера видны все библиотечные вызовы, выловленные ltrace. Нас интеремует функция encrypt. В неё передаются адреса, по которым записаны ключ (rdx), открытый текст (rsi), места под шифротекст (rdi) и длина шифруемого текста (rcx).
```
(gdb) break encrypt
(gdb) continue
```
Теперь исполняя инструкцию за инструкцией с помощью команды ni, несложно увидеть, что текст сперва xor'ится с ключом: ct[i] = t[i] ^ k[i%8], затем при помощи операций сдвига перемешивается в блоках по 4 байта следующим образом: 0->4 1->3 2->0 3->1, и напоследок ещё раз xor'ится с ключом. Из несложных уравнений, которые мне лень переписывать, следует возможность проверки с некоторой вероятностью гипотезы, что первые 8 байт открытого текста есть 'InnoCTF', и, если это вероятно, восстановить ключ и расшифровать всё сообщение. Для этого запускаем python:
```python
% ipython
ct - CipherText, t - Text
ct=bytearray(open('encrypted','rb').read())
t=bytearray(ord(i) for i in 'InnoCTF{')
```

Поскольку перестановки в каждом 4B блоке одинаковые, каждые 8B с текстом xor'ится одна и та же пара байт ключа. Получим эти пары:
```python
kk=[]
kk.append(ct[0]^t[2])
kk.append(ct[1]^t[3])
kk.append(ct[2]^t[1])
kk.append(ct[3]^t[0])
kk.append(ct[4]^t[6])
kk.append(ct[5]^t[7])
kk.append(ct[6]^t[5])
kk.append(ct[7]^t[4])
```

Проверим гипотезу о первых восьми байтах текста:
```python
from functools import reduce
0 == reduce(lambda a,b:a^b,ct[:4]+t[:4])
0 == reduce(lambda a,b:a^b,ct[:4]+t[4:8])
```
Возвращается true, в противном случае нужно было бы подбирать другие варианты текста

Люблю функциональщину =)
```python
print(
    ''.join(
        map(
            chr,
            (
                reduce(
                    lambda a,b:a+b,
                    (
                        (
                            (
                                ct[i+3]^kk[3],
                                ct[i+2]^kk[2],
                                ct[i+0]^kk[0],
                                ct[i+1]^kk[1],
                                ct[i+7]^kk[7],
                                ct[i+6]^kk[6],
                                ct[i+4]^kk[4],
                                ct[i+5]^kk[5]
                            ) 
                            for i in (0,8,16)
                        )))))))
```

Забираем флаг и радуемся =)

