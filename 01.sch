v 20130925 2
C 40000 40000 0 0 0 title-B.sym
C 50700 46300 1 90 0 resistor-2.sym
{
T 50700 46500 5 10 1 1 0 0 1
value=8
T 50700 46800 5 10 1 1 0 0 1
refdes=R2
T 50700 46300 5 10 0 1 0 0 1
device=RESISTOR
}
C 49200 47200 1 180 0 resistor-2.sym
{
T 48700 46800 5 10 1 1 0 0 1
value=3
T 48700 47300 5 10 1 1 0 0 1
refdes=R1
T 49200 47200 5 10 0 1 0 0 1
device=RESISTOR
}
N 48300 47100 47000 47000 4
{
T 48000 47200 5 10 1 1 0 0 1
netname=1
}
N 50600 47200 49200 47100 4
{
T 50300 47200 5 10 1 1 0 0 1
netname=2
}
N 47000 45900 50600 46300 4
{
T 48800 46100 5 10 1 1 0 0 1
netname=0
}
N 47000 45900 47000 46300 4
C 46800 47000 1 270 0 battery-1.sym
{
T 47700 46700 5 10 0 0 270 0 1
device=BATTERY
T 47300 46700 5 10 1 1 270 0 1
refdes=v1
T 48100 46700 5 10 0 0 270 0 1
symversion=0.1
T 46600 46500 5 10 1 1 0 0 1
value=2.7
}
