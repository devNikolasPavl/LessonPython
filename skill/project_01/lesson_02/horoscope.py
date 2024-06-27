import random

times = ['утром', 'днем', 'вечером', 'ночью']
advices = ['ожидайте', 'предостерегайтесь', 'будьте открыты для']
promises = ['гостей', 'встреч', 'неожиданного праздника']

generated_prophecies = []
i = 0
while i < 5:
    j = 0
    forecast = []
    while j < 3:
        ti = random.randrange(0, len(times))
        ai = random.randrange(0, len(advices))
        pi = random.randrange(0, len(promises))

        t = times[ti]
        a = advices[ai]
        p = promises[pi]
        full_sentence = t.title() + ' ' + a + ' ' + p + '.'

        forecast.append(full_sentence)

        j = j + 1

    generated_prophecies.append(forecast[0] + ' ' + forecast[1] + ' ' + forecast[2])
    i = i + 1
