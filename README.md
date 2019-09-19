# RESTful API Backend (under development)

[![Build Status](https://travis-ci.org/henryvalbuena/the-mother-ship.svg?branch=master)](https://travis-ci.org/henryvalbuena/the-mother-ship)

[![Version Status](https://img.shields.io/github/manifest-json/v/henryvalbuena/the-mother-ship)](https://img.shields.io/github/manifest-json/v/henryvalbuena/the-mother-ship)


# The Mother Ship

RESTful API backend provider for frontend apps hosted on AWS

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
docker and docker-compose
```

### Commands to Build and Run

> Notice that project_name matches the service name used in *docker-compose.yaml*

### Build Project
```
docker-compose run --rm [project_name] django-admin startproject [project-name] .
```
### Build Apps
```
docker-compose run --rm [project_name] django-admin startapp [app_name]
```

### Run compose
```
docker-compose up
```

### Stop compose
```
docker-compose stop
```

### Build before start
```
docker-compose up --build
```

### Run tests
```
docker-compose run app sh -c "./manage.py test && flake8"
```

### And coding style tests

These test follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines

```
docker-compose run app sh -c "./manage.py flake8"
```

## Deployment

TBD

## Built With

TDD, Django, Django Rest Framework, Docker, and Postgres

* [Django](https://docs.djangoproject.com/en/2.2/) - Web framework
* [Rest Framework](https://www.django-rest-framework.org/) - RESTful API framework
* [Docker](https://www.docker.com/) - Environments and containers
* [PostgreSQL](https://www.postgresql.org/) - Database

## Contributing

Send a PR

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Henry Valbuena** - *Initial work* - [Henry](https://github.com/henryvalbuena)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* [Template link](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
by [@PurpleBooth](https://github.com/PurpleBooth)
