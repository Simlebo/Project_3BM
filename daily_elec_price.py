from entsoe import EntsoePandasClient
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

client = EntsoePandasClient(api_key='b9240fd6-199e-47c9-8d2e-b9de5abaa625')

country_code = 'BE'
start_date = pd.Timestamp.now(tz='Europe/Brussels')
end_date = start_date + pd.Timedelta(days=1)

data = client.query_day_ahead_prices(country_code, start=start_date, end=end_date)
def create_entsoe_price_plot():
    return data
#plt.close("all")
#plt.figure(figsize=(10, 5))

#plt.step(data.index, data.values, where='mid', color='teal', linewidth=2)

# Format x-axis to show only hours and minutes
#ax = plt.gca()
#ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))  # Every 2 hours
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
#plt.xticks(rotation=0, ha='center')

#plt.title(f'Belgian Electricity Prices from {data.index[0].strftime("%d/%m/%Y")} to {data.index[-1].strftime("%d/%m/%Y")}')
#plt.xlabel('Time')
#plt.ylabel('Price (€/MWh)')
#plt.grid(True, linestyle='--', alpha=0.4)

#plt.tight_layout()
#plt.show()
