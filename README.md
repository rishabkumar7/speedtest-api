# Flask Speedtest API

This is a Flask app that provides an API for running a speedtest and returning the download and upload speeds in Mbps. The app also includes an index page with a button to run the speedtest and display the results.

## Prerequisites

- Python 3.6 or higher
- Flask
- speedtest-cli

## Installation

1. Clone this repository:

``` bash
git clone https://github.com/rishabkumar7/speedtest-api.git`
```

2.Install the required packages:

``` bash
pip install -r requirements.txt
```

3.Run the app:

``` bash
python app.py
```

4.Visit `http://localhost:5000` in your web browser to view the index page.

## Usage

To run the speedtest and get the results in JSON format, make a GET request to the `/speedtest` endpoint. For example:

```bash
curl http://localhost:5000/speedtest
```

The response will be in JSON format and will include the download and upload speeds in Mbps:

```json
{
  "download_speed": 25.56,
  "upload_speed": 10.23
}
```

To view the index page, visit the root URL `http://localhost:5000`. Click the "Run Speedtest" button to start the speedtest and display the results.

## Deployment

This app can be deployed to a cloud hosting platform such as AWS, Azure, or GCP.

## Credits

This app uses the `speedtest-cli` library for running the speedtest. The animated GIF used for the loading spinner was sourced from [Giphy](https://giphy.com/).

## License

This project is licensed under the MIT License. See the [LICENSE]() file for details.
