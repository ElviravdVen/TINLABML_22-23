USE collected;

CREATE TABLE wheel1 (
    M_TIMESTAMP timestamp,
    M_CLIENT_NAME char,
    S_SPEED_X float, 
    S_SPEED_Y float,
    S_SPEED_Z float,
    S_RPM smallint,
    S_GEAR tinyint,
    S_ANGLE float,
    S_Z float,
    S_DAMAGE float,
    S_TRACK_POSITION float,
    S_RACE_POSITION tinyint,
    S_DISTANCE_RACED float,
    S_DISTANCE_FROM_START float,
    S_CURRENT_LAPTIME float,
    S_LAST_LAPTIME float,
    S_TIMESTAMP date,
    A_ACCELERATION float,
    A_BRAKE float,
    A_GEAR tinyint,
    A_STEER float,
    A_CLUTCH float,
    PRIMARY KEY (M_TIMESTAMP, M_CLIENT_NAME) 

)

