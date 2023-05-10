


# """Write a decorator that ensures a function is only called by users with a specific role."""
#
#
# def is_admin(func):
#     def wrapper(*args, **kwargs):
#         if kwargs.get('user_type') != 'admin':
#             raise ValueError('Permission denied')
#         return func(*args, **kwargs)
#     return wrapper



"""Write a decorator that wraps a function in a try-except block and print an error if error has happened"""


# def catch_errors(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except KeyError as e:
#             print(f'Found 1 error during execution of your function: KeyError - {str(e)}')
#         except Exception as e:
#             print(f'Found 1 error during execution of your function: {type(e).__name__} - {str(e)}')
#     return wrapper
#
#
# @catch_errors
# def some_function_with_risky_operation(data):
#     print(data['key'])




