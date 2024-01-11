=====
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/ageitgey/face_recognition/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/wasimakh2/face_recognition/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `face_recognition` for local development.

1. Fork the `face_recognition` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/face_recognition.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv face_recognition
    $ cd face_recognition/
    $ tox
    $ flake8 --ignore=E501,W503 face_recognition tests
    $ flake8 --ignore=E501,W503 --max-complexity=10 --max-line-length=127 --inline-quotes=single --multiline-quotes=double --docstring-quotes=double face_recognition tests
    $ pytest --all-versions

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

95: 1. The pull request should include tests and ensure that the tests pass for all supported Python versions. Additionally, ensure that the changes pass flake8 and pytest. Reference the `tests` directory.
61: 
62:     
63:     
64:     
65: 
66:    To install flake8 and tox, use the following command:


    $ python setup.py test
    $ pytest --all-versions
    $ tox

    $ tox
85:     The pull request should work for all supported Python versions.
86:     $ git push origin name-of-your-bugfix-or-feature
87: 

   To install flake8 and tox, use the following commands:

```
=======
.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~
Report bugs at https://github.com/wasimakh2/face_recognition/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/wasimakh2/face_recognition/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `face_recognition` for local development.

1. Fork the `face_recognition` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/face_recognition.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv face_recognition
    $ cd face_recognition/
    $ tox
    $ flake8 --ignore=E501,W503 face_recognition tests
    $ flake8 --ignore=E501,W503 --max-complexity=10 --max-line-length=127 --inline-quotes=single --multiline-quotes=double --docstring-quotes=double face_recognition tests
    $ pytest --all-versions

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

95: 1. The pull request should include tests and ensure that the tests pass for all supported Python versions.
61: 
62:     
63:     
64:     
65: 
66:    To install flake8 and tox, use the following command:

    $ python setup.py test
    $ tox
85:     The pull request should work for Python 2.7, 3.5, 3.6, 3.7, 3.8, and PyPy.
86:     $ git push origin name-of-your-bugfix-or-feature
87: 

   To install flake8 and tox, use the following commands:

```

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/wasimakh2/face_recognition/issues.

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/ageitgey/face_recognition/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/ageitgey/face_recognition/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `face_recognition` for local development.

1. Fork the `face_recognition` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/face_recognition.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv face_recognition
    $ cd face_recognition/
    $ tox
    $ flake8 --ignore=E501,W503 face_recognition tests
    $ flake8 --ignore=E501,W503 --max-complexity=10 --max-line-length=127 --inline-quotes=single --multiline-quotes=double --docstring-quotes=double face_recognition tests
    $ python -m unittest discover -t . -s tests

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

95: 1. The pull request should include tests and ensure that the tests pass for all supported Python versions.
61: 
62:     
63:     
64:     
65: 
66:    To install flake8 and tox, use the following command:

    $ flake8 --ignore=E501,W503 face_recognition tests
    $ python setup.py test
    $ tox
85:     The pull request should work for Python 2.7, 3.5, 3.6, 3.7, 3.8, and PyPy.
86:     $ git push origin name-of-your-bugfix-or-feature
87: 

   To install flake8 and tox, use the following commands:

```

```

```
 --all-versions
```

6. Commit your changes and push your branch to GitHub:

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature
    
    Add a new guideline to ensure that the code passes flake8 checks, specify the supported Python versions, and the need to check tests for all versions.
85:     85:     The pull request should include tests and ensure that the tests pass for all supported Python versions. Additionally, ensure that the changes pass flake8 and pytest. Reference the `tests` directory, the `test_something.py` file created in the previous step, and use the following flake8 command:
       $ flake8 --ignore=E501,W503 face_recognition tests
86:     $ git push origin name-of-your-bugfix-or-feature
87: 

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests and ensure that the tests pass for all supported Python versions. Additionally, ensure that the changes pass flake8 and pytest. Reference the `tests` directory, the `test_something.py` file created in the previous step, and use the following flake8 command:
       $ flake8 --ignore=E501,W503 face_recognition tests
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.
   Additionally, ensure that the changes pass flake8 and tests.
3. The pull request should work for all supported Python versions. Check
   https://github.com/wasimakh2/face_recognition/pull_requests  and make sure that the tests pass for all supported Python versions.
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests, use the following command and options:     $ pytest --all-versions


    pytest --all
