CREATE DATABASE IF NOT EXISTS stock;
USE stock;

DROP TABLE IF EXISTS TCB;
CREATE TABLE TCB (
    time DATETIME NOT NULL,
    open BIGINT NOT NULL,
    high BIGINT NOT NULL,
    low BIGINT NOT NULL,
    close BIGINT NOT NULL,
    volumne BIGINT NOT NULL,
    ticker CHAR(5) NOT NULL
)
ALTER TABLE TCB ORDER BY time;

DROP TABLE IF EXISTS HPG;
CREATE TABLE HPG (
    time DATETIME NOT NULL,
    open BIGINT NOT NULL,
    high BIGINT NOT NULL,
    low BIGINT NOT NULL,
    close BIGINT NOT NULL,
    volumne BIGINT NOT NULL,
    ticker CHAR(5) NOT NULL
)
ALTER TABLE HPG ORDER BY time;

DROP TABLE IF EXISTS SSI;
CREATE TABLE SSI (
    time DATETIME NOT NULL,
    open BIGINT NOT NULL,
    high BIGINT NOT NULL,
    low BIGINT NOT NULL,
    close BIGINT NOT NULL,
    volumne BIGINT NOT NULL,
    ticker CHAR(5) NOT NULL
)
ALTER TABLE SSI ORDER BY time;

DROP TABLE IF EXISTS VIC;
CREATE TABLE VIC (
    time DATETIME NOT NULL,
    open BIGINT NOT NULL,
    high BIGINT NOT NULL,
    low BIGINT NOT NULL,
    close BIGINT NOT NULL,
    volumne BIGINT NOT NULL,
    ticker CHAR(5) NOT NULL
)
ALTER TABLE VIC ORDER BY time;

DROP TABLE IF EXISTS VHM;
CREATE TABLE VHM (
    time DATETIME NOT NULL,
    open BIGINT NOT NULL,
    high BIGINT NOT NULL,
    low BIGINT NOT NULL,
    close BIGINT NOT NULL,
    volumne BIGINT NOT NULL,
    ticker CHAR(5) NOT NULL
)
ALTER TABLE VHM ORDER BY time;