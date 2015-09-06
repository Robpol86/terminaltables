# Contributing

Everyone that wants to contribute to the project should read this document.

## Getting Started

You may follow these steps if you wish to create a pull request. Fork the repo and clone it on your local machine. Then
in the project's directory:

```bash
virtualenv env  # Create a virtualenv for the project's dependencies.
source env/bin/activate  # Activate the virtualenv.
pip install tox  # Install tox, which runs linting and tests.
tox  # This runs all tests on your local machine. Make sure they pass.
```

You can ignore `InterpreterNotFound` if you see any. However you shouldn't see any `commands failed` from tox.

## Consistency and Style

Keep code style consistent with the rest of the project. Some suggestions:

1. **Write tests for your new features.** `if new_feature else` **Write tests for bug-causing scenarios.**
2. Write docstrings for all classes, functions, methods, modules, etc.
3. Document all function/method arguments and return values.
4. Document all class variables instance variables.
5. Documentation guidelines also apply to tests, though not as strict.
6. Keep code style consistent, such as the kind of quotes to use and spacing.
7. Don't use `except:` or `except Exception:` unless you have a `raise` in the block. Be specific about error handling.
8. Don't use `isinstance()` (it breaks [duck typing](https://en.wikipedia.org/wiki/Duck_typing#In_Python)).

## Thanks

Thanks for fixing bugs or adding features to the project!
