[![Build Status](https://ghenkins.bigdatalab.ibm.com/job/Watson-Continuous-Delivery/job/hello-world-flask/job/master/badge/icon)](https://ghenkins.bigdatalab.ibm.com/job/Watson-Continuous-Delivery/job/hello-world-flask/job/master/)

# hello-world-flask

This is an attempt to make a smaller and less resource-intense version of the
csf-hello-world.

This is written in Python and makes use of the popular
[Flask](http://flask.pocoo.org/) framework.

# Building
This project uses a multistage Docker build to define a base image with only
the necessary dependencies to run the application in a production environment.
The three other containers inherit from this base container as follows:

## final
This is the final production image. This image merely has the source tree
copied into it and sets up Gunicorn as the entrypoint for the application. This
uses Gunicorn since the Flask internal web server is suitable only for local
development.

## test
This image is used to run the unit tests and thus, has the necessary testing
dependencies installed.

## localdev
Because Gunicorn does not detect filesystem updates and restart its service
accordingly, we use the Flask local development server for this image and set
a few environment variables to better control its behavior.

# Local testing / development

There are helper scripts found in the `scripts/` directory to locally build the
container images and set up volume mounts for faster testing / development.
Their names should be self-describing, but to describe them further:

- `start-local-dev` - This starts a local Flask server that creates a volume
  mount for the local directory and forwards port 5000 into the container. This
  also listens to the local filesystem and will reload the local dev server
  when any files change.
- `run-tests` - This creates the volume mount and runs all of the tests using
  the Nose test running framework with a minimal number of options. A similar
  invocation is used in the CI environment with additions for code coverage and
  test performance analysis. These operations take additional time which is why
  they are excluded from the local development environment.
- `start-prod-image` - This creates and runs the final production image and
  sets up port forwarding to 5000.

## To get started:

1. Clone this repo.
2. Run the `scripts/start-local-dev`.
3. Open your browser to http://localhost:5000.
