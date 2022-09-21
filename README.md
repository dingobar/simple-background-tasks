# Background tasks with asyncio

It's simple and stateless. There is no cron schedule and no timeouts - just some coroutine being
called over and over again. Your coroutine can run for 1ms or 1 year, it doesn't matter. It will run
until it fails or succeeds, wait for a number of seconds, then start again. A use case could be to
refresh a cache every so often based on a slow 3rd party service, or calculate some prometheus
metrics that aren't strictly related to the API itself, whatever you want. I have tested it out in
production and it seems surprisingly reliant.

**The only thing you have to make sure of is that your coroutine is idempotent.**

I wanted to create this because I wanted to build a FastAPI app that runs some task periodically in
the background. I guess it can be used for anything though, as long as the app is asynchronous.

See [the examples](./examples).

## Backlog

- Publish as python package on pypi
