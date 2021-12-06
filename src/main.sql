CREATE TABLE user(
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	mobile_number INTEGER,
	email TEXT,
	location TEXT,
	/*1=todo,2=sent,3=received*/
	order_status INTEGER,
	created_at INTEGER,
	updated_at TIMESTAMP DEFAULT NOW
);

CREATE TABLE onSale(
	id INTEGER PRIMARY KEY,
	item TEXT NOT NULL UNIQUE,
	amount INTEGER NOT NULL,
	created_at INTEGER,
	updated_at TIMESTAMP DEFAULT NOW
);
