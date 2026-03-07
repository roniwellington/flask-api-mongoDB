from pydantic import BaseModel, ConfigDict
from datetime import date, datetime

class Sale(BaseModel):
    sale_date: date
    product_id: str
    quantify: int
    total_value: float


    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )
