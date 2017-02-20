import threading


def threaded(function):
    def wrapper(*args, **kwargs):
        threading.Thread(target=function, args=args, kwargs=kwargs, daemon=True).start()

    return wrapper
