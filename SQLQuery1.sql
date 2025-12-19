USE RestaurantFeedbackDatabase;

CREATE TABLE feedback (
    id INT IDENTITY(1,1) PRIMARY KEY,
    text NVARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT GETDATE()
);

SELECT *
FROM feedback;
