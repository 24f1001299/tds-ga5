import calendar
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/prorate")
async def prorate(req: Request):
    body = await req.json()

    old_price = body["old_price"]
    new_price = body["new_price"]
    year = body["year"]
    month = body["month"]
    upgrade_day = body["upgrade_day"]

    days_in_month = calendar.monthrange(year, month)[1]
    days_remaining = days_in_month - upgrade_day + 1

    charge = round((new_price - old_price) * (days_remaining / days_in_month), 2)

    return {"charge": charge}
