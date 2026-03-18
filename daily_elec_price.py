from entsoe import EntsoePandasClient
import pandas as pd
import matplotlib.pyplot as plt


client = EntsoePandasClient(api_key='b9240fd6-199e-47c9-8d2e-b9de5abaa625' )


# Define the parameters for the query
country_code = 'BE'  # Belgium
start_date = pd.Timestamp.now(tz='Europe/Brussels')  # first argument: the date YYYYMMDD
end_date   =start_date + pd.Timedelta(days=1)  # second argument: the time zone

# Fetch the data
data = client.query_day_ahead_prices(country_code, start=start_date, end=end_date)
# Display the data
plt.close("all")
data.plot()
plt.title('Belgian electrical consumption')
plt.show()

