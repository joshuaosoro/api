from fastapi import FastAPI
import sqlalchemy as sa
import pandas as pd

meta = sa.MetaData()
#conn_str = "postgresql://postgres:postgres@localhost:5432"
conn_str = "sqlite:///sqldb.db"
engine = sa.create_engine(conn_str, future=True)

app = FastAPI()


@app.get("/")
def index():
	with engine.connect() as conn:
		df = pd.read_sql_table("penguins", conn)
	return df.to_dict(orient="records")

@app.get('/penguin/{penguin_id}')
def get_penguin(penguin_id):
	with engine.connect() as conn:
		df = pd.read_sql_table("penguins", conn)
	
	for d in df.to_dict(orient = "records"):
		if str(d["id"]) ==  penguin_id:
			return d
	
