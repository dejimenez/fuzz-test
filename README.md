# Fuzz Testing

Fuzzing permits us to find bugs by testing our application with randomized inputs. It helps the developer to improve the program’s robustness, security and overall quality. And since it’s mostly automated, it frees the developer to actually code while it runs. RESTLer gives us all those benefits.

There are two key points that indicate the benefits of this tool: Firstly, it can infer the requests dependencies, as to say that it can infer that a resource of a request is necessary as an input argument of another request; Secondly, it has a dynamic feedback, meaning the tool can analyze previous results to predict invalid request flows, ie.: Doing the requests X and Y, will provoke the refusal of request Z.

We are using [Microsoft RESTLer fuzzer](https://github.com/microsoft/restler-fuzzer) to fuzz the APIs

## There are 2 settings on RESTLer you can use

**Fuzz-lean:** execute once every endpoint+method in a compiled RESTLer grammar with a default set of checkers to see if bugs can be found quickly.

**Fuzz:** bug hunting — explore a RESTLer fuzzing grammar in smart breadth-first-search mode (deeper search mode) for finding more bugs. Warning: This type of fuzzing is more aggressive and may create outages in the service under test if the service is poorly implemented (e.g., fuzzing might create resource leaks, perf degradation, backend corruptions, etc.).

## Dependencies

In order to run this project it only requires [Docker](https://docs.docker.com/get-docker/) in your local computer.

## Run locally

```
docker compose up
```

 ## Test example

We are using [Pet Store API](https://petstore.swagger.io/) to test the RESTLer

### Steps

1. Create a test. In this case you must provide the url of the OpenApi documentation used by RESTLer to run the tests.
2. Trigger one of the tests (**Fuzz-lean** | **Fuzz**).
3. Show the results of the tests

## References

[Youtube video explaining how RESTLer works](https://www.youtube.com/watch?v=FYmiPoRwEbE&t=1207s)