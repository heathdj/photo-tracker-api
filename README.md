# Photo Tracker API

A Django Rest API for the Photo Tracking App as a RestAPI.

This project uses github actions for testing, building containers and deploying.

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[!build](https://img.shields.io/github/actions/workflow/status/heathdj/photo-tracker-api/tests.yml)

## Deployment

To deploy this project for development:

```bash
  docker compuse up
```

To deploy for testing:

```bash
    docker compose run --rm app sh -c 'python manage.py wait_for_db && python manage.py test && flake8
```

To deploy in production:

```bash
    TBD
```

## API Reference

Wehn running the API provides a Swagger API for reference. The following API is for reference only.

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contributing

We welcome pull requestions from the users for this project. If you wish to make a feature update or fix a bug we ask that you claim an issue or create an issue first for tracking purposes.

## Authors

- [@heathdj](https://www.github.com/octokatherinheathdje) David Heath
