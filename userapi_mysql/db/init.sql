CREATE DATABASE apiusers;
use apiusers;

CREATE TABLE users (
  username VARCHAR(40),
  firstname VARCHAR(20),
  lastname VARCHAR(20)
);

INSERT INTO users
  (username, firstname, lastname)
VALUES
  ('andy','andrew','andrews'),
  ('bazzab','barry','brown'),
  ('charliec','charles','chaplin'),
  ('dags','david','downer');
