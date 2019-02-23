def h_decorate(func):
    def func_wrapper(name):
        return "<h1>" + func(name) + "</h1>"
    return func_wrapper


@h_decorate
def get_greeting(name):
    return "Welcome " + name + ", How are you!"


print(get_greeting("Ahmad"))
