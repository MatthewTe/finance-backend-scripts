from sqlalchemy import create_engine, MetaData, Table, Column, String, Boolean, Integer

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# Main database Metadata object:
metadata_obj = MetaData()

company_table = Table(
    "main_company_tbl",
    metadata_obj,

    Column("id", String, primay_key=True),
    Column("name", String),
    Column("ticker", String),
    Column("public_status", Boolean),
    Column("cik", Integer),
    Column("home_country", String)

)

metadata_obj.create_all(engine)