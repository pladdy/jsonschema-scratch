Changelog
=========

Project changes based on `changelog <https://keepachangelog.com/en/1.0.0/>`_ format.

[0.2.2] - 2020-07-03
~~~~~~~~~~~~~~~~~~~~

Added
-----

- pre-commit

Changed
-------

- Bump versions with dephell

Fixed
-----

- Changelog history

Removed
-------

- bumpversion

[0.2.1] - 2020-06-16
~~~~~~~~~~~~~~~~~~~~

Fixed
-----

- Out of date docs

Added
-----

- badges for build, codacy, coverage, and license
- dephell which created a requirements.txt file

[0.2.0] - 2020-06-16
~~~~~~~~~~~~~~~~~~~~

Added
-----

- GET ``/schemas`` endpoint to view schemas
  - ?resolve parameter to resolve schema refs
- POST ``/validate`` endpoint that takes a ``?schema=<name of schema from /schemas>``
- Travis CI set up
