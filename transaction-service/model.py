from pydantic import BaseModel, ValidationError, Field, IPvAnyAddress
from uuid import UUID,uuid4
from enum import Enum
from typing import Dict, Any
from datetime import datetime, timezone

class TransactionStatus(str, Enum):
    PENDING = "PENDING"
    VALIDATING = "VALIDATING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    FLAGGED = "FLAGGED"


class Transactions(BaseModel):
    transaction_id:UUID = Field(default_factory=uuid4)
    user_id:str = Field(..., min_length=3, max_length=50)
    amount:int = Field(..., gt=0, description="Amount in smallest currency unit")
    currency:str
    merchant_category:str
    source_ip:IPvAnyAddress
    device_id:str
    correlation_id:UUID = Field(default_factory=uuid4)
    metadata:Dict[str, Any] = Field(default_factory=dict)
    status: TransactionStatus = TransactionStatus.PENDING
    created_at:datetime = Field(default_factory=lambda:datetime.now(timezone.utc))

    class Config:
        # This allows the model to work with SQLAlchemy objects later
        from_attributes = True



