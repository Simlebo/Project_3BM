from entsoe import EntsoePandasClient
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

client = EntsoePandasClient(api_key='ef81833e-bb7d-4ddc-826d-9dd8c26de4ba')

country_code = 'BE'

def create_entsoe_price_plot():
    try:
        start_date = pd.Timestamp.now(tz='Europe/Brussels')
        end_date = start_date + pd.Timedelta(days=1)
        data = client.query_day_ahead_prices(country_code, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error fetching electricity prices: {e}")
        return None


def get_average_electricity_price(duration_minutes, base_time=None):
    
    data = create_entsoe_price_plot()
    if data is not None:
        if base_time is None:
            base_time = pd.Timestamp.now(tz='Europe/Brussels')
        end_time = base_time + pd.Timedelta(minutes=duration_minutes)
        period_data = data[(data.index >= base_time) & (data.index < end_time)]
        if not period_data.empty:
            return float(period_data.mean())
    return None

def get_average_electricity_price_over_period(start_offset_minutes, duration_minutes, base_time=None):
    
    data = create_entsoe_price_plot()
    if data is not None:
        if base_time is None:
            base_time = pd.Timestamp.now(tz='Europe/Brussels')
        start_time = base_time + pd.Timedelta(minutes=start_offset_minutes)
        end_time = start_time + pd.Timedelta(minutes=duration_minutes)
        period_data = data[(data.index >= start_time) & (data.index < end_time)]
        if not period_data.empty:
            return float(period_data.mean())
    return None


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
