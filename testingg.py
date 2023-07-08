def create_eg():
    eg = ExceptionGroup('Exception Group',
                        [FileNotFoundError('Not Found'),
                         FileNotFoundError('Not Found1'),
                         ValueError('name error')
                         ])
    raise eg


if __name__ == '__main__':
    # create_eg()

    try:
        create_eg()
    except* FileNotFoundError as eg:
        print(eg.exceptions)
    except* ValueError as eg:
        print(eg.exceptions)
