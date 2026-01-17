from pydantic import BaseModel, Field, IPvAnyAddress
from uuid import UUID, uuid4
from datetime import datetime, timezone
from typing import Any, Dict
from model import TransactionStatus


class TransactionBase(BaseModel):
    
    amount:int = Field(..., gt=0, description="Amount in smallest currency unit")
    currency:str
    merchant_category:str
    source_ip:IPvAnyAddress
    device_id:str
    correlation_id:UUID = Field(default_factory=uuid4)
    metadata:Dict[str, Any] = Field(default_factory=dict)
    status: TransactionStatus = TransactionStatus.PENDING
   
class TransactionCreate(TransactionBase):
    user_id:str = Field(..., min_length=3, max_length=50)


class TransactionResponse(TransactionBase):
    transaction_id:UUID 
    user_id:str
    created_at:datetime = Field(default_factory=lambda:datetime.now(timezone.utc))

