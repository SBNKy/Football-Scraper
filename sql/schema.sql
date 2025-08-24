DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    competition_name VARCHAR(50) NOT NULL,
    position INT NOT NULL,
    team_name VARCHAR(50) NOT NULL,
    matches_played INT NOT NULL,
    wins INT NOT NULL,
    draws INT NOT NULL,
    losses INT NOT NULL,
    goals_scored INT NOT NULL,
    goals_conceded INT NOT NULL,
    goals_diff INT GENERATED ALWAYS AS (goals_scored - goals_conceded) STORED,
    points INT NOT NULL,
    expected_goals NUMERIC(3, 2) NOT NULL,
    expected_goals_conceded NUMERIC(3, 2) NOT NULL,
    expected_goals_diff NUMERIC(3, 2) GENERATED ALWAYS AS (expected_goals - expected_goals_conceded) STORED,
    expected_goals_diff_90_min NUMERIC(3, 2) NOT NULL,
    last_5 VARCHAR(20) NOT NULL,
    top_team_scorer VARCHAR(100) NOT NULL,
    attendance INT NOT NULL
);

CREATE TABLE players (
    id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    team_id INT REFERENCES teams(id),
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);


