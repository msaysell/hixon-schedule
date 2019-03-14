from Hixon.settings import *
import dj_database_url

# Database
DATABASES = {
    'default':  dj_database_url.config(
        default="postgres://postgres:postgres@localhost:5432/hixon",
        conn_max_age=600)
}
