from functools import partial

from colors import BLUE
from colors import GREEN
from colors import RED

from domain.word_url import English
from domain.word_url import TLD


DOT = RED('.')


longer_than = lambda length: partial(filter, lambda s: len(s) > length) # noqa
shorter_than = lambda length: partial(filter, lambda s: len(s) < length) # noqa
starts_with = lambda start: partial(filter, lambda s: s.startswith(start)) # noqa
ends_with = lambda end: partial(filter, lambda s: s.endswith(end) and s != end) # noqa
contains = lambda sub: partial(filter, lambda s: sub in s) # noqa


def apply(modifier):
    def decorator(function):
        def inner(*args, **kwargs):
            yield from modifier(function(*args, **kwargs))
        return inner
    return decorator


def conditions(iterator, *functions):
    gunction = iter
    for function in functions:
        gunction = apply(function)(gunction)
    yield from gunction(iterator)


def domain(s):
    left, right = s.split('.')
    return BLUE(left) + DOT + GREEN(right)


def iter_print(f, *args, **kwargs):
    for each in f(*args, **kwargs):
        print(domain(each))


@apply(sorted)
def the(tlds, words):
    words = set(words)
    for tld in tlds:
        if tld in words:
            yield 'the.' + tld


@apply(sorted)
def end(tlds, words):
    words = list(words)
    for tld in tlds:
        for word in words:
            if word.endswith(tld):  # and tld != word:
                yield word[: -len(tld)] + DOT + GREEN(tld)


@apply(sorted)
def double(tlds, words):
    words = set(words)
    for tld in tlds:
        for word in words:
            if word.endswith(tld):
                stub = word[: -len(tld)]
                if stub in words:
                    yield stub + DOT + GREEN(tld)


def main():
    tlds = set(TLD.get())
    words = set(English.get())

    # # The

    # iter_print(
    #     the,
    #     conditions(
    #         tlds,
    #         longer_than(2),
    #         shorter_than(10),
    #     ),
    #     words,
    # )

    # # Dog

    # iter_print(
    #     end,
    #     conditions(
    #         tlds,
    #         longer_than(1),
    #         shorter_than(10),
    #     ),
    #     conditions(
    #         words,
    #         contains('dog'),
    #     ),
    # )

    # Dog

    iter_print(
        double,
        conditions(
            tlds,
            longer_than(1),
            shorter_than(6),
        ),
        conditions(
            words,
            longer_than(3),
        ),
    )


if __name__ == '__main__':
    main()
