for i in 1 2 3 4
do
    n=0
    if [ $i -eq 1 ]
    then
        n=300
    fi
    if [ $i -eq 2 ]
    then
        n=1000
    fi
    if [ $i -eq 3 ]
    then
        n=10000
    fi
    if [ $i -eq 4 ]
    then
        n=10000
    fi
    ./main.py "pacmaze$i.txt" 0.1 0.1 $n
    ./main.py "pacmaze$i.txt" 0.1 0.5 $n
    ./main.py "pacmaze$i.txt" 0.1 0.9 $n
    ./main.py "pacmaze$i.txt" 0.5 0.1 $n
    ./main.py "pacmaze$i.txt" 0.5 0.5 $n
    ./main.py "pacmaze$i.txt" 0.5 0.9 $n
    ./main.py "pacmaze$i.txt" 0.9 0.1 $n
    ./main.py "pacmaze$i.txt" 0.9 0.5 $n
    ./main.py "pacmaze$i.txt" 0.9 0.9 $n
done