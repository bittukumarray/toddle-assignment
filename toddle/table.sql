-- User is a model already present in Django, 
-- and I have mapped by Foreign key to this table (User) 
-- from Tables Survey, SurveyResponse, and QuestionResponse



CREATE TABLE Survey(
    id int NOT NULL,
    name VARCHAR(255),
    created_by VARCHAR,
    PRIMARY KEY (id),
    FOREIGN KEY (created_by) REFERENCES User(username)
);


CREATE TABLE Question(
    id int NOT NULL,
    title VARCHAR(1000),
    survey int,
    PRIMARY KEY (id),
    FOREIGN KEY (survey) REFERENCES Survey(id)
);


CREATE TABLE SurveyResponse(
    id int NOT NULL,
    survey int,
    respondent VARCHAR,
    PRIMARY KEY (id),
    FOREIGN KEY (survey) REFERENCES Survey(id),
    FOREIGN KEY (respondent) REFERENCES User(username)

);

CREATE TABLE QuestionResponse(
    id int NOT NULL,
    survey_response int,
    question int,
    respondent VARCHAR,
    ans_given BOOLEAN,
    PRIMARY KEY (id),
    FOREIGN KEY (survey_response) REFERENCES SurveyResponse(id),
    FOREIGN KEY (question) REFERENCES Question(id),
    FOREIGN KEY (respondent) REFERENCES User(username)
);



