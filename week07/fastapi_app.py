from fastapi import (
    FastAPI,
    HTTPException,
    Query,
    Request
)

from fastapi.responses import JSONResponse

from pydantic import (
    BaseModel,
    Field
)

from typing import Optional
from typing import List

import uuid
import datetime

app = FastAPI(
    title="FinTrust Transaction API",
    version="1.0.0"
)


class TransactionIn(BaseModel):

    account_id: str = Field(
        ...,
        min_length=1
    )

    amount: float = Field(
        ...,
        gt=0
    )

    currency: str = Field(
        ...,
        pattern=r'^[A-Z]{3}$'
    )

    description: Optional[str] = None


class TransactionOut(TransactionIn):

    id: str
    status: str
    created_at: str


class StatusUpdate(BaseModel):

    status: str

    def validate_status(self):

        allowed = [
            "approved",
            "rejected"
        ]

        if self.status not in allowed:
            raise ValueError(
                "Status must be approved or rejected"
            )


transactions = []


@app.middleware("http")
async def request_id_middleware(
        request: Request,
        call_next):

    request_id = str(
        uuid.uuid4()
    )

    response = await call_next(
        request
    )

    response.headers[
        "X-Request-ID"
    ] = request_id

    return response


@app.get('/health')
async def health():

    return {
        'status': 'ok'
    }


@app.post(
    '/transactions',
    response_model=TransactionOut,
    status_code=201
)
async def create_transaction(
    body: TransactionIn
):

    txn = {
        'id': str(uuid.uuid4()),
        **body.model_dump(),
        'status': 'pending',
        'created_at':
            datetime.datetime.utcnow()
            .isoformat()
    }

    transactions.append(txn)

    return txn


@app.get(
    '/transactions',
    response_model=List[
        TransactionOut
    ]
)
async def list_transactions(
    account_id:
    Optional[str] = Query(None)
):

    if account_id:

        return [
            t
            for t in transactions
            if t['account_id']
            == account_id
        ]

    return transactions


@app.get(
    '/transactions/{txn_id}',
    response_model=TransactionOut
)
async def get_transaction(
    txn_id: str
):

    for txn in transactions:

        if txn["id"] == txn_id:
            return txn

    raise HTTPException(
        status_code=404,
        detail="Transaction not found"
    )


@app.patch(
    '/transactions/{txn_id}/status'
)
async def update_status(
        txn_id: str,
        body: StatusUpdate
):

    if body.status not in [
        "approved",
        "rejected"
    ]:
        raise HTTPException(
            status_code=400,
            detail="Invalid status"
        )

    for txn in transactions:

        if txn["id"] == txn_id:

            txn["status"] = (
                body.status
            )

            return txn

    raise HTTPException(
        status_code=404,
        detail="Transaction not found"
    )