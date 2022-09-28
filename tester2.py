def get_kratni_and_dilnyki():
    counter = 1
    for i in range(1500, 2000000, 5):
        if i % 7 == 0:
            counter += 1
            print(counter, "<- num ->", i)
            if counter == 50:
                break

get_kratni_and_dilnyki()