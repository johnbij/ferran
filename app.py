def some_function(safe_name):
    return f'recién subidos/{safe_name}'

try:
    # some code that could raise an exception
    pass
except Exception as exc:
    msg = 'An error occurred'
    print(f'{msg}: {str(exc)}')