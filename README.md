# spreadly-data

### About

This repository is used to host off chain data for Spreadly. Users will be able to pull this repo down & server our database (coming soon). People who host database nodes will be incentivized through Spreadly tokens.

### Installation

Install dependencies
```
pip install -r requirements.txt
```

Pull latest rqlite docker image.
```
docker pull rqlite/rqlite
```

Running a single database node.
```
docker run -p4001:4001 rqlite/rqlite
```

### Usage

Run script to create authentication tables. 
```
python auth.py
```

