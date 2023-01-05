-- Returns how much time a person spent on a place

SELECT day, person_id, sum(exit_time - arrival_time) as time_spent
FROM person_data
GROUP BY day, person_id
