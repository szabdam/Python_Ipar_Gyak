import time
def main():
    t = time.localtime()

    print(f"{t.tm_year}-{t.tm_mon}-{t.tm_mday}-{t.tm_hour}:{t.tm_min}:{t.tm_sec}")

    


if __name__ == "__main__":
    main()