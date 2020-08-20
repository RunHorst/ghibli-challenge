## Ghibli coding challenge

### Installation

### Running tests

### Live instance


### Coding challenge limitations
These are things that should and would have been handled differently outside of a coding challenge:

* **Proper static files management** - currently, there is no need for static files (as the minimal styling that was added was embedded directly into the HTML)
* **Deserialization of Ghibli API responses** - it would be nice to properly deserialize the API responses into objects (rather than operating on the raw JSON), although there is no real benefit to this in the current state of the project
* **Image sources** - The images used should be self-hosted (and their usage rights should be clarified)
* **Proper caching backend** - opposed to a DatabaseCache in a local SQLite file
