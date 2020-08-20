## Ghibli coding challenge
This Django micro-project was built to answer the coding challenge encountered during a hiring process. It uses the unofficial [Ghibli movie API](https://ghibliapi.herokuapp.com/) to retrieve basic movie and character data, perform simple relationship association on them and present them in a straigh-forward minimalistic frontend.


### Installation
This project comes with a `Makefile`. It is recommended to use a Python virtual environment:
```bash
$ python -m venv venv
[...]
$ . venv/bin/activate
```

The requirements can be installed via the Makefile:
```bash
$ make install
```


### Running tests

Automated tests (including a test coverage report and PEP8 compliance check) are available via the Makefile:
```bash
$ make tests
```


### Local server

To run the project locally, run:
```bash
$ make run-local
```

A list of Ghibli movies and their associated characters is available under the root URL (`localhost:8000/` by default).

To view the `404` page, visit any other route (e.g. `localhost:8000/help-i-am-lost/`).

To view the error page, it's easiest to disable your network connection (and wait one minute for the cached data to become stale, in case you've already made requests to the server).


### Live instance

A live instance of this project can be accessed at [ghibli.runhorst.dev](https://ghibli.runhorst.dev/).

The live instance runs on gunicorn behind an SSL-enabled Apache reverse proxy.


### Coding challenge limitations
These are things that should and would have been handled differently outside of a coding challenge:

* **Proper static files management** - currently, there is no need for static files (as the minimal styling that was added was embedded directly into the HTML)
* **Deserialization of Ghibli API responses** - it would be nice to properly deserialize the API responses into objects (rather than operating on the raw JSON), although there is no real benefit to this in the current state of the project
* **Image sources** - The images used should be self-hosted (and their usage rights should be clarified)
* **Proper caching backend** - opposed to a DatabaseCache in a local SQLite file
* **More extensive tests** - some exemplary tests are present (and were used for test-driven development), but there should, of course, be more extensive testing in place
* **Thorough production settings** - some very obvious settings were adapted for the [live instance](#live-instance), but most are still identical to the ones for the local server. In a real-world application, this would introduce security (and other) issues
* **Proper version control** - this project was developed exclusively on the `master` branch. In a project involving more complex features and more developers, feature branches should of course have been used
* **Async cache renewal** - depending on the expected traffic and the server resources available, it would be nice to have periodic async tasks (utilizing e.g. Celery) running in the background to automatically refresh the cached data from the Ghibli API, rather than refreshing the cashe on-demand as it is currently the case (or at least refresh the cache asynchronously _after_ each request so that the cache never becomes stale during high-traffic times)
* ~**CI** - it would be nice to have the tests (and the deployment of the live instance) be run automatically on pushing new commits~ The project now uses GitHub CI to automatically run tests on changes to `master` - it turns out the structure of the YAML file is very straightfoward and not too different from the Git**Lab** CI
* **Better documentation** - ... obviously
