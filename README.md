# data-filtering
Filtering data using Pandas

Analiza ABPM

1.	Po PESEL, który będzie nazwą pliku (Patient name) będziemy wciągać surowe dane do naszej bazy danych (możemy kopiować plik CSV - z mojej strony metoda nie ma znaczenia).
2.	Do analizy nie bierzemy pomiarów mających inny znacznik niż „0” w pozycji „ERR” - error lub „EXC” - exclude
3.	Do naszej bazy danych chcemy, żeby system wyliczał i prezentował następujące parametry:
      a.	średnia i SD z całego okresu pomiaru dla: 
        i.	SYS (systolic= SBP)
        ii.	DIA (diastolic=DBP)
        iii.	PUL (pulse = HR)
        iv.	MAP (wg wzoru: DIA+1/3(SYS-DIA))
    b.	% wyników SYS (ładunek SBP) >130 z całego okresu pomiaru
    c.	% wyników DIA (ładunek DBP) > 80 z całego okresu pomiaru
    d.	średnia, SD, najmniejszy wynik (min.) i największy wynik (maks.) z okresu snu (między „SLEEP TIME” a "WAKE TIME"):
        i.	SYS (systolic= SBP)
        ii.	DIA (diastolic=DBP)
        iii.	PUL (pulse = HR)
        iv.	MAP (wg wzoru: DIA+1/3(SYS-DIA))
    e.	% wyników SYS (ładunek SBP) >120 z okresu snu
    f.	% wyników DIA (ładunek DBP) > 70 z okresu snu
    g.	średnia, SD, najmniejszy wynik (min.) i największy wynik (maks.) z okresu czuwania (między „WAKE TIME” a " SLEEP TIME"):
        i.	SYS (systolic= SBP)
        ii.	DIA (diastolic=DBP)
        iii.	PUL (pulse = HR)
        iv.	MAP (wg wzoru: DIA+1/3(SYS-DIA))
    h.	% wyników SYS (ładunek SBP) >135 z okresu czuwania
    i.	% wyników DIA (ładunek DBP) > 85 z okresu czuwania
    j.	średnią i SD z trzech pierwszych pomiarów
    k.	MS (Morning surge) dla SYS, DIA i MAP zgodnie ze wzorem: średnia z 2 godzin po „WAKE TIME” – średnia z najmniejszego wyniku z okresu snu (między „SLEEP TIME” a "WAKE TIME") i po 1 wyniku sąsiadującym
    l.	dipping dla SBP, DBP i MAP zgodnie ze wzorem: średnia z pomiarów w czasie czuwania (między „WAKE TIME” a " SLEEP TIME") – średnia z pomiarów w czasie snu (między „SLEEP TIME” a "WAKE TIME") / średnia z pomiarów w czasie czuwania (między „WAKE TIME” a " SLEEP TIME") * 100% 

UWAGA!
Jeśli WAKE TIME = czasowi pomiaru to pomiar jest zaliczany do okresu czuwania
Jeśli SLEEP TIME = czasowi pomiaru to pomiar jest zaliczany do okresu czuwania

