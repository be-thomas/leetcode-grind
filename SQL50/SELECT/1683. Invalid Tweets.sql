-- LENGTH: Returns the length of a string IN bytes.
-- CHAR_LENGTH: Returns the length of a string IN characters.
SELECT  tweet_id
FROM Tweets
WHERE char_length(content) > 15;