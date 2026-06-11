-- Find all high-priority open tickets assigned to engineer1
-- Pretty straightforward filter on three columns
SELECT
    ticket_id,
    status,
    priority,
    assigned_to
FROM tickets
WHERE status = 'open'
  AND assigned_to = 'engineer1'
  AND priority = 'high';
