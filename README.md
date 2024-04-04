# How to start the project
1. Clone the repository `git clone git@github.com:maciej-szok/projects-api.git`
2. `cd` into the application directory: `cd projects-api`
3. Start the application `./start.sh`
    - This script will:
      - create an `.env` file based on `.env.local`,
      - load the `.env` file,
      - build a docker container containing the application,
      - start containers using `docker compose`,
      - print out some useful info.

# How to run tests
1. `cd` into the application directory: `cd projects-api`
2. Run the tests `./test.sh`
   - This script will:
     - build the application in dev mode,
     - start the application,
     - run the tests,
     - stop the application.

# Documentation
Project will automatically generate OpenAPI documentation, 
by default available at [http://0.0.0.0:3000/docs](http://0.0.0.0:3000/docs).

### Project Structure (request & response bodies)
```
{
	"name": "Example project", # up to 32 characters
	"description": null, # optional; can be null or a string (up to 2000 characters)
	"area_of_interest": { # any fields under area_of_interest are optional
		"field1": "oka"
	},
	"id": 1, # unique identifier
	"date_range": {
		"lower": "2024-04-02", # date format: YYYY-MM-DD, lower is inclusive
		"upper": "2024-04-03"  # same as above, but upper is exclusive
	}
}
```


# TODO
* [x] Design the REST API and decide on architecture
* [x] Basic API
* [x] Add Dockerfile
* [x] Add tests
* [x] Add start instructions
* [x] Write a nice README
* [x] Test manually
* [ ] Test using siege
