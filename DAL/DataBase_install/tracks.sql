CREATE TABLE tracks AS
  SELECT *
  FROM track inner join track_features on track.track_id= track_features.track_id ;
 