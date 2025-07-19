x = 45


def with_error():
    raise Exception("Sorry, no impl")


try:
    print(x)
    with_error()
except Exception:
    print("Variable x is not defined")
except (RuntimeError, TypeError, NameError):
    pass
except:
    print("Something else went wrong")
finally:
    print('finally')


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

file_path = '../io/workfile.txt'
try:
    f = open(file_path, 'r')
except OSError:
    print('cannot open', )
else:
    print(file_path, 'has', len(f.readlines()), 'lines')
    f.close()

def this_fails():
    x = 1/0
try:
    this_fails()
    raise NameError('HiThere')
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
except NameError as err:
    print('Handling NameError: ', err)


def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
divide(2, 0)
# divide("2", "1")

def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)
try:
    f()
except Exception as e:
    print(f'caught {type(e)}: e, message: {e.args}')