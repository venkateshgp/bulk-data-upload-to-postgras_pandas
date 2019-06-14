#!/usr/bin/env/python

import psycopg2
import os
from io import StringIO
import pandas as pd

# Get a database connection
dsn = os.environ.get('DB_DSN')  # Use ENV vars: keep it secret, keep it safe
conn = psycopg2.connect(dsn)

# Do something to create your dataframe here...
df = pd.read_csv("file.csv")

# Initialize a string buffer
sio = StringIO()
sio.write(df.to_csv(index=None, header=None))  # Write the Pandas DataFrame as a csv to the buffer
sio.seek(0)  # Be sure to reset the position to the start of the stream

# Copy the string buffer to the database, as if it were an actual file
with conn.cursor() as c:
    c.copy_from(sio, "schema.table", columns=dataframe.columns, sep=',')
    conn.commit()