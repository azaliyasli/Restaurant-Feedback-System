CREATE DATABASE RestaurantFeedbackDatabase;
USE RestaurantFeedbackDatabase;

CREATE TABLE comments (
	comment_id INT AUTO_INCREMENT PRIMARY KEY,
    comment VARCHAR(300) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE feedbacks (
    feedback_id INT NOT NULL,
    feedback VARCHAR(300),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (feedback_id) REFERENCES comments(comment_id)
);

SELECT *
FROM feedbacks;

SELECT * 
FROM comments;