from .header import Header

BASIC_HEADER = Header(
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0"},
    Accept='*/*',
    DNT=1,
    Connection="keep-alive"
)
