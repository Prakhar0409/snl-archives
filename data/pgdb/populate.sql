--dropping tables--
-- DROP TABLE rating cascade;
-- DROP TABLE actor_title cascade;
-- DROP TABLE title cascade;
-- DROP TABLE episode cascade;
-- DROP TABLE actor cascade;
-- DROP TABLE host cascade;
-- DROP TABLE season cascade;



-- create seasons table --
create table season (
sid int primary key not null,
year int not null 
);

-- create episodes table --
create table episode (
sid int not null,
eid int not null,
aired varchar(100),
primary key (sid,eid),
foreign key (sid) references season(sid) on delete cascade
);

--create table for hosts --
CREATE TABLE host (
sid int not null,
eid int not null,
aid varchar(100),
primary key (sid,eid,aid),
foreign key (sid) references season(sid) on delete cascade
);

-- create table for the titles -- 
create table title (
sid int not null,
eid int not null,
tid int not null,
name varchar(500),
type varchar(100),
primary key (sid,eid,tid),
foreign key (sid,eid) references episode(sid,eid)
);

-- create table for the actors -- 
create table IF NOT EXISTS actor (
aid varchar(100) primary key not null,
name varchar(100),
isCast int   		--isCast= 0 if a snl cast, 1 if a celebrity --
);

-- create table for actor_vs_title --
create table actor_title (
sid int not null,
eid int not null,
tid int not null,
aid varchar(100) references actor(aid),
type varchar(100),			-- host or crew or cast --
foreign key (sid,eid,tid) references title(sid,eid,tid)
);

-- create table for ratings --
CREATE TABLE IF NOT EXISTS rating (
sid INT NOT NULL,
eid INT NOT NULL,
one INT,
ten INT,
two INT,
three INT,
four INT,
five INT,
six INT,
seven INT,
eight INT,
nine INT,

age18_29 INT,
age18_29_avg REAL,

age30_44 INT,
age30_44_avg REAL,

age45p INT,				--over 45 or 45 plus -- 
age45p_avg REAL,

age18m INT,				--under 18 or 18 minus--
age18m_avg REAL,

females REAL,

fage18_29 INT,
fage18_29_avg REAL,

fage30_44 INT,
fage30_44_avg REAL,

fage45p INT,
fage45p_avg REAL,

fage18m INT,
fage18m_avg REAL,

favg REAL,

imdb_staff INT,
imdb_staff_avg REAL,

imdb_users INT,
imdb_users_avg REAL,

males REAL,

mage18_29 INT,
mage18_29_avg REAL,

mage30_44 INT,
mage30_44_avg REAL,

mage45p INT,
mage45p_avg REAL,

mage18m INT,
mage18m_avg REAL,

mavg REAL,

non_us INT,
non_us_avg REAL,

top1k INT,		-- top 1000 voters --
top1k_avg REAL,

us INT,			-- us users --
us_avg REAL,

PRIMARY KEY (sid,eid),
FOREIGN KEY (sid,eid) REFERENCES episode(sid,eid)
);



-- population of the database --

--populate seasons--
COPY season FROM '/Users/prakhar0409/random/snl-dbms/data/snl_season.csv' WITH DELIMITER ',' CSV HEADER;

--populate episode--
COPY episode FROM '/Users/prakhar0409/random/snl-dbms/data/snl_episode.csv'  WITH DELIMITER ',' CSV HEADER;
-- COPY episode FROM '/Users/prakhar0409/random/snl-dbms/data/snl_episode_pipe_separated.csv'  WITH DELIMITER '|' CSV HEADER;

--populate host--
COPY host FROM '/Users/prakhar0409/random/snl-dbms/data/snl_host.csv' WITH DELIMITER ',' CSV HEADER;

--populate titles--
COPY title FROM '/Users/prakhar0409/random/snl-dbms/data/snl_title.csv' WITH DELIMITER ',' CSV HEADER;

--populate actors--
COPY actor FROM '/Users/prakhar0409/random/snl-dbms/data/snl_actor.csv' WITH DELIMITER ',' CSV HEADER;

--populate actors_vs_titles--
COPY actor_title FROM '/Users/prakhar0409/random/snl-dbms/data/snl_actor_title.csv' WITH DELIMITER ',' CSV HEADER;

--populate ratings--
COPY rating FROM '/Users/prakhar0409/random/snl-dbms/data/snl_rating.csv' WITH DELIMITER ',' CSV HEADER;
