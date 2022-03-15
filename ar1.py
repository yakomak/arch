# Тут буду разные файлы выкладывать - архив

# файл ar1.py - создаю 15 марта 2022 года около 14:53

# что-то по числам Фибоначи

n=1
for i in sys.modules:
 print(str(n)+') '+i)
 n+=1
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
for i in fib():
    print(i)
for i in fib():
    print(str(n)+') '+str(i)+'<br>')
    n+=1
    
    
#

#-2-----------------------------------------------
music/  Top-level package
  __init__.py      Initialize the music package
 formats/ Subpackage for file conversions
 __init__.py
 wavread.py
 wavwrite.py
 aiffread.py
 aiffwrite.py
 auread.py
 auwrite.py
 ...
 effects/ Subpackage for sound effects
 __init__.py
 echo.py
 surround.py
 reverse.py
 ...
 filters/ Subpackage for filters __init__.py equalizer.py vocoder.py karaoke.py ...
Источник: https://pythonim.ru/osnovy/package-python
#-3-----------------------------------------------

#-4-----------------------------------------------

#-5-----------------------------------------------

#-6-----------------------------------------------

#-7-----------------------------------------------

#-8-----------------------------------------------
