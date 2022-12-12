create table users (
	id serial NOT NULL,
	user_id VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	birth_date VARCHAR(50) NOT NULL,
	CONSTRAINT id_pk PRIMARY KEY (id),
	CONSTRAINT email_pk UNIQUE (email)
);

create table tweets (
	id serial NOT NULL,
	tweet_id VARCHAR(50) NOT NULL,
	content VARCHAR(280) NOT NULL,
	created_at VARCHAR(50) NOT NULL,
	update_at VARCHAR(50) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (id)
		REFERENCES users (id)
		ON DELETE CASCADE
);

create table password (
	id serial NOT NULL,
	password VARCHAR(50) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (id)
		REFERENCES users (id)
		ON DELETE CASCADE
);