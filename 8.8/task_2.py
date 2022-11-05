def my_zip_2(*args):
    length = min(len(element) for element in args)
    return (tuple(struct[index] for struct in list(args))
            for index in range(length))