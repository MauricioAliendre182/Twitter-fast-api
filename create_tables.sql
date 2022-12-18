create table users (
	email VARCHAR(50) NOT NULL,
	user_id VARCHAR(50) NOT NULL,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	birth_date VARCHAR(50) NOT NULL,
	CONSTRAINT id_pk PRIMARY KEY (user_id),
	CONSTRAINT user_pk UNIQUE (user_id),
	CONSTRAINT email_pk UNIQUE (email)
);

create table tweets (
	tweet_id VARCHAR(50) NOT NULL,
	content VARCHAR(280) NOT NULL,
	created_at VARCHAR(50) NOT NULL,
	update_at VARCHAR(50) NOT NULL,
	user_id VARCHAR(50) NOT NULL,
	PRIMARY KEY (tweet_id),
	CONSTRAINT tweet_pk UNIQUE (user_id),
	CONSTRAINT fk_user
	FOREIGN KEY (user_id)
		REFERENCES users (user_id)
		ON DELETE CASCADE
);

create table passwords (
	password VARCHAR(50) NOT NULL,
	user_id VARCHAR(50) NOT NULL,
	PRIMARY KEY (password),
	CONSTRAINT password_pk UNIQUE (password),
	CONSTRAINT fk_user
	FOREIGN KEY (user_id)
		REFERENCES users (user_id)
		ON DELETE CASCADE
);