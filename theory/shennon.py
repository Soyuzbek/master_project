# -*- coding: utf-8 -*-

txt = 'Бир эле «Манасты» канчалаган зор китеп кылса болгудай. Бирок аны ким окуйт? Азыркы кымгуут заманда, информация адам башына жамгырдай жаап жаткан шартта илгерки айкерчиликтегидей болуп киши айлап-түндөп китеп окубайт. Экинчиден, роман варианты окуялардын тизмектелишине, сюжеттин тыкан курулушуна ыңгайлуу. Анан калса, «Манаста» канчалык апыртмалуулук, миф, жомок арбын болбосун табиятында абдан реалисттик чыгарма. Образдардын, мүнөздөрдүн түзүлүшүн эле аңдап көрөлүчү, окуялардын баяндалышын көрөлүчү, көбүнесе реалдуу турмуш, адамдардын реалдуу карымкатнашы, атүгүл психологиялык илме-кайыптык да бар.'
letters = []
for i in txt:
    if i not in letters:
        letters.append(i)

counts = []
for i in letters:
    count = 0
    for j in txt:
        if i == j:
            count += 1
    counts.append(count)

for i, j in sorted(zip(letters, counts), key=lambda x: x[1]):
    print(i)
print()
print()
for i, j in sorted(zip(letters, counts), key=lambda x: x[1]):
    print(j/len(txt))

print()
print()
for i, j in sorted(zip(letters, counts), key=lambda x: x[1]):
    print(-((j/len(txt))*np.log2(j/len(txt))))