DROP TABLE IF EXISTS users;

CREATE TABLE users (
  username VARCHAR(40) PRIMARY KEY,
  firstname VARCHAR(20) NOT NULL,
  lastname VARCHAR(20) NOT NULL
);

INSERT INTO users
  (username, firstname, lastname)
VALUES
  ('andy','andrew','andrews'),
  ('bazzab','barry','brown'),
  ('charliec','charles','chaplin'),
  ('dags','david','downer');
