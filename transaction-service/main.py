from fastapi import FastAPI
from schema import TransactionCreate

app = FastAPI()

@app.post("/transaction")
async def ingestTransactions(
    txn: TransactionCreate
):
    try:
        print("check")
    except:
        print("error")