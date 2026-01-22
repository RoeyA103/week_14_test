from pydantic import BaseModel , Field
import pandas 

class SqlSchemas(BaseModel):
    weapon_id: str = Field(max_length=100)
    weapon_name: str =Field(max_length=100)
    weapon_type : str =Field(max_length=100)
    range_km : int 
    weight_kg :float
    manufacturer : str =Field(max_length=100)
    origin_country: str =Field(max_length=100)
    storage_location : str =Field(max_length=100)
    year_estimated: int
    risk_level : str =Field(max_length=100)


def validate_df(df):
    data = df.to_dict("records") 
    try:
        for row in data:
            SqlSchemas.model_validate(row)
        return df 
    except Exception as e:
        return e   