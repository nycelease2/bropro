CREATE TABLE IF NOT EXISTS user(
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	mobile_number INTEGER,
	email TEXT,
	location TEXT,
	/*1=todo,2=sent,3=received*/
	order_status INTEGER,
	orders CHAR,
	created_at INTEGER,
	updated_at INTEGER
);

CREATE TABLE IF NOT EXISTS onSale(
	id INTEGER PRIMARY KEY,
	item TEXT NOT NULL UNIQUE,
	amount INTEGER NOT NULL,
	unit CHAR NOT NULL,
	created_at INTEGER,
	updated_at TIMESTAMP DEFAULT NOW
);
