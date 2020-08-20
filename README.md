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
* **More extensive tests** - some exemplary tests are present (and were used for test-driven development), but there should, of course, be more extensive testing in place
* **Thorough production settings** - some very obvious settings were adapted for the [live instance](#live-instance), but most are still identical to the ones for the local server. In a real-world application, this would introduce security (and other) issues
