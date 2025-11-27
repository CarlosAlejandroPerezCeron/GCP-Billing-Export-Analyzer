SELECT
  service.description AS service,
  project.id AS project_id,
  DATE(usage_start_time) AS date,
  SUM(cost) AS total_cost
FROM `${GCP_PROJECT_ID}.${BQ_DATASET}.${BQ_TABLE}`
WHERE cost > 0
GROUP BY service, project_id, date
ORDER BY date DESC;
