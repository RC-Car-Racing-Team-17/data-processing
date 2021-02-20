from multiprocessing import Pool

foo = {1: []}

def f(x):
    print('mid')
    return x

def main():
    pool = Pool()
    foo[1] = pool.map(f, range(100))
    pool.close()
    pool.join()
    print('finished')
    print(foo)

if __name__ == '__main__':
    main()