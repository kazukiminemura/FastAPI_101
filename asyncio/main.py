import asyncio

async def fetch_data():
    print("Start fetching data...")
    await asyncio.sleep(4)  # Simulate a network delay
    print("Data fetched!")
    return {"data": 123}
  
async def perform_calculation():
    print("Start calculation...")
    await asyncio.sleep(2)  # Simulate a computation delay
    print("Calculation done!")
    return 456
  
async def main():
  print("Before fetching data and calculation")
  await asyncio.gather(fetch_data(), perform_calculation())
  print("After fetching data and calculation")
  
asyncio.run(main())