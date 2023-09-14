.mode column
.headers on
--PRAGMA foreign_keys = ON;

CREATE TABLE race_types (
    race_id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT
);

CREATE TABLE runners (
    runner_id INTEGER PRIMARY KEY,
    name TEXT,
    gender TEXT,
    email TEXT
);

CREATE TABLE races (
    track_race_id INTEGER PRIMARY KEY,
    race_id INTEGER,
    challenge_type TEXT
);

CREATE TABLE runtimes (
    runner_id INTEGER,
    track_race_id INTEGER,
    runtime NUMERIC(5, 2),
    finished TEXT
);


INSERT INTO race_types VALUES (1, "bridge challenge", "Jumping over bridges, I guess");
INSERT INTO race_types VALUES (2, "ruby marathon", "Collecting rubies");
INSERT INTO race_types VALUES (3, "sea to mountain sprint", "Sprinting in Atlantic");
INSERT INTO race_types VALUES (4, "flat and fast marathon", "Running like a pig");
INSERT INTO race_types VALUES (5, "wine route stroll", "Race drunk");

INSERT INTO runners VALUES (1, "Favour Okeke", "M", "okeke@gmail.com");
INSERT INTO runners VALUES (2, "Philip", "M", "phili@gmail.com");
INSERT INTO runners VALUES (3, "Aarthi", "F", "aa@gmail.com");
INSERT INTO runners VALUES (4, "Minh", "F", "minh@gmail.com");
INSERT INTO runners VALUES (5, "Trang", "F", "tean@gmail.com");

INSERT INTO races VALUES (1, 1, "terrain");
INSERT INTO races VALUES (2, 2, "terrain");
INSERT INTO races VALUES (3, 3, "terrain");
INSERT INTO races VALUES (4, 4, "marathon");
INSERT INTO races VALUES (5, 2, "marathon");

INSERT INTO runtimes VALUES (3, 4, 12.32, "Yes");
INSERT INTO runtimes VALUES (4, 4, 13.00, "Yes");
INSERT INTO runtimes VALUES (2, 4, 10.23, "Yes");
INSERT INTO runtimes VALUES (5, 4, 15.86, "Yes");
INSERT INTO runtimes VALUES (3, 5, 13.98, "Yes");

SELECT name, runtime FROM runtimes
    JOIN runners ON runtimes.runner_id == runners.runner_id
    WHERE runners.gender == "F" AND track_race_id == 4
    ORDER BY runtime
    LIMIT 3;

SELECT name, COUNT(*) AS race_count FROM runners
    JOIN runtimes ON runtimes.runner_id == runners.runner_id
    JOIN races ON races.track_race_id == runtimes.track_race_id
    WHERE challenge_type == "marathon" AND finished == "Yes"
    GROUP BY email
    HAVING race_count == 2;
