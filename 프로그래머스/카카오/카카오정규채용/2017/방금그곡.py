def code_change(music):
    music = music.replace("A#", 'a')
    music = music.replace("C#", 'c')
    music = music.replace("D#", 'd')
    music = music.replace("G#", 'g')
    music = music.replace("F#", 'f')
    return music


def time_check(s, e):
    h1, m1 = map(int, s.split(':'))
    h2, m2 = map(int, e.split(':'))
    return (h2*60+m2)-(h1*60+m1)


def solution(m, musicinfos):
    m = code_change(m)
    n = 0
    answer = []
    while musicinfos:
        n += 1
        start, end, title, melody = musicinfos.pop(0).split(',')
        record = time_check(start, end)
        melody = code_change(melody)
        song = ''

        for i in range(record):
            song += melody[i % len(melody)]

        if m in song:
            answer.append([record, title, n])

    if len(answer) != 0:
        answer = sorted(answer, key=lambda x: (-x[0], x[2]))
        return answer[0][1]
    else:
        return "(None)"
