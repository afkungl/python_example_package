Contribution guide
==================

Contributions are welcome to the project.
Before starting your own contribution, please consider the following checklist.

**Open issues** should be tracked on the Project board on Github.
Open a new issue (product backlog item or bug) before you start the implementation.

**Branching strategy:** We use the Gitflow branching strategy for development.
We use the *master* branch for releasing to production and the *dev* branch as the leading branhc for development.
For details consult this `site
<https://www.atlassian.com/de/git/tutorials/comparing-workflows/gitflow-workflow>`_
The number of the corresponding issue should be tracked in the name of the feature branch as described in the wikipage of the branching strategy.
For example: features/562843_add_new_brick.

**Codestyle:** Check your contribution for codestyle with pycodestyle (from the root of the repo)::

    pycodestyle path/to/my_file.py --config=tox.ini

Modify your contribution such that it passes this test.
Use google-style docstrings.
*Tipp:* Consider using GenAI-based chats and copilots, e.g. for writing docstrings and typhints.

**Linting:** Check your contribution for codestyle with pylint (from the root folder of the repo)::

    pylint path/to/my_file.py --config=pylintrc

Modify your contribution such that it passes this test.

**Test:** Write tests in the pytest framework. Navigate to the test folder and run the tests via pytest::

    pytest tests

You can also run single test files via pytest, for example::

    pytest tests/path/to/test.py

**Commit messages:** Use best practices as far as possible, e.g. `here
<https://www.gitkraken.com/learn/git/best-practices/git-commit-message>`_.
For example:

    - Use imperative verb form
    - Avoid unnecessary capitalization
    - Double check your spelling
    - Do not end commit message summaries with punctuation
    - example commit message:
        Fix edge-case in brick do-specific-step

**Documentation:** Document your changes in the documentation in *docs*.
We use the `sphinx tool <https://www.sphinx-doc.org/en/master/>`_ to create the docs.
Add your changes to the waiting for release section in *docs/releases.rst*.
Further, document it on other relevant pages.
If you look for inspiration and tipps for documentation, check out this `documentation guide <https://www.writethedocs.org/guide/>`_.

**Pull request:** Always add your contributions to the dev branch via pull requests.
There should be at least one required reviewer, who also has to approve the PR.
The PR should be merged via a squash-commit and the corresponding features branch deleted.
Finally, move the corresponding issue on the board to done.