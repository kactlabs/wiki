/ [Home](index.md)

# Activepieces Setup

## Docker commands (both for linux and for windows)

```
docker run -d \
  -p 8080:80 \
  -v ~/.activepieces:/root/.activepieces \
  -e AP_QUEUE_MODE=MEMORY \
  -e AP_DB_TYPE=SQLITE3 \
  -e AP_FRONTEND_URL="http://localhost:8080" \
  activepieces/activepieces:latest
  ```
  * After running the command you can access the activepieses in this link http://localhost:8080

