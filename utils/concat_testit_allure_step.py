import testit
import allure

def allure_testit_step(description):
    def wrapper(func):
        func = testit.step(description)(func)
        func = allure.step(description)(func)
        return func
    return wrapper
