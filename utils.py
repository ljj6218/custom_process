from app import db
import traceback
session = db.session


def affair_decorator(a_func):
    def wrap_the_function():
        print("I am doing some boring work before executing view()")
        try:
            a_func()
        except:
            traceback.print_exc()
            session.rollback()
            raise
        else:
            session.commit()

        print("I am doing some boring work after executing view()")

    return wrap_the_function
