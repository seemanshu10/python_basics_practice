import data_fetcher
import data_parser

def main():
    print("Starting the Weather Application...")
    data = data_fetcher.fetch_weather_data()
    data_parser.parse_weather_data(data)

if __name__ == "__main__":
    main()